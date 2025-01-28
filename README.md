# Copy Paste Monitor

## Overview
**Copy Paste Monitor** is a cross-platform clipboard manager designed for systems with multiple monitors. This tool allows users to copy text, images, or files and paste them seamlessly to a selected monitor. It includes a graphical interface for easy monitor selection and supports automatic fallback to the primary monitor when only one is detected.

## Features
- **Cross-Platform Compatibility**: Works on macOS, Windows, and Linux.
- **Clipboard Content Management**:
  - Supports text and can be extended for images and files.
- **Multi-Monitor Support**:
  - Detects all connected monitors.
  - Allows users to select the target monitor via a modern GUI.
- **Global Hotkey**: Quickly trigger the tool using the `F12` key.
- **Automatic Fallback**: Defaults to the primary monitor when only one is detected.
- **Compiled Executable**: A ready-to-use `.exe` is available for Windows users.

## Installation

### From Source
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/multiple_monitor_copyPaste.git
   cd multiple_monitor_copyPaste
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:
   ```bash
   python3 copyPaste.py
   ```

### From GitHub Releases
1. **Download the Precompiled `.exe`**:
   - Visit the [Releases page](https://github.com/yourusername/multiple_monitor_copyPaste/releases).
   - Download the latest version of `CopyPasteMonitor.exe`.

2. **Run the Application**:
   - Double-click `CopyPasteMonitor.exe` to launch.
   - No installation required.

## Usage
1. **Copy Content**:
   - Use `Ctrl+C` or **Right-Click > Copy** to copy text, images, or files.

2. **Launch the Tool**:
   - Run the script or open the precompiled `.exe`.

3. **Select a Monitor**:
   - Use the graphical interface to choose the monitor for pasting.
   - If only one monitor is detected, the tool defaults to the primary monitor.

4. **Paste Content**:
   - The tool pastes the content automatically or guides you for unsupported content types.

## Hotkey Support
- Press `F12` to trigger the tool globally.
- Ensure the application is running in the background for the hotkey to work.

## Requirements
- **Python 3.7 or Higher** (for source users).
- **Dependencies**:
  - `pyperclip`
  - `pyautogui`
  - `screeninfo`
  - `PyQt5`
- **Operating System**: Windows, macOS, or Linux.

## Known Limitations
- **Image and File Support**: Currently supports only text for automatic pasting. Image and file handling are planned for future releases.
- **Hotkey Scope**: The global hotkey must be enabled while the tool is running in the background.

## Contributing
We welcome contributions to improve the tool! To get started:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits
- **Author**: Your Name Here
- **GitHub**: [yourusername](https://github.com/yourusername)
