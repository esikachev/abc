import argparse

from abc_server.github import client
from abc_server.flask import abc_server

def get_parser():
    parser = argparse.ArgumentParser(description="Abc server.")
    parser.add_argument('--email', '-e', default=None, nargs='?',
                        help='Specify email for github account')
    parser.add_argument('--password', '-p', default=None, nargs='?',
                        help='Specify password for github account')
    return parser.parse_args()


def main():
    args = get_parser()
    email = args.email
    password = args.password

    user = client.GithubClient(email, password)
    user.authenticate()

    abc_server.run(debug=True) 


if __name__ == '__main__':
    main()
