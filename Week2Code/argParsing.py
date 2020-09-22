'''
Auhor: George Zhou
Date: September 22, 2020

To demonstrate argument parsing
'''

import argparse
DEFAULT_PORT = 12345
DEFAULT_PROTO = 'tcp'

parser = argparse.ArgumentParser()
parser.add_argument(
    '-proto',
    required=True,
    choices=['http','tcp','udp'],
    help='choices may be http, tcp or udp'
)

parser.add_argument(
    '-port',
    default=DEFAULT_PORT,
    type=int,
    help=f'port to use for the communication, '
)

args = parser.parse_args()

print(args)