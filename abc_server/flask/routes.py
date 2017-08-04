from abc_server.flask import abc_server
from abc_server.flask import jsonify
from abc_server.service import apply_files
from abc_server.service import base
from abc_server.service import sync_files


@abc_server.route('/')
def index():
    return return_200()


@abc_server.route('/init', methods=['POST'])
def init():
    git = base.get_git_client(init=True)
    git.clone()

    return return_200()


@abc_server.route('/sync', methods=['POST'])
def sync():
    sync_files.sync()

    return return_200()


@abc_server.route('/apply', methods=['POST'])
def apply():
    apply_files.apply()

    return return_200()


def return_200(**kwargs):
    return jsonify(status=200, **kwargs)
