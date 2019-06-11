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

@application.add_handler('/staff/')
def stuf_handler(env):
    content = view('index.html')
    return {
        "html": content,
        "extra_headers": {'Content-Type': 'text/html'}
    }


# application.add_handler("/", index_handler)
# application.add_handler("/contacts/", contact_handler)