import logging

log = logging.getLogger(__name__)


def main(args):
    log.debug('This will only show on debug levels...')
    log.info('Hello world!')
    log.warn('Something went wrong as expected!')
    log.error('Something went wrong!')
    log.critical('Something really went wrong!')

    if args.file:
        fh = open(args.file, 'r')
        print(fh.read())
        fh.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    # Add your own script parameters here...
    parser.add_argument('--file')

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
    # log_params = {
    #     'filename': args.log_file,
    #     'level': getattr(
    #         logging, args.log_level.upper()
    #     ),
    #     'format': (
    #         '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
    #     ),
    # }
    # logging.basicConfig(**log_params)
    logging.basicConfig(
        filename=args.log_file,
        level=getattr(
            logging, args.log_level.upper()
        ),
        format=(
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    )


    # Run
    main(args)
