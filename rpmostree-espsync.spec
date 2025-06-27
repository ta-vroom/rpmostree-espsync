Name:           rpmostree-espsync
Version:        0.1
Release:        1%{?dist}
Summary:        Sync CoreOS kernel/initramfs to the ESP

License:        MIT
URL:            https://github.com/ta-vroom/rpmostree-espsync
Source0:        rpmostree-espsync.tar.gz

BuildArch:      noarch
Requires:       systemd >= 220, rpm-ostree

%description
Small helper that copies the current Fedora CoreOS
vmlinuz & initramfs into the systemd-boot ESP.

%prep
%autosetup -n %{name}-%{version}

%install
# We’re already inside BUILD/%{name}-%{version}
install -D -m 0755 esp-sync %{buildroot}%{_bindir}/esp-sync
install -D -m 0644 esp-sync.service %{buildroot}%{_unitdir}/esp-sync.service
install -D -m 0644 esp-sync.path %{buildroot}%{_unitdir}/esp-sync.path

%files
%license LICENSE
%{_bindir}/esp-sync

%changelog
* Fri Jun 27 2025  Your Name <you@example.com> - 0.1-2
- Add systemd helper macros and list unit files in %%files
- Switch Source0 to %%{name}-%%{version}.tar.gz for easier version bumps

* Mon Jun 23 2025  Your Name <you@example.com> - 0.1-1
- Initial package
