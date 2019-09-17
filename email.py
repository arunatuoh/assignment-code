import smtplib
s=smtplib.SMTP('smtplib.gmail.com',587)
s.starttls()
s.login("arunatuoh@gmail.com","uoh@456")
message="hello how are you"
s.sendmail("arunatuoh@gmail.com","arunsingrajput19@gmail.com",message)
s.quit()
