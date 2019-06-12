# WSGI-app
OTUS Home Work 3

The Web Server Gateway Interface (WSGI) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language

## Server and Web App
**WSGI has two parts:**
* The server–often high-profile web servers such as Nginx or Apache
* The web app made from a python script

The server executes the web app and sends related information and a callback function to the app. The request is processed on the app side, and a response is sent back to the server utilizing the callback function.

## Requirements:
```
Python>=3.6.5
uWSGI
```
**Install uWSGI:**
```
pip install uwsgi
```

## Start WSGI app, run:
```
uwsgi --http :port --wsgi-file app.py 
```

## Example handler in app
```
@application.add_handler('/wsgi/')
def stuf_handler(env):
    content = view('index.html')
    return {
        "html": content,
        "extra_headers": {'Content-Type': 'text/html'}
    }
```
