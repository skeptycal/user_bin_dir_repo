# DEV Tools Template Repo

---

[![netlify badge](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys) [![Build Status](https://travis-ci.com/skeptycal/.dotfiles.svg?branch=dev)](https://travis-ci.com/skeptycal/.dotfiles) [![test coverage](https://img.shields.io/badge/test_coverage-100%25-6600CC.svg?logo=Coveralls&color=3F5767)](https://coveralls.io) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3454/badge)](https://bestpractices.coreinfrastructure.org/projects/3454)

[![GitHub Pipenv locked Python version](https://img.shields.io/badge/Python-3.8-yellow?color=3776AB&logo=python&logoColor=yellow)](https://www.python.org/) [![nuxt.js](https://img.shields.io/badge/nuxt.js-2.10.2-35495e?logo=nuxt.js)](https://nuxtjs.org/) [![macOS Version](https://img.shields.io/badge/macOS-10.15%20Catalina-orange?logo=apple)](https://www.apple.com)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=prettier)](https://github.com/prettier/prettier)  [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?label=GitHub&style=social)


## Project template setup for python / javascript setup on a MacBook Pro using Big Sur, Zsh, and Python 3.9

This is my software development setup for a MacBook Pro (mid-2015, 16g ram, 256g SSD). It is the setup I currently use and may change frequently. I am a dabbler in many arts ... and far from expert in most areas. Take it for what it is worth to you.

**Please feel free to offer suggestions and [changes][repo-issues]**. I have been coding for many years, but mostly as a side activity ... as a tool to assist me in other endeavors ... so I have not had the 'hard time' invested of constant coding that many of you have.

> Copyright © 2018-2020 [Michael Treanor](https:/skeptycal.github.com)


[![License](https://img.shields.io/badge/License-MIT-darkblue)][skep-mit]

## Installation

>**Warning:** If you want to use this setup, you should fork this repository, review the code, and make changes to suit your needs. If you aren't sure, don't use it!

>This setup works for me for what I do. Don’t blindly use other people's settings unless you know what is going on. If parts of it do not apply, commment them out or delete them. Misuse could make your system inoperable or at least very annoying to use! Use at your own risk!

---

### Prerequisites

- Xcode
- [VSCode][get-code] IDE (or whatever you prefer)
- [Sarah Drasner][sdras]'s Vue VSCode [Extension Pack][sdras-pack]
- [Don Jayamanne][donj]'s Python [Extension Pack][djay-pack]

These are basic utilities that anyone developing on macOS would probably use or like to learn about. Add these if you don't have them.

```sh
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Use Homebrew to nstall Git and utilities
brew install git hub gpg python poetry pre-commit
```

---

### Repo Setup

I use python quite a bit and throw in a bit of flask and Vue / Nuxt. The python ecosystem has a very fiddly system to isoloate the coding environment for each project. There are many [options available](), but as of now I have found that this works best for my situation:

You can clone this GitHub repository as a starting point:
```sh
git clone https://github.com/skeptycal/user_bin_dir_repo.git && cd user_bin_dir_repo && translate_template.sh
```

This will automate most of the naming and prepping.

---

### Details

I have included a list of steps used to create this environment from scratch so anyone can modify the process to their needs:

1. **Pick a repo name:** This name is used in **MANY LOCATIONS** so choose one
   you like a lot. I do not provide a way to automate changeing the name.
   For this example, I'm using ***MasterBlaster*** for the name.

2. **Location:** Make a directory and change to that directory:

        mkdir MasterBlaster && cd MasterBlaster

3. **Virtual Environment:** create a python environment:

    (I use python3.x (latest) and I have several aliases setup for that)

    ```sh
    # default zsh shell (macOS Catalina and up)
    alias py='python3 -m ' >~/.zshrc
    # default bash shell (before macOS Catalina)
    alias py='python3 -m ' >~/.bashprofile
    # create a new venv
    alias pyv='python3 -m venv venv'
    # activate venv for this repo
    alias sba='source bin/activate'
    # setup dependencies and metadata with poetry
    alias p='poetry '
    # issue pre-commit commands
    alias pc='pre-commit'

    # a longer function to process minor repo changes
    gitit() { ... stuff ... } # see below
    ```
    So to setup my environment, I use:

    ```sh
    # always have source control in place to track changes
    git init

    # if this will be a local template directory:
    git config --global init.templateDir . && pre-commit init-templatedir .

    # time saving helpers ...
    pre-commit autoupdate

    # this is the recommended way for python 3.6+
    # older versions used pyenv or virtualenv
    python3 -m venv venv
    # activate current virtal environment
    source bin/activate # i use zsh ... others may vary here
    ```


    >I always use the same name for my virtual environment so all my scripts work in any location. If you prefer different names for each one, there is an environment variable that is set whenever a virtual environment is active:




It’s probably better to [fork this repository][repo-fork] instead, though.

### Sensible macOS defaults

When setting up a new Mac, you may want to set some sensible macOS defaults:

This repo has installation and defaults for macOS.

---

## Feedback

Suggestions/improvements
[welcome][repo-issues]

---

## Author

[![twitter/skeptycal](https://s.gravatar.com/avatar/b939916e40df04f870b03e0b5cff4807?s=80)](http://twitter.com/skeptycal "Follow @skeptycal on Twitter")

[**Michael Treanor**][me]


## Thanks to…

- [Mathias Bynens][mb]

[repo-issues]: (https://github.com/skeptycal/dotfiles/issues)
[repo-fork]: (https://github.com/skeptycal/dotfiles/fork)



[me]: (https://www.skeptycal.com)
[skep-image]: (https://s.gravatar.com/avatar/b939916e40df04f870b03e0b5cff4807?s=80)
[skep-twitter]: (http://twitter.com/skeptycal)
[skep-mit]: (https://skeptycal.mit-license.org/1976/)


[mb]: (https://mathiasbynens.be/)
[sdras]: (https://sarahdrasnerdesign.com/)
[djay]: (https://github.com/DonJayamanne)


[get-code]: (https://code.visualstudio.com/download)
[brew]: (https://brew.sh/)
[djay-pack]: (https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
[sdras-pack]: (https://marketplace.visualstudio.com/items?itemName=sdras.vue-vscode-extensionpack)
