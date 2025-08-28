import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from datetime import datetime

class JournalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Journal-CLI-Tool")
        self.resize(500, 400)

        # Central widgets
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Write what you feel... ")

        self.save_button = QPushButton("Save to journal")
        self.save_button.clicked.connect(self.save_entry)

        # Design
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def save_entry(self):
        text = self.text_edit.toPlainText().strip()
        if text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("my_journal.txt", "a", encoding="utf-8") as f:
                f.write(f"{timestamp} - {text}\n")
            self.text_edit.clear()
            self.statusBar().showMessage("Saved entry...", 3000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JournalWindow()
    window.show()
    sys.exit(app.exec())
