#!/usr/bin/zsh

function warp() {
    eval '$(python ~/.warp/warp.py "$@")'
}
