#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
#? ############################# skeptycal.com

#? update-version.sh - Script to update the version information.
# Reference: https://github.com/libyal/dtformats/blob/master/utils/update_version.sh

BASH_SOURCE="${0}"
SCRIPT_NAME="${BASH_SOURCE##*/}"
SCRIPT_PATH="${BASH_SOURCE%/*}"
REPO_NAME="${SCRIPT_PATH##*/}"

DATE_VERSION=`date +"%Y%m%d"`;
DATE_PKG=`date -R`;
EMAIL_PKG="Michael Treanor <skeptycal@gmail.com>";

sed -i -e "s/^\(__version__ = \)'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'$/\1'${DATE_VERSION}'/" "${REPO_NAME}/__init__.py"
sed -i -e "s/^\(${REPO_NAME} \)([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-1)/\1(${DATE_VERSION}-1)/" "${SCRIPT_PATH}/CHANGELOG.md"
sed -i -e "s/^\( -- ${EMAIL_PKG}  \).*$/\1${DATE_PKG}/" "${SCRIPT_PATH}/CHANGELOG.md"
