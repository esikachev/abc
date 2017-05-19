import os

from abc_server import settings
from abc_server import utils


def check_config():
    conf_dir = os.path.dirname(settings.CONFIG_PATH)
    if not os.path.exists(conf_dir):
        os.mkdir(conf_dir)
    create_config()


def create_config():
    if not os.path.isfile(settings.CONFIG_PATH):
        utils.write_to_file(settings.CONFIG_PATH, settings.DEFAULT_TEMPLATE)


def read_config(config_path=settings.CONFIG_PATH):
    return utils.read_from_file(config_path)
