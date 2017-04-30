import os
from abc_server import utils


DEFAULT_TEMPLATE = {
    "watch": [
        "",
    ],
}

DEFAULT_CONFIG_PATH = "{}/.abc/abc_config.yaml".format(os.environ.get('HOME'))


def create_default_config():
    utils.write_to_file(DEFAULT_CONFIG_PATH, DEFAULT_TEMPLATE)


def read_config(config_path=DEFAULT_CONFIG_PATH):
    return utils.read_from_file(config_path)
