#! usr/bin/python3

"""
This GUI Application helps you send single email to receipients
"""

import sys
import smtplib


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from email.mime.text import MIMEText as text



class Window(QWidget):
     
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        form=QFormLayout()
        info=QLabel("This Application Help\'s you send emails")
        senderLabel=QLabel("Sender\'s Email Address : ")
        self.sender=QLineEdit()
        receiverLabel=QLabel("Receipient\'s Email Adress :")
        self.receiver=QLineEdit()

        self.msg=QTextEdit("Compose your message here")
        subjectLabel=QLabel("Subject: ")
        self.subjectText=QLineEdit()

        self.sendBtn=QPushButton("Submit")


        form.addRow(info)
        form.addRow(senderLabel)
        form.addRow(self.sender)
        form.addRow(receiverLabel)
        form.addRow(self.receiver)
        form.addRow(subjectLabel,self.subjectText)
        form.addRow(self.msg)
        form.addRow(self.sendBtn)
        self.sendBtn.clicked.connect(self.EmailSender)



        self.setGeometry(100,100,400,450)
        self.setWindowTitle(" Email Sender ")
        self.setLayout(form)
    



    def EmailSender(self):
        try:    
            message=self.msg.toPlainText()
            sndr=self.sender.text()
            receipient=self.receiver.text()
            subject=self.subjectText.text()

            m=text(message)
            m['Subject']=subject
            m['From']=sndr
            m['To']=receipient
                
            
            server= smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("youremail@gmail.com","xxxxxx")
            server.sendmail(sndr,receipient, m.as_string())
            server.quit()
            self.msg.clear()
            self.sender.clear()
            self.receiver.clear()

            QMessageBox.information (self,"Email Alert","Email Successfully Sent")
           
        except:
            QMessageBox.information (self,"Email Alert","Check your inputted information")


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())