import argparse
from glob import glob
from os import environ
from os.path import join as pjoin
from shutil import copy
from sys import platform


def main():
    """
    Fix paths to dlls
    """
    p = argparse.ArgumentParser()
    p.add_argument("sitepackagesdir")
    args = p.parse_args()
    # hdf5_path = environ.get("HDF5_DIR")
    hdf5_path = r'C:\Miniconda37-x64\envs\build_env\Library\lib'
    if platform.startswith('win'):
        for f in glob(pjoin(hdf5_path, '*.dll')):
            copy(f, pjoin(args.sitepackagesdir, 'pytables'))


if __name__ == '__main__':
    main()
