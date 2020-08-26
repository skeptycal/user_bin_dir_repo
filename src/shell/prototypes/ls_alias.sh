#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
  # shellcheck shell=bash
  # shellcheck source=/dev/null
  # shellcheck disable=2178,2155

# test aliases in scripts ...


# use aliases from .zshrc (<unsetopt aliases> will turn it back off)
setopt aliases

alias ls1='ls -lrt'
ls1
