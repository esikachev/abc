import argparse

from abc.github import client


def get_parser():
    parser = argparse.ArgumentParser(description="Abc utility.")
    parser.add_argument('--username', '-u', default=None, nargs='?',
                        help='Specify username')
    parser.add_argument('--password', '-p', default=None, nargs='?',
                        help='Specify password')
    return parser.parse_args()


def main():
    args = get_parser()
    username = args.username
    password = args.password

    user = client.Client(username, password)
    user.authenticate()

    user._check_repo_exist()


if __name__ == '__main__':
    main()
