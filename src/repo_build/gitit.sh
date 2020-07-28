#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155

# git status ok ...
gsok () { git-achievements status | grep 'nothing to commit'; }

gitit () {
    if ! [ -r "$PWD/.git" ]; then
		warn "Git repo not found in .../${PWD##*/}/.git"
	else
		gsok
		if [ $? -eq 0 ]
		then
			canary "Git status ${GO:-}OK${RESET:-}: $PWD"
		else
			message="${*:-$(cat ~/.dotfiles/.stCommitMsg)}"
			blue "GitIt - add and commit all updates."
			green "  repo: ${PWD##*/}"
			green "  message: "
			green "$message"
			[ -f .pre-commit-config.yaml ] || pre-commit sample-config > .pre-commit-config.yaml
			git-achievements add --all > /dev/null 2>&1
			pre-commit > /dev/null 2>&1
			git-achievements add --all
			pre-commit
			git-achievements commit -m "$message"
			git-achievements push --set-upstream origin "$(git_current_branch)"
			git-achievements status
		fi
	fi
}

if
