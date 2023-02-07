import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox,QLineEdit, QFormLayout, QTextEdit

def showondisplay():
    freshlyentered = entertext.toPlainText()
    displaytext.setText(freshlyentered)
    
def encryption():
    original_text = entertext.toPlainText()
    # Add your encryption logic here
    encrypted_text = original_text  # replace this with the encrypted text
    displaytext.setText(encrypted_text)
    
def decryption():
    encrypted_text = displaytext.toPlainText()
    # Add your decryption logic here
    decrypted_text = encrypted_text # replace this with the decrypted text
    displaytext.setText(decrypted_text)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(900, 900)
    w.setWindowTitle('BojuAI')

    displaytext = QTextEdit(w)
    displaytext.resize(700,200)
    displaytext.move(50,50)
    displaytext.setReadOnly(True)
    displaytext.setStyleSheet('background-color: black; color:yellow')
    #displaytext.setPlaceholderText('Do not type here')

    entertext = QTextEdit(w)
    entertext.resize(700,200)
    entertext.move(50,400)
    entertext.setReadOnly(False)
    entertext.setStyleSheet('background-color: white; color:black')
    entertext.setPlaceholderText('Enter Text here')
    entertext.textChanged.connect(showondisplay)

    encrypt_button = QPushButton('Encrypt', w)
    encrypt_button.move(50, 630)
    encrypt_button.clicked.connect(encryption)

    decrypt_button = QPushButton('Decrypt', w)
    decrypt_button.move(200, 630)
    decrypt_button.clicked.connect(decryption)

    w.show()
    sys.exit(app.exec())
