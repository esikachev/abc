from abc_server.flask import abc_server


@abc_server.route('/')
def index():
    return ''
