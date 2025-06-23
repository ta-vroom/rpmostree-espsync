#!/usr/bin/env bash
set -euo pipefail

# 1) figure out which loader directory is active right now
ACTIVE_DIR="$(readlink -f /boot/loader)" # → /boot/loader.0  or  /boot/loader.1
echo "Syncing from ${ACTIVE_DIR}"

ESP=/boot/efi                       # already mounted by early boot
[ -d "${ESP}/EFI" ] || { echo "ESP not mounted"; exit 1; }

# 2) copy loader.conf and entries
rsync -a --delete \
      "${ACTIVE_DIR}/"              \
      "${ESP}/loader/"

# 3) be sure the systemd-boot binary itself is current
bootctl --path="${ESP}" update >/dev/null 2>&1 || true

echo "ESP sync complete."