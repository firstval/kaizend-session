import logging

log = logging.getLogger(__name__)


def main(args):
    log.debug(f'args.file: {args.file}')

    for file in args.file:
        log.debug(f'opening file: {file}')
        with open(file, 'r') as fh:
            print(fh.read())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    # Required `file` parameter
    parser.add_argument(
        'file',
        nargs='+',  # Accept 1 or more files
    )

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

    log_params = {
        'filename': args.log_file,
        'level': getattr(
            logging, args.log_level.upper()
        ),
        'format': (
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    }
    logging.basicConfig(**log_params)

    main(args)
