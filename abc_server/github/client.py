import github


class GithubClient(object):
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
                return repo
        return False

    def create_repo(self):
        repo = self._check_repo_exist()
        if not repo:
            return self.user.create_repo('abc')

        return repo
