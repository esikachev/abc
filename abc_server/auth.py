import argparse

from abc_server import config
from abc_server.github import client
from abc_server import utils


def get_parser():
    parser = argparse.ArgumentParser(description="Abc server.")
    parser.add_argument('--email', '-e', default=None, nargs='?',
                        help='Specify email for github account')
    parser.add_argument('--password', '-p', default=None, nargs='?',
                        help='Specify password for github account')
    return parser.parse_args()


def authenticate():
    args = get_parser()
    email = args.email
    password = args.password

    if email and password:
        return _authenticate(email, password)

    abc_account = config.read_config(
        utils.from_home_dir('.abc_account.yaml'))
    return _authenticate(abc_account['github']['email'],
                         abc_account['github']['password'])


def _authenticate(email, password):
    user = client.GithubClient(email, password)
    user.authenticate()
    return user
