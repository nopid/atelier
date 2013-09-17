#!/bin/bash
export ATELIER=$HOME/atelier
export PATH=$ATELIER/bin:${PATH}
export LC_ALL=fr_FR.UTF-8
### export http_proxy=http://MONLOGIN:MONMOTDEPASSE@wwwcacheetuauth.univ-orleans.fr:3128
export https_proxy=$http_proxy
cd $ATELIER
gnome-terminal --full-screen --hide-menubar -e "tmux -f etc/tmux.conf"
