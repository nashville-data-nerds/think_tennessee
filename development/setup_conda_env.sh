#!/bin/bash
conda activate base
conda remove --name think_tn --all
conda env create -f ../environment.yml