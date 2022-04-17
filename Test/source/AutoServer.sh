#!/bin/bash

clear; sphinx-autobuild ./source ./build/html --ignore *.kate-swp --watch './rst' --watch  '../'

