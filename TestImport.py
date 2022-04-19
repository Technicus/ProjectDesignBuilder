#!/bin/python

import importlib

piss = importlib.import_module('Utilities.Data.Program.Pisser')
registry = importlib.import_module('Utilities.Data.Program.RegistryManager')

print(piss)
dir(piss)

print(registry)
dir(registry)

piss.pissAss()
