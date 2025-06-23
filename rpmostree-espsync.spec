# RPM Spec file for esp-sync
# Save this as esp-sync.spec

Name:           esp-sync
Version:        0.1
Release:        1%{?dist}
Summary:        Sync Fedora CoreOS boot entries and kernels to the EFI System Partition

License:        MIT
URL:            https://github.com/youruser/esp-sync
Source0:        esp-sync.sh
Source1:        esp-sync.service
Source2:        esp-sync.path
BuildArch:      noarch
Requires:       systemd-boot-update # provided by systemd package
Requires(post): systemd
Requires(preun): systemd

%description
A tiny helper for OSTree‑based systems that copies the active loader directory
and matching kernel/initramfs to the EFI System Partition (ESP) after every
rpm‑ostree deployment.  This package installs the shell script plus a
systemd path‑activated unit so the copy runs automatically on each reboot
once a new deployment is finalised.

%prep
# Nothing to unpack – script & unit files are shipped as sources

%build
# Nothing to build – pure script + unit

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/esp-sync.sh
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/esp-sync.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/esp-sync.path

%post
# Enable the path unit so it triggers on each deployment
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
/usr/bin/systemctl enable --now esp-sync.path >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ] ; then
  /usr/bin/systemctl disable --now esp-sync.path >/dev/null 2>&1 || :
fi

%files
%license LICENSE
/usr/local/bin/esp-sync.sh
%{_unitdir}/esp-sync.service
%{_unitdir}/esp-sync.path

%changelog
* Mon Jun 23 2025 Your Name <you@example.com> - 0.1-1
- Initial package
# RPM Spec file for esp-sync
# Save this as esp-sync.spec

Name:           esp-sync
Version:        0.1
Release:        1%{?dist}
Summary:        Sync Fedora CoreOS boot entries and kernels to the EFI System Partition

License:        MIT
URL:            https://github.com/youruser/esp-sync
Source0:        esp-sync.sh
Source1:        esp-sync.service
Source2:        esp-sync.path
BuildArch:      noarch
Requires:       systemd-boot-update # provided by systemd package
Requires(post): systemd
Requires(preun): systemd

%description
A tiny helper for OSTree‑based systems that copies the active loader directory
and matching kernel/initramfs to the EFI System Partition (ESP) after every
rpm‑ostree deployment.  This package installs the shell script plus a
systemd path‑activated unit so the copy runs automatically on each reboot
once a new deployment is finalised.

%prep
# Nothing to unpack – script & unit files are shipped as sources

%build
# Nothing to build – pure script + unit

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/esp-sync.sh
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/esp-sync.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/esp-sync.path

%post
# Enable the path unit so it triggers on each deployment
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
/usr/bin/systemctl enable --now esp-sync.path >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ] ; then
  /usr/bin/systemctl disable --now esp-sync.path >/dev/null 2>&1 || :
fi

%files
%license LICENSE
/usr/local/bin/esp-sync.sh
%{_unitdir}/esp-sync.service
%{_unitdir}/esp-sync.path

%changelog
* Mon Jun 23 2025 Your Name <you@example.com> - 0.1-1
- Initial package
