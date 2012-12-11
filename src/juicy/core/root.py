import os
import shutil

import juicy


def proceed_source_dir(exports, dir_name, file_names):
    rel_dir = os.path.relpath(dir_name, exports['src'])
    dest_dir = os.path.join(exports['dest'], rel_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for file_name in file_names:
        src_path = os.path.join(dir_name, file_name)
        dest_path = os.path.join(dest_dir, file_name)
        if os.path.isfile(src_path) \
                and (exports['overwrite'] or not os.path.exists(dest_path)):
            shutil.copy(src_path, dest_path)


def sync_dirs(src, dest, overwrite=False):
    exports = {
        'src': os.path.abspath(src),
        'dest': os.path.abspath(dest),
        'overwrite': overwrite
    }
    if not os.path.exists(exports['dest']):
        os.makedirs(exports['dest'])
    os.path.walk(src, proceed_source_dir, exports)


def copy_to_home():
    sync_dirs(
        juicy.rootpath,
        juicy.homepath
    )
