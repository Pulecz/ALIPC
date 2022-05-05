#!/bin/bash
today=$(date +'%Y-%m-%d_')
pacman -Qe > $today.qoutput
