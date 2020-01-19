import logging
from pathlib import Path

log = logging.getLogger(__name__)

SCRIPT = Path(__file__).resolve()  # Absolute path of this script
SCRIPT_DIR = SCRIPT.parent  # Absolute path of this script's directory


def main(args):
    log.info(f'Script: {SCRIPT}')
    log.info(f'Script directory: {SCRIPT_DIR}')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

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
        'level': getattr(logging, args.log_level.upper()),
        'format': (
            '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
        ),
    }
    logging.basicConfig(**log_params)

    main(args)
