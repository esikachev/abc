import os

import gittle

from abc_server import config
from abc_server import utils


class GitClient(object):
    def __init__(self, repo_url=None):
        self.dir_path = utils.from_home_dir(".abc")
        self.repo_url = repo_url
        if repo_url is None:
            configs = config.read_config()
            self.repo_url = configs['repo_url']
        self.repo = None

    def _check_is_local_repo_exist(self):
        return os.path.isdir(self.dir_path)

    def clone(self):
        if not self._check_is_local_repo_exist():
            self.repo = gittle.Gittle.clone(self.repo_url, self.dir_path)
            return self.repo

    def init(self):
        if self._check_is_local_repo_exist():
            self.repo = gittle.Gittle(self.dir_path)
            return self.repo

        self.clone()

    def commit(self):
        gittle.Gittle(self.dir_path)
        self.repo = gittle.Gittle(self.dir_path, origin_uri=self.repo_url)
        untracked_files = self.repo.untracked_files
        changed_files = self.repo.modified_files

        if untracked_files or changed_files:
            self.repo.add(untracked_files)
            self.repo.stage(changed_files)

            self.repo.commit(name="ABC Bot", message="Backup")
            return

        print "Nothing to commit, working tree clean :)"

    def push(self):
        remote_repo = gittle.Gittle(self.dir_path, origin_uri=self.repo_url)

        remote_repo.push()
