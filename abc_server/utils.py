import os
import shutil

import yaml


def from_home_dir(path=None):
    if not path:
        return os.environ.get('HOME')
    return "{0}/{1}".format(os.environ.get('HOME'), path)


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        return yaml.load(f)


def copy_files(file_path):
    file_name = os.path.basename(file_path)
    if '~' in file_path:
        shutil.copy2(from_home_dir(file_path[2:]),
                     from_home_dir('.abc/{}'.format(file_name)))
        return
    shutil.copy2(file_path, from_home_dir('.abc/{}'.format(file_name)))
