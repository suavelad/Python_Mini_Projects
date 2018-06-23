
#! usr/bin/python3
"""
This GUI Program encrypts and decrypts messages
"""

import sys
import pyperclip

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
     
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        form= QFormLayout()
        info=QLabel("This Application help\'s you encrypt and decrypt messages")
        modeLabel=QLabel("Mode: ")
        self.modeEn=QRadioButton("Encrypt")
        self.modeDe=QRadioButton("Decrypt")

        Hmode=QHBoxLayout()
        Hmode.addWidget(self.modeEn)
        Hmode.addWidget(self.modeDe)

        keyLabel=QLabel("Secret Key: ")
        self.keyinput=QLineEdit("0-26")

        msgLabel= QLabel("Insert the Message ")
        self.msginput=QTextEdit() 

        self.submitBtn= QPushButton("SUBMIT")
        self.submitBtn.clicked.connect(self.Cipher)


        form.addRow(info)
        form.addRow(modeLabel,Hmode)
        form.addRow(keyLabel,self.keyinput)
        form.addRow(msgLabel)
        form.addRow(self.msginput)
        form.addRow(self.submitBtn)

        self.setLayout(form)
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Cipher Application")

    def Cipher(self):
        
        try:
            if self.modeEn.isChecked():
                mode="encrypt"
            elif self.modeDe.isChecked():
                mode="decrypt"
            
            message=self.msginput.toPlainText()
            key=int(self.keyinput.text())

            LETTERS= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            translated=''

            message= message.upper()

            for symbol in message:
                if symbol in LETTERS:
                    num=LETTERS.find(symbol)
                    if mode=="encrypt":
                        num=num+key
                    elif mode=="decrypt":
                        num=num-key
                    if  num >= len(LETTERS):
                        num= num- len(LETTERS)
                    elif num < 0:
                        num= num + len(LETTERS)
                    translated= translated + LETTERS[num]
                else:
                    translated=translated + symbol
            QMessageBox.information (self,"The {}ed Message ".format(mode),translated)
            pyperclip.copy(translated)
            

        except:
            QMessageBox.information(self,"Whoah !!!","Check what you inserted")    

    

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


