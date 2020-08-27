#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155

. $(which ssm)

TEMPLATE_DIR=~/Documents/coding/cc_template

trap "exec 1>&6 6>&-" EXIT
exec 6>&1 1>/dev/null

# As of pip 20.2.2
# 	this is a new option to resolve dependencies
# 	--use-feature=2020-resolver
alias pip='pip --use-feature=2020-resolver '

alias piu='pip install -U --use-feature=2020-resolver '

lime "Updating pip ... " >&6
pip install -U pip || ( get-pip; piu pip; )

lime "Installing basic pip tools ... " >&6
piu wheel setuptools twine pytest pylint pre-commit

lime "Installing pip dev tools ... " >&6
piu toml autosysloguru cookiecutter coverage autopep8 dataclasses docutils Pygments pygments-pre-commit pytest-cookies pytest-cov Sphinx sphinx-rtd-theme tox requests

lime "Updating all pythong packages ... " >&6
piu $(pip list | sed 's/  */ /g' | cut -d ' ' -f 1 | tail -n +3; )

# as of 8/23/2020
pip_package_versions=<<-PIPVERSIONS
	Package                       Version
	----------------------------- ---------
	alabaster                     0.7.12
	appdirs                       1.4.4
	arrow                         0.13.2
	astroid                       2.4.2
	attrs                         20.1.0
	autopep8                      1.5.4
	autosysloguru                 0.4.0
	Babel                         2.8.0
	binaryornot                   0.4.4
	black                         19.10b0
	certifi                       2020.6.20
	cfgv                          3.2.0
	chardet                       3.0.4
	click                         7.1.2
	codecov                       2.1.9
	colorama                      0.4.3
	cookiecutter                  1.7.2
	coverage                      5.2.1
	dataclasses                   0.6
	distlib                       0.3.1
	docutils                      0.16
	filelock                      3.0.12
	flake8                        3.8.3
	identify                      1.4.28
	idna                          2.10
	imagesize                     1.2.0
	iniconfig                     1.0.1
	isort                         5.4.2
	Jinja2                        2.11.2
	jinja2-time                   0.2.0
	lazy-object-proxy             1.4.3
	loguru                        0.5.1
	MarkupSafe                    1.1.1
	mccabe                        0.6.1
	more-itertools                8.4.0
	nodeenv                       1.4.0
	packaging                     20.4
	pathspec                      0.8.0
	pathtools                     0.1.2
	pip                           20.2.2
	pluggy                        0.13.1
	poyo                          0.5.0
	pre-commit                    2.7.0
	py                            1.9.0
	pycodestyle                   2.6.0
	pyflakes                      2.2.0
	Pygments                      2.6.1
	pygments-pre-commit           2.2.0
	pylint                        2.6.0
	pyparsing                     2.4.7
	pytest                        5.4.3
	pytest-cookies                0.5.1
	pytest-cov                    2.10.1
	python-dateutil               2.8.1
	python-slugify                4.0.1
	pytz                          2020.1
	PyYAML                        5.3.1
	regex                         2020.7.14
	requests                      2.24.0
	setuptools                    49.6.0
	six                           1.15.0
	snowballstemmer               2.0.0
	Sphinx                        3.2.1
	sphinx-rtd-theme              0.5.0
	sphinxcontrib-applehelp       1.0.2
	sphinxcontrib-devhelp         1.0.2
	sphinxcontrib-htmlhelp        1.0.3
	sphinxcontrib-jsmath          1.0.1
	sphinxcontrib-qthelp          1.0.3
	sphinxcontrib-serializinghtml 1.1.4
	text-unidecode                1.3
	toml                          0.10.1
	tox                           3.19.0
	typed-ast                     1.4.1
	urllib3                       1.25.10
	virtualenv                    20.0.31
	wcwidth                       0.2.5
	wheel                         0.35.1
	wrapt                         1.12.1
PIPVERSIONS
