import argparse

from abc_ctl.github import client


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

    user.create_repo()


if __name__ == '__main__':
    main()
