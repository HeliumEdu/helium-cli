#!/usr/bin/env python

import argparse
import sys

from .actions import utils
from .actions.buildrelease import BuildReleaseAction
from .actions.deploybuild import DeployBuildAction
from .actions.prepcode import PrepCodeAction
from .actions.setbuild import SetBuildAction
from .actions.startservers import StartServersAction
from .actions.update import UpdateAction
from .actions.updateprojects import UpdateProjectsAction

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Helium Edu'
__version__ = utils.VERSION


def main(argv):
    actions = {
        UpdateAction(),
        UpdateProjectsAction(),
        SetBuildAction(),
        StartServersAction(),
        PrepCodeAction(),
        BuildReleaseAction(),
        DeployBuildAction(),
    }

    parser = argparse.ArgumentParser(prog="helium-cli")
    parser.add_argument("--silent", action="store_true", help="Run more quietly, not displaying decorations")
    subparsers = parser.add_subparsers(title="subcommands")

    silent = '--silent' in argv
    if not silent:
        print(utils.get_title())

    for action in actions:
        action.setup(subparsers)

    if len(argv) == 1:
        parser.print_help()

        return

    args = parser.parse_args()

    if not hasattr(args, 'action'):
        parser.print_help()

        return

    args.action.run(args)

    print("")


if __name__ == "__main__":
    main(sys.argv)
