import logging

from pathlib import Path

log = logging.getLogger(__name__)


def get_files_in_dir(path, filter=None):
    try:
        # When the path is no longer a
        # directory, print it and exit
        if not path.is_dir():
            # Apply filters or other actions here
            print(path)
            return

        # Call this function for each path
        for p in path.iterdir():
            get_files_in_dir(p)
    except PermissionError:
        # Handle permission error
        log.warn('Permission denied')
        return


def list_files(args):
    log.info(f'Listing files in {args.path}...')

    # Get the absolute path
    list_path = Path(args.path).resolve()

    if not list_path.exists():
        print('Path does not exist')
    elif list_path.is_dir():
        # Path is a directory
        get_files_in_dir(list_path)
    elif list_path.is_file():
        # Path is a single file
        print(list_path)


def list_pattern(args):
    log.info(f'Listing files in {args.path}...')
    list_path = Path().glob(args.path)
    for f in list_path:
        print(f)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Add sub command parsers and parameters here...
    parser_list_files = subparsers.add_parser('list')
    parser_list_files.add_argument(
        'path', help='Path to list files from.')

    parser_list_pattern = subparsers.add_parser(
        'ls_pat'
    )
    parser_list_pattern.add_argument(
        'path', help='Path to list files from.')

    # Set functions to run for each sub parser
    parser_list_files.set_defaults(func=list_files)
    parser_list_pattern.set_defaults(
        func=list_pattern)

    # Default parameters and parameter initialization
    parser.add_argument(
        '-L', '--log-level',
        help='set log level',
        default='INFO',
    )
    parser.add_argument(
        '--log-file',
        help='set log file',
    )
    args = parser.parse_args()

    # Configure logging
    log_params = {
        'filename': args.log_file,
        'level': getattr(logging, args.log_level.upper()),
        'format': (
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    }
    logging.basicConfig(**log_params)

    # Run sub command function
    args.func(args)
