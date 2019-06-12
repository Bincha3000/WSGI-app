from server import Application
from render import view


application = Application()


@application.add_handler('/')
def index_handler(env):
    return {
        "text": "Hello World",
        "extra_headers": {'Content-Type': 'text/plain'}
    }


@application.add_handler('/contact/')
def contact_handler(env):
    return {
        "json": {"city": "Moscow"},
        "extra_headers": {'Content-Type': 'text/json'}
    }


@application.add_handler('/wsgi/')
def stuf_handler(env):
    content = view('index.html')
    return {
        "html": content,
        "extra_headers": {'Content-Type': 'text/html'}
    }
