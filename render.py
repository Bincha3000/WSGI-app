import os


def view(template_name):
    template_path = os.path.join('template', template_name)
    if not os.path.exists(template_path):
        return

    with open(template_path) as template_handler:
        content = template_handler.read()
    return content
