import sae
import urllib2

def download()
	socket = urllib2.urlopen("http://www.baidu.com")
	content = socket.read()
	socket.close()
	return content

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return download()

application = sae.create_wsgi_app(app)