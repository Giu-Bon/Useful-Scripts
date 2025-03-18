## Overview

This script automates the installation of programs. It reads from  `.md` files (`binary.md` and `flatpak.md`) for easy and pretty edit.


> ⚠️ **WARNING:** This script is **intended for Fedora Linux only**.
>>This is cause i am adding in the install Script Fedora repositories. 
It is really easy to adjust it for other Linux Distros 

---

## Features

- **Dynamic List Handling**:  
    Reads and installs programs listed in:
    - `binary.md` for `dnf` packages.
    - `flatpak.md` for Flatpak applications.
    
- **Automated Repository Setup**:  
    Configures repositories like RPM Fusion and Flathub.
    
- **System Updates**:  
    Ensures the system and installed packages are up-to-date.
    
- **Flatpak Configuration**:  
    Sets up the Flathub repository and installs Flatpak applications as a non-root user.

- **In total**:  
    Great for an initial Setup :)

    
---

## Requirements

- Fedora Linux
- User must have **sudo** privileges (part of the `wheel` group). Ofc since you wanna install sth.

---


## File Structure

```
.
├── Setup.sh               # The main script
├── binary.md              # List of Programms to install via dnf
└── flatpak.md             # List of Flatpak applications to install
```

### Example File Contents

#### `binary.md`

```markdown
# Binary Packages
## All Programms listed in here will be installed using dnf
- Programm
- Another-programm # Yeah this is a good Programm 
- And-Another-PROGRAMM # and this comment will be ignored
```

#### `flatpak.md`

```markdown
# Flatpak Applications
## All Programms listed in here will be installed using flatpak
- com.Programm.Client # Comment will be ignored :)
- com.old-Best.Browser-Firefox
- actual.Best.Browser-Brave 
```

---
## Usage

1. **Clone or Download** this folder of the repository to your system. And `cd` into it ofc.
2. **Ensure the script is executable**:
    
    ```bash
    chmod +x Setup.sh
    ```

3. **Modifying Program Lists**:  
    Edit the following files to include the programs you want to install:
    
    - `binary.md`: List of `dnf` packages.
    - `flatpak.md`: List of Flatpak applications.
    
    Use the bullet point format (`- program_name`).
    
    
4. **Run the script**
    > ⚠️ **WARNING:** do NOT use `sudo` to execute the script itself. it will request sudo for the things it needs it for
    
    ```bash
    ./Setup.sh
    ```

---

## Troubleshooting

1. **Markdown Files Missing**:  
    Ensure `binary.md` and `flatpak.md` exist in the same directory as the script.
    
2. **Flatpak Permissions**:  
    **Do not run the script with `sudo`!**  
    Flatpak installations should always be performed as a regular user for proper configuration.
    
3. **Script Permissions**:  
    If you encounter a `Permission Denied` error, ensure the script is executable:
    
    ```bash
    chmod +x Setup.sh
    ```
    
4. **User Permissions**:  
    Ensure your user is part of the `wheel` group to execute `sudo` commands within the script.



---

Have fun using Fedora

