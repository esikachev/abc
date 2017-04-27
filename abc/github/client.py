import github


class Client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None

    def authenticate(self):
        self.user = github.Github(self.username, self.password)

    def _check_repo_exist(self):
        for repo in self.user.get_user().get_repos():
            if 'abc' == repo.name:
                print 'Repo abc exist'
