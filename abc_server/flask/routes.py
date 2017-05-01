from abc_server import auth
from abc_server.flask import abc_server
from abc_server.git import client as git_client


@abc_server.route('/')
def index():
    return ''


@abc_server.route('/init/<data>', methods=['POST'])
def init(data):
    user = auth.authenticate()
    repo = user.create_repo()
    git = git_client.GitClient(repo.ssh_url)
    git.clone()

    return ''
