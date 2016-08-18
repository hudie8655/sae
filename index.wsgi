import sae
import urllib2
from sae.mail import send_mail



def download():
	socket = urllib2.urlopen("http://www.baidu.com")
	content = socket.read()
	socket.close()
	return content

def sendmail(content):
	send_mail("katherine@vampire.com", "rmrb", content,("smtp.sina.cn", 25, "rmrb321@sina.cn", "123rmrb", False))

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
	body = download()
	sendmail(body)
    return "success"

application = sae.create_wsgi_app(app)