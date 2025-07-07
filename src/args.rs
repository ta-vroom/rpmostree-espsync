use clap::{builder::OsStr, Parser};


#[derive(Parser)]
pub struct Args {
    #[arg(long)]
    pub verbose: bool,
    
    #[arg(short = 'p', long)]
    pub parents: bool,

    #[arg(long)]
    pub dry_run: bool,

    
    #[arg(short = 'f', long)]
    pub force: bool,

    #[arg(short = 'i', long)]
    pub input: Option<String>,

    #[arg(short = 'o', long, default_missing_value_os="/boot/efi")]
    pub output: Option<String>

} 