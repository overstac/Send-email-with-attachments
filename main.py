import yagmail
import os
sender= "pintilei92@gmail.com"
receiver= "pintilei.catalin92@gmail.com"
subject= "Subiect"

contents= ["Hey there here is the content nice !", "text.txt"]  # /url of the file


yag= yagmail.SMTP(user= sender, password=os.environ['PASS'])
yag.send(to= receiver, subject= subject, contents= contents)
print("Email sent!")    
