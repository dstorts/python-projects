import smtplib

my_email = "dylanstorts33@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
    gmail_connection.starttls() #start secure connection setup
    gmail_connection.login(user=my_email, password="N#RatbAdf2019g")
    gmail_connection.sendmail(from_addr=my_email, to_addrs="dylanstorts33@hotmail.com",
                              msg="Subject:Python Hello\n\nHello from PYTHON")
