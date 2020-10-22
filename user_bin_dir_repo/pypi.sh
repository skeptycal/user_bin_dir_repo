#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155


# ------------------------------- PREPARE
# security
# check .gitignore for tokens, keys, **/*private*, etc

# check if this is a repo (.git and venv present)

# check for venv and run sba


# --------------------- clear old files and caches
# rm -rf **/*/dist/
# rm -rf **/*/__pycache__
# rm -rf **/*/*.egg-info

# rm -rf $REPO/.tox

# ------------------------------- LINTING

# ------------------------------- TESTING

# ------------------------------- PREPARE




# --------------------- bump version
# if '-bump xxx' is passed; xxx is major minor patch


# --------------------- toml file requirements:

# name

# version

# description

# license

# authors

# --------------------- toml file options:

# maintainers

# readme

# homepage

# repository

# documentation

# keywords

# classifiers

# packages

# include and exclude

# dependencies

# dev-dependencies

# scripts

# extras

# plugins

# urls

# Poetry and PEP-517 (build-system)

# ------------------------------- BUILD

python3 -m bdist-wheel sdist
# check for errors
