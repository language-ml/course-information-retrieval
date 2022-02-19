import os
import fnmatch

def recursive_glob(treeroot, pattern):
    '''
    :param treeroot: the path to the directory
    :param pattern:  the pattern of files
    :return:
    '''
    results = []
    for base, dirs, files in os.walk(treeroot):
        good_files = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in good_files)
    return 