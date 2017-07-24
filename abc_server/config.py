from abc_server import settings
from abc_server import utils


def read_config(config_path=settings.CONFIG_PATH):
    return utils.read_from_file(config_path)
