Name:           sd-bootc
Version:        0.1
Release:        1%{?dist}
Summary:        Sync CoreOS kernel/initramfs to the ESP

License:        MIT
URL:            https://github.com/ta-vroom/sd-bootc
Source0:        sd-bootc.tar.gz

BuildArch:      noarch
Requires:       systemd >= 220, rpm-ostree

%description
Small helper that copies the current Fedora CoreOS
vmlinuz & initramfs into the systemd-boot ESP.

%prep
%autosetup -n %{name}-%{version}

%install
# We’re already inside BUILD/%{name}-%{version}
install -D -m 0755 sd-bootc %{buildroot}%{_bindir}/sd-bootc
install -D -m 0644 sd-bootc.service %{buildroot}%{_unitdir}/sd-bootc.service
install -D -m 0644 sd-bootc.path %{buildroot}%{_unitdir}/sd-bootc.service

%files
%license LICENSE
%{_bindir}/sd-bootc
%{_unitdir}/sd-bootc.service
%{_unitdir}/sd-bootc.service

%changelog
* Fri Jun 27 2025  Your Name <you@example.com> - 0.1-2
- Add systemd helper macros and list unit files in %%files
- Switch Source0 to %%{name}-%%{version}.tar.gz for easier version bumps

* Mon Jun 23 2025  Your Name <you@example.com> - 0.1-1
- Initial package
