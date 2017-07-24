import argparse

from abc_server.github import client


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

    raise Exception("Credentials is not provided. Run 'abc-server -h'"
                    "for additional information")


def _authenticate(email, password):
    user = client.GithubClient(email, password)
    user.authenticate()
    return user
