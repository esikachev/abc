import os

import gittle

from abc_server import utils


class GitClient(object):
    def __init__(self, repo_url):
        self.dir_path = utils.from_home_dir(".abc")
        self.repo_url = repo_url
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
        untracked_files = self.repo.untracked_files
        changed_files = self.repo.modified_files

        self.repo.add(untracked_files)
        self.repo.stage(changed_files)

        self.repo.commit(name="ABC Bot", message="Backup")

    def push(self):
        remote_repo = gittle.Gittle(self.dir_path, origin_uri=self.repo_url)

        remote_repo.push()
