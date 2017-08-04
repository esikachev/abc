from abc_server import auth
from abc_server.git import client


def get_git_client(init=False):
    user = auth.authenticate()
    if init:
        repo = user.create_repo()
    else:
        repo = user.get_repo()
    return client.GitClient(repo_url=repo.ssh_url)
