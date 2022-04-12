#!/bin/python

import subprocess
import sys


def run_publisher():
    subprocess.run(
        args = [
        'clear; \
        ./Administration/Documentum/Publisher/Author/Publisher.py'
        ], shell=True
    )


def run_git(commit_message = None):
    if commit_message is None:
        commit_message = []
    else:
        commit_message = commit_message
    subprocess_test = subprocess.run(
        args = [
        'clear; \
        git status; git add .; git status; git commit -m \"' + commit_message + '\"; git status; \
        git push; git status'
        ], shell=True
    )


def main():
    #run_publisher()
    commit_message = input("\nCommit message: ")
    #print(commit_message)
    run_git(commit_message)
    print()

if __name__ == "__main__":
    main()
