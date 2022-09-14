import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

os.chdir(os.path.dirname(os.path.abspath(__file__)))

send_email = "네이버@naver.com"
send_pwd = "네이버비밀번호"

recv_email = "구글@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "html로 보내는 메일입니다."
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #339966;">글자의 색상을 지정하거나</span></p>
<h1>크기를 조정할수있습니다.</h1>
<p>표도 만들수있습니다.</p>
<table style="height: 82px;" width="305">
<tbody>
<tr>
<td style="width: 94.3281px;">1</td>
<td style="width: 94.3281px;">2</td>
<td style="width: 94.3438px;">3</td>
</tr>
<tr>
<td style="width: 94.3281px;">표를</td>
<td style="width: 94.3281px;">만들수</td>
<td style="width: 94.3438px;">있습니다.</td>
</tr>
<tr>
<td style="width: 94.3281px;">4</td>
<td style="width: 94.3281px;">5</td>
<td style="width: 94.3438px;">6</td>
</tr>
</tbody>
</table>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()