import argparse

CHOICES = ["restore", "push"]


def main(prog):
    parser = argparse.ArgumentParser(
        description="Implement quick edits to files", prog=prog
    )
    parser.add_argument("command", nargs=1, choices=CHOICES)
    # subparsers = parser.add_subparsers(help='Main command arguments')
    # cmd_push =  subparsers.add_parser('push',
    #     help="Initates the replacement of labeled objects")
    # cmd_restore = subparsers.add_parser('restore',
    #     help="Restores labeled objects to their original values")

    # parser.add_argument(
    #     "-m",
    #     "--mock",
    #     nargs=1,
    #     choices=ARG_CHOICES,
    #     help="If passed on,"
    #     " celery will run mock tasks for endpoints provision and kill. The input files"
    #     " defined in settings for both endpoints will be 'test.sh'",
    #     default="",
    #     )
    # parser.add_argument(
    #     "-d",
    #     "--debug",
    #     nargs=1,
    #     choices=ARG_CHOICES,
    #     help="Quickly change debug in settings",
    #     default="",
    #     )
    return parser


def run_subcommand(command, vars=None):
    if command == "push":
        parser = argparse.ArgumentParser(
            description="Initates the replacement of labeled objects"
        )
    elif command == "restore":
        parser = argparse.ArgumentParser(
            description="Restores labeled objects to their original values"
        )
    else:
        return
    parser.add_argument(
        "target", nargs="*", help="Target or list of targets to be modified"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Indicates [command] will be applied " "to all objects in configuration",
    )

    return parser


def run(prog):
    main_parser = main(prog)
    args, unknown = main_parser.parse_known_args()
    command = args.command[0]
    parser = run_subcommand(command)
    args, unknown = parser.parse_known_args()
    if unknown:
        parser.print_help()
    print(args)
