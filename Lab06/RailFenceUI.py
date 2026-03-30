import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class RailFenceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nhập văn bản (Plaintext/Ciphertext):"))
        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        layout.addWidget(QLabel("Nhập số hàng (Key - Integer):"))
        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        self.btn_encrypt = QPushButton("Mã hóa (Encrypt)")
        self.btn_decrypt = QPushButton("Giải mã (Decrypt)")
        layout.addWidget(self.btn_encrypt)
        layout.addWidget(self.btn_decrypt)

        layout.addWidget(QLabel("Kết quả:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)
        self.setWindowTitle('Rail Fence Cipher - Lab06')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RailFenceApp()
    sys.exit(app.exec_())