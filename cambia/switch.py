import argparse

def main():
	parser = argparse.ArgumentParser(
        description="Implement quick edits to files", prog="Cambia"
    )
    parser.add_argument(
        "-m",
        "--mock",
        nargs=1,
        choices=ARG_CHOICES,
        help="If passed on,"
        " celery will run mock tasks for endpoints provision and kill. The input files"
        " defined in settings for both endpoints will be 'test.sh'",
        default="",
    )
    parser.add_argument(
        "-d",
        "--debug",
        nargs=1,
        choices=ARG_CHOICES,
        help="Quickly change debug in settings",
        default="",
    )
    args = parser.parse_args()