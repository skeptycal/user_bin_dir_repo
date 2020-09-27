#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
#? ############################# skeptycal.com
    # Find and delete all broken symbolic links in current directiry
    # use safety feature $1 == '-d' to actually delete them
    # interesting method:
    # https://stackoverflow.com/a/26887762/9878098

# echo "\$1: $1"
case $1 in
    -h|--help)
        echo "Usage: $0 [-d] [PATH]"
        ;;
    -d)
        shift
        echo "Deleting Broken Symlinks ..."
        find -L ${1:-$PWD} -type l -exec rm -- {} +
        ;;
    *)
        echo "Listing Broken Symlinks (use -d to delete links)..."
        find -L ${1:-$PWD} -type l -print 2>&1
        ;;
esac
