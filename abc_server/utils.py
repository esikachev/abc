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


def copy_files(file_path, sync=True):
    file_name = os.path.basename(file_path)
    copy_from = file_path
    if '~' in file_path:
        copy_from = from_home_dir(file_path[2:])
    copy_to = from_home_dir('.abc/{}'.format(file_name))

    if not sync:
        copy_to, copy_from = copy_from, copy_to

    shutil.copy2(copy_from, copy_to)
