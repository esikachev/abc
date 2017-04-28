import argparse
import flask

from abc_server.github import client

abc_server = flask.Flask(__name__)
abc_server.url_map.strict_slashes = False


def get_parser():
    parser = argparse.ArgumentParser(description="Abc server.")
    parser.add_argument('--email', '-e', default=None, nargs='?',
                        help='Specify email for github account')
    parser.add_argument('--password', '-p', default=None, nargs='?',
                        help='Specify password for github account')
    return parser.parse_args()


@abc_server.route('/')
def main():
    args = get_parser()
    email = args.email
    password = args.password

    user = client.GithubClient(email, password)
    user.authenticate()

    user.create_repo()


if __name__ == '__main__':
    main()
