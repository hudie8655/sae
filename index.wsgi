import sae
import urllib2
from sae.mail import send_mail



def download():
	socket = urllib2.urlopen("http://paper.people.com.cn/rmrb/html/2016-08/18/nbs.D110000renmrb_01.htm")
	content = socket.read()
	socket.close()
	return content

def sendmail(content):
	send_mail("rmrb321@yeah.net", "newest", content,("smtp.sina.cn", 25, "rmrb321@sina.cn", "123rmrb", False))

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    body = download()
    sendmail(body)
    return "success"

application = sae.create_wsgi_app(app)