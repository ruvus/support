import urllib2, smtplib
from email.mime.text import MIMEText

recipients = [ 'codline@tatar.ru']

wpad_list = ['10.14.250.55','i.tatar.ru', '10.14.165.49', '10.14.165.50', '10.14.250.40' ]

passw='test2014'

results = []

error = False

for item in wpad_list:
  try:
    url = urllib2.urlopen('http://'+item+'/wpad.dat')
    wpad = url.read()
    if not 'PROXY' in wpad: error=True
    print item+' ' +'OK'
  except:
    print 'Error'
    error = True
    results.append('Error with wpad '+item)
	
if  results:
   server = smtplib.SMTP('mail.tatar.ru')
   server.login('gal.new', passw)
   msg = MIMEText('Subject:Ошибка на wpad\n\n'+'\n'.join(results))
   msg['To'] = ", ".join(recipients)
   msg['From'] = 'Monitoring@tatar.ru'
   server.sendmail('exchange.mailbox1@tatar.ru', recipients, msg.as_string())
   server.quit()
