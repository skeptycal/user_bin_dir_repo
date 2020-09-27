#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155

# use aliases from .zshrc
setopt aliases
[[ ${SHELL##*/} == 'zsh' ]] && set -o shwordsplit
. $(which ssm)
. "$HOME/.dotfiles/.oh-my-zsh/lib/git.zsh"

TEMPLATE_DIR=$HOME/local_coding/cc_template

# if [[ $(hash git-achievements >/dev/null 2>&1) -eq 0 ]] && alias git='git-achievements '

# Utilities from .zshrc
diff() { git diff --no-index --color-words "$@"; }
gs() { git status >/dev/null 2>&1; }
gsok() { git status | grep 'nothing to commit'; }
gstdir() { [[ -n $1 ]] && ( cd $1; gs ); }


# trap "exec 1# >&6 6>&-" EXIT
# trap "exec 6>&-" EXIT

# exec 6>&1 # 1>/dev/null

gitit() {

    repo="${PWD##*/}"
    if [ ! -r "$PWD/.git" ]; then
        warn "Git repo not found in .../${repo}/.git"
    else
        if gsok; then
            canary "Git status ${GO:-}OK${RESET:-}: .../${repo}"
        else
            # -m "${*:-'Gitit bot: minor updates and formatting.'}"
            message="${*:-$(cat ~/.dotfiles/.stCommitMsg)}"
            # blue $message
            green "  repo: $repo"
            green "  message:  $message"
            [ -f .pre-commit-config.yaml ] || cp  $TEMPLATE_DIR/.pre-commit-config.yaml .

            pre-commit autoupdate

            # catch any changes from the server
            git stash
            git pull origin master --rebase # >&6
            git stash pop

            # first run through catches errors that are autofixed
            git add --all >/dev/null 2>&1
            pre-commit >/dev/null 2>&1

            # second time shows persistent errors ...
            git add --all
            pre-commit # >&6

            git commit -m "$message" # --gpg-sign=$(which gpg_private)
            git push --set-upstream origin $(git_current_branch) # >&6

            git status # >&6
        fi
    fi
} >/dev/null 2>&1

gitit "$@"
