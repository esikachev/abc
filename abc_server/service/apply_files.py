from abc_server import config
from abc_server import utils


def apply():
    configs = config.read_config()
    for item in configs['watch']:
        utils.copy_files(item, sync=False)
