import threading

from abc_server import auth
from abc_server import config
from abc_server.flask import abc_server
from abc_server.flask import jsonify
from abc_server.git import client as git_client
from abc_server import utils


@abc_server.route('/')
def index():
    return return_200()


@abc_server.route('/init', methods=['POST'])
def init():
    git = get_git_client(init=True)
    git.clone()

    return return_200()


@abc_server.route('/sync', methods=['POST'])
def sync():
    sync_method()

    return return_200()


def get_git_client(init=False):
    user = auth.authenticate()
    if init:
        repo = user.create_repo()
    else:
        repo = user.get_repo()
    return git_client.GitClient(repo_url=repo.ssh_url)


def sync_method():
    configs = config.read_config()
    for item in configs['watch']:
        utils.copy_files(item)
    git = get_git_client()
    git.commit()
    git.push()
    threading.Timer(24 * 3600, sync_method).start()


def return_200(**kwargs):
    return jsonify(status=200, **kwargs)
