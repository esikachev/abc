from abc_server import utils


DEFAULT_TEMPLATE = {
    "repo_url": '',
    "watch": [],
}

CONFIG_PATH = utils.from_home_dir(".abc/abc_config.yaml")
