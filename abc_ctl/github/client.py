import github


class Client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None

    def authenticate(self):
        user = github.Github(self.username, self.password)
        self.user = user.get_user()

    def _check_repo_exist(self):
        for repo in self.user.get_repos():
            if 'abc' == repo.name:
                print 'Repo abc exist'
                return True

    def create_repo(self):
        if not _check_repo_exist():
            self.user.get_user().create_repo('abc')
