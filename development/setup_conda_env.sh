#!/bin/bash
########
# before running script, be in your base env 
# you can activate base with the following command:
# conda activate base
######
conda remove --name think_tn --all
conda env create -f ../environment.yml