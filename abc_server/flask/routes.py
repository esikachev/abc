from abc_server import auth
from abc_server.flask import abc_server
from abc_server.flask import request
from abc_server.git import client as git_client
from abc_server import settings
from abc_server import utils


@abc_server.route('/')
def index():
    return ''


@abc_server.route('/init', methods=['POST'])
def init():
    user = auth.authenticate()
    repo = user.create_repo()
    git = git_client.GitClient(repo.ssh_url)
    git.clone()

    return ''


@abc_server.route('/add', methods=['POST'])
def add():
    with utils.YamlEditor(settings.CONFIG_PATH) as yaml:
        yaml['watch'].extend(request.json["files"])
    return ''
