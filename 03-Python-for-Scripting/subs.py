import logging

log = logging.getLogger(__name__)


def kung(args):
    log.info('Running kung sub command...')
    log.debug(f'Args: {args}')


def foo(args):
    log.info('Running foo sub command...')
    log.debug(f'Args: {args}')


def bacon(args):
    log.info('Running bacon sub command...')
    if args.file:
        fh = open(args.file, 'r')
        print(fh.read())
        fh.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Add sub command parsers and parameters here...
    parser_kung = subparsers.add_parser('kung')
    parser_kung.add_argument('a', help='Kung param')

    parser_foo = subparsers.add_parser('foo')
    parser_foo.add_argument('a', help='Foo param')

    parser_bacon = subparsers.add_parser('bacon')
    parser_bacon.add_argument(
        '--file', help='File to read')

    # Set functions to run for each sub parser
    parser_kung.set_defaults(func=kung)
    parser_foo.set_defaults(func=foo)
    parser_bacon.set_defaults(func=bacon)

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
