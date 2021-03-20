#! /bin/bash  
# This command starts jupyter notebook without strict CORS rules 
# This way it can be run from within gitpod env 
jupyter notebook --NotebookApp.allow_origin=\'$(gp url 8888)\'
