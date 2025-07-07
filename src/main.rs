mod args;
use args::Args;
use clap::Parser;
use std::{
    env,
    fs::{self, File, OpenOptions},
    io::{self, BufRead, BufReader, Write},
    os::unix::fs::MetadataExt,
    path::{Path, PathBuf},
    process::Command as ShellCommand,
};

fn main() -> io::Result<()> {
    let args = Args::parse();

    let dry_run = args.dry_run;
    let force = args.force;

    let input = Path::new(&args.input.unwrap_or("/boot".into())).join("loader");

    let active_dir = fs::read_link(input)
        .expect("Failed to resolve input directory")
        .join("entries");
    
    let esp = args.output.unwrap_or("/boot/efi".into());
    let efi = Path::new(&esp);
    let entries_dir = efi.join("loader/entries");

    if !efi.join("EFI").is_dir() {
        eprintln!("ESP not mounted");
        std::process::exit(1);
    }

    println!("Syncing from {:?}", active_dir);

    let mut no_entries = 0; 

    for entry in fs::read_dir(&active_dir)? {
        no_entries += 1;
        let entry = entry?;
        let path = entry.path();
        if !path.is_file() {
            continue;
        }

        let file_name = path
            .file_name()
            .and_then(|s| s.to_str())
            .unwrap_or_default();

        // let num: String = file_name.chars().filter(|c| c.is_numeric()).collect();

        // let output_path = entries_dir.join("ostree").join(num);


        if !entries_dir.exists() && args.parents {
            fs::create_dir_all(&entries_dir)?;
        }

        if entries_dir.exists() && !force && !dry_run {
            eprintln!(
                "Existing entry found in {:?}. Use -f or --force to overwrite.",
                entries_dir
            );
            std::process::exit(1);
        }

   
        let file = File::open(&path)?;
        for line in BufReader::new(file).lines() {
            let line = line?;
            let new_line = if line.starts_with("options") {
                line
            } else if line.starts_with("linux") || line.starts_with("initrd") {
                line.replace("/boot", "")
            } else if line.starts_with("aboot") {
                continue;
            } else {
                line
            };

            if dry_run {
                println!("{}", new_line);
            } else {
                let mut out = OpenOptions::new()
                    .create(true)
                    .append(true)
                    .open(entries_dir.join(&file_name))?;
                writeln!(out, "{}", new_line)?;
            }
        }
    }

    let _ = ShellCommand::new("bootctl")
        .args(["--path=/boot/efi", "update"])
        .output();

    println!("ESP sync complete.\n");
    println!("Copied {no_entries} configurations.");

    Ok(())
}
