#!/bin/python
# ProjectDesignBuilder.py
# 2022.04.20.21.57

from importlib import import_module as introduce


project_name = "ProjectDesignBuilder"
__version__ = "0.0.2"
__release__ = "0.0.0"


def main():
    """This is the main() entrance for ProjectDesignBuilder.  After entering,
    the assistant() will introduced you to the Administrator."""
    ProjectDesignBuilder = introduce(
        ".Administrator", "Administration.Directors"
    ).assitant()
    return None


# Proceed through the main() entrance.
if __name__ == "__main__":
    main()
