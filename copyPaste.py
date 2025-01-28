"""
Copy Paste Monitor

Author: morsnoctus
Email: secninjago@gmail.com
GitHub: https://github.com/mixedup4x4/multiple_monitor_copyPaste
Description: A cross-platform clipboard manager for multiple monitors.
Version: 1.0.0
License: MIT
"""
import pyperclip
import pyautogui
from screeninfo import get_monitors
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox, QWidget


class ClipboardManager(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_index = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Select Monitor")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        label = QLabel("Select a monitor to paste to:")
        layout.addWidget(label)

        self.monitor_list = QListWidget(self)
        monitors = get_monitors()
        for i, monitor in enumerate(monitors):
            monitor_info = f"Monitor {i + 1}: {monitor.width}x{monitor.height} at ({monitor.x}, {monitor.y})"
            self.monitor_list.addItem(monitor_info)
        layout.addWidget(self.monitor_list)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.select_monitor)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def select_monitor(self):
        selected_items = self.monitor_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Required", "Please select a monitor before proceeding.")
        else:
            self.selected_index = self.monitor_list.currentRow()
            self.close()

    def detect_clipboard_content(self):
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            return "text", clipboard_content
        return None, None

    def move_cursor_to_monitor(self, monitor_index):
        monitors = get_monitors()
        if monitor_index < 0 or monitor_index >= len(monitors):
            raise ValueError("Invalid monitor index.")

        monitor = monitors[monitor_index]
        center_x = monitor.x + monitor.width // 2
        center_y = monitor.y + monitor.height // 2
        pyautogui.moveTo(center_x, center_y)

    def main(self):
        try:
            # Step 1: Detect clipboard content
            content_type, clipboard_content = self.detect_clipboard_content()
            if not content_type:
                QMessageBox.warning(self, "Clipboard Empty", "Clipboard is empty or contains unsupported content.")
                return

            # Step 2: Detect monitors
            monitors = get_monitors()
            if len(monitors) == 1:
                QMessageBox.information(self, "Single Monitor", "Only one monitor detected. Defaulting to the primary monitor.")
                self.move_cursor_to_monitor(0)
            else:
                # Step 3: Show GUI and select monitor
                self.show()
                app.exec_()
                if self.selected_index is None:
                    return
                self.move_cursor_to_monitor(self.selected_index)

            # Step 4: Paste content
            if content_type == "text":
                pyautogui.hotkey("ctrl", "v" if pyautogui.platform == "win" else "command", "v")
                QMessageBox.information(self, "Success", "Text pasted successfully.")
            else:
                QMessageBox.warning(self, "Unsupported Content", "Only text is currently supported for pasting.")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication([])
    manager = ClipboardManager()
    manager.main()
