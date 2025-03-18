#!/bin/bash

# funtcion rmoving the "-" that way it looks good and is usable 
# NEW Added: now you can write comments using # 
# Eveything behind # will be ignored
extract_programs() {
    local file="$1"
    grep -E '^\s*- ' "$file" | sed 's/#.*//' | sed 's/^\s*- //' | tr '\n' ' '
}

#############################################
#               Preparation                 #
#############################################

# Update
sudo dnf update -y

# Add RPM Fusion repositories
sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf config-manager --enable fedora-cisco-openh264 -y

# Update package lists after adding repositories
sudo dnf update -y

#############################################
#                Installation               #
#############################################

# Read program lists from markdown files
binary_packages=$(extract_programs "binary.md")
flatpak_list=$(extract_programs "flatpak.md")

# Install packages
echo "Installing binary packages: $binary_packages"
sudo dnf install -y $binary_packages
sudo dnf update -y

# Add Flatpak repository and install Flatseal
sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
sudo flatpak install -y flathub com.github.tchx84.Flatseal

# Install Flatpaks
for flatpak in $flatpak_list; do
    sudo flatpak install -y flathub "$flatpak"
done

echo "All installations are complete!"
