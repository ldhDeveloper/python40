import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

os.chdir(os.path.dirname(os.path.abspath(__file__)))

send_email = "구글아이디@gmail.com"
send_pwd = "구글앱비밀번호"

recv_email = "네이버아이디@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
첨부파일 메일 테스트 내용 입니다.
감사합니다.
"""

msg = MIMEMultipart()

msg['Subject'] = "메일제목은 여기에 넣습니다."
msg['From'] = send_email
msg['To'] = recv_email

contentPart = MIMEText(text)

msg.attach(contentPart)

etc_file_path = r'첨부파일.txt'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition', 'attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()