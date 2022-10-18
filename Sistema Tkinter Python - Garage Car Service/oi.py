import smtplib

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()

smtp.login('samuka.20100@gmail.com', 'S@muel20191998')

de = 'samuka.20100@gmail.com'
para = ['samuka.20100@outlook.com']
msg = """From: %s
To: %s
Subject: Buteco Open Source

Email de teste do Buteco Open Source.""" % (de, ', '.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()