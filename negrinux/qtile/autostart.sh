#!/bin/sh
~/.config/polybar/launch.sh
yay -Syu
sudo pacman -Syu
picom &
paccache -r
faillock --reset
/usr/share/pipewire

