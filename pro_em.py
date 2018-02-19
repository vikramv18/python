# Python code to illustrate Sending mail with attachments from your Gmail account 
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("hvtvikkymax@gmail.com","vk18vikram")
message="how are you"
s.sendmail("hvtvikkymax@gmail.com","vikramv7654@gmail.com",message)
s.quit()
print("finish")
