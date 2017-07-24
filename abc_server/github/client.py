import github


class GithubClient(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None

    def authenticate(self):
        user = github.Github(self.username, self.password)
        self.user = user.get_user()

    def get_repo(self):
        for repo in self.user.get_repos():
            if 'abc' == repo.name:
                return repo
        return False

    def create_repo(self):
        repo = self.get_repo()
        if not repo:
            return self.user.create_repo('abc')

        print 'Repo abc exist'
        return repo
