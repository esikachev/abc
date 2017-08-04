import threading

from abc_server import config
from abc_server.service import base
from abc_server import utils


def sync():
    configs = config.read_config()
    for item in configs['watch']:
        utils.copy_files(item)
    git = base.get_git_client()
    git.commit()
    git.push()
    threading.Timer(24 * 3600, sync).start()
