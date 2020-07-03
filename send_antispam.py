import smtplib

from email.mime.text import MIMEText

recipients = ['codline@tatar.ru']

results = 'Ошибка'

antispam_list = { 'kas.citrt.net':'85.233.79.195','kas-2.citrt.net':'85.233.64.94', 'kas-3.citrt.net':'85.233.79.194'}

for item in antispam_list.keys():
     try:
	   server = smtplib.SMTP(antispam_list[item])
	   msg = MIMEText(antispam_list[item])
	   msg['To'] = ", ".join(recipients)
	   msg['From'] = 'Monitoring@tatar.ru'
	   server.sendmail('Monitoring@tatar.ru', recipients, msg.as_string())
	   server.quit()
     except:
	   results.append('Error with '+item)
	   print 'error'
