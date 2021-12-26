import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt,QDateTime
# import library
class pencere(QDialog):
    def __init__(self):
        super().__init__()
        self.arayuz()
    def arayuz(self):
        self.grid = QGridLayout()
        self.gonderen = QLineEdit()
        self.yazi1 = QLabel("From: ")
        self.parola = QLineEdit()
        self.yazi6 = QLabel("Password: ")
        self.parola.setEchoMode(QLineEdit.Password)
        self.yazi5 = QLabel("E-Mail Account: ")
        self.eposta = QLineEdit("")

        self.gonderilen = QLineEdit()
        self.yazi2 = QLabel("To: ")

        self.konu = QLineEdit()
        self.yazi3 = QLabel("Subject: ")

        self.time = QLabel("")
        self.yazi9 = QTextEdit()
        self.yazi4 = QLabel("Write: ")

        self.yazi7 = QLabel("Mail gönderebilmek için uygulamalara izin ver butonu - AÇIK - seçilmelidir.\nİlk olarak daha az güvenli uygulamalar için öncelikle aşağıdaki linke gidiyoruz ve güvenliği kaldırıyoruz.\nhttps://myaccount.google.com/lesssecureapps")
        self.buton = QPushButton("Gönder")
        self.buton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        timer = QTimer(self)
        timer.timeout.connect(self.zaman)
        timer.start(1000)

        self.grid.addWidget(self.gonderen,1,1)
        self.grid.addWidget(self.yazi1,1,0)

        self.grid.addWidget(self.gonderilen,2,1)
        self.grid.addWidget(self.yazi2,2,0)

        self.grid.addWidget(self.konu,3,1)
        self.grid.addWidget(self.yazi3,3,0)

        self.grid.addWidget(self.yazi9,4,1)
        self.grid.addWidget(self.yazi4,4,0)

        self.grid.addWidget(self.eposta,1,3)
        self.grid.addWidget(self.yazi5,1,2)

        self.grid.addWidget(self.parola,2,3)
        self.grid.addWidget(self.yazi6,2,2)

        self.grid.addWidget(self.buton,3,3)
        self.grid.addWidget(self.yazi7,4,3)
        self.grid.addWidget(self.time,5,3)

        self.buton.clicked.connect(self.gonder)

        self.setWindowTitle("Mail Gönderici")
        self.setLayout(self.grid)
        self.show()

    def zaman(self):
        datetime = QDateTime.currentDateTime()
        displayTxt = datetime.toString()
        self.time.setText(displayTxt)

    def gonder(self):
        mesaj = MIMEMultipart()
        mesaj["From"] = self.gonderen.text()
        mesaj["To"] = self.gonderilen.text()
        mesaj["Subject"] = self.konu.text()
        yazi = self.yazi9.toPlainText()
        mesaj_govdesi = MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.eposta.text(),self.parola.text())
            mail.sendmail(self.gonderen.text(), self.gonderilen.text(), mesaj.as_string())
            print("Mail başarıyla gönderildi.")
            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu. Süreçleri kontrol ediniz.")
            sys.stderr.flush()
    def send():
        pass
app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())