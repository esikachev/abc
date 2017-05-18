from abc_server import config
from abc_server.flask import abc_server


def main():
    config.check_config()
    abc_server.run(debug=True)


if __name__ == '__main__':
    main()
