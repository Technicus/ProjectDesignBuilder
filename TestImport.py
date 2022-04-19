#!/bin/python

import importlib

registry = importlib.import_module('Utilities.Data.Program.RegistryManager_01')

print(registry)
dir(registry)

registry.report()
