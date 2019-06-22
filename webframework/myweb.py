from wsgiref.simple_server import make_server
import time

def login(req):
    print(req["QUERY_STRING"])
    return b"<h1>welcome</h1>"

def signup(req):
    pass

def foo(req):
    f = open('index.html', 'rb')
    data = f.read()
    return data

def foo2(req ):
    f = open('index2.html', 'rb')
    data = f.read()
    return data

def show_time(req):
    times = time.ctime()
    f = open('index.html', 'rb')
    data = f.read()
    data = data.decode('utf8')
    data = data.replace("{{time}}", str(times))
    return data.encode('utf8')

def router():
    url_patterns = [
        ('/login', login),
        ('/signup', signup),
        ('/foo', foo),
        ('/foo1', foo2),
        ('/time', show_time),
    ]
    return url_patterns

def application(environ, start_response):
    print(environ)
    path = environ['PATH_INFO']
    print(path)
    start_response('200 ok', [('Content-Type', 'text/html')])
    url_patterns = router()
    func = None
    for item in url_patterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'404']


httpd = make_server('', 8080, application)

print("Serving HTTP on port 8080")
httpd.serve_forever()