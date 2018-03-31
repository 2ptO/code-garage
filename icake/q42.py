# Write a function that returns a list of all the duplicate files. 
# We'll check them by hand before actually deleting them, since 
# programmatically deleting files is really scary. To help us confirm
# that two files are actually duplicates, return a list of tuples where:

# the first item is the duplicate file
# the second item is the original file
# For example:

#   [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
#  ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
# You can assume each file was only duplicated once.

import os
import hashlib

def _get_files(start_directory):
    for dirpath, _, files in os.walk(start_directory, topdown=True):
        for file in files:
            # Restricting to .py files for simplicity reasons
            if file.endswith(".py"):
                yield os.path.join(dirpath, file)

def _compute_hash(file):
    sha1_hasher = hashlib.sha256()
    with open(file, "r+") as f:
        for line in f:
            sha1_hasher.update(line.encode())
    return sha1_hasher.hexdigest()

def find_duped_files(start_directory):
    files_seen = {}
    duplicates = []
    for cur_file in _get_files(start_directory):
        file_hash = _compute_hash(cur_file)
        if file_hash in files_seen:
            # find the duplicate
            prev_file = files_seen[file_hash]
            prev_file_creation_time = os.path.getctime(prev_file)
            cur_file_creation_time = os.path.getctime(cur_file)
            if prev_file_creation_time > cur_file_creation_time:
                # file1 is latest
                duplicates.append((prev_file, cur_file))
            else:
                duplicates.append((cur_file, prev_file))
        else:
            # Hitting first time. Add it to the seen map
            files_seen[file_hash] = cur_file
    return duplicates

# Came up with the pseudocode in good time, but took
# a while to code because file and hashlib operations
# in python was new to me. Also, encountered some unicode
# conversion issues too. 