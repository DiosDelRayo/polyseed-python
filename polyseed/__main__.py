from . import  generate, recover, pbkdf2, show_polyseed

from argparse import ArgumentParser
from sys import exit

if __name__ == '__main__':
    parser = ArgumentParser(description='Command line tool')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    # Sub-parser for the 'generate' command
    generate_parser = subparsers.add_parser('generate', help='Generate something')
    generate_parser.add_argument('--password', help='Optional password for encryption')

    # Sub-parser for the 'recover' command
    recover_parser = subparsers.add_parser('recover', help='Recover key from polyseed')
    recover_parser.add_argument('phrase', type=str, help='polyseed phrase')
    recover_parser.add_argument('--password', help='Additional password if encrypted')

    # Sub-parser for the 'pbkdf2_sha256' command
    pbkdf2_parser = subparsers.add_parser('pbkdf2_sha256', help='PBKDF2 SHA-256 encryption')
    pbkdf2_parser.add_argument('password', type=str, help='Password')
    pbkdf2_parser.add_argument('salt', type=str, help='Salt')
    pbkdf2_parser.add_argument('rounds', type=int, help='Rounds')
    pbkdf2_parser.add_argument('bytes', type=int, help='Bytes')

    # Sub-parser for the 'test' command
    test_parser = subparsers.add_parser('test', help='Test functionalities')
    test_parser.add_argument('--generate', action='store_true', help='Enable generate')
    test_parser.add_argument('--recover', action='store_true', help='Enable recover')
    test_parser.add_argument('--pbkdf2_sha', action='store_true', help='Enable pbkdf2_sha')

    # Parsing the arguments
    args = parser.parse_args()

    # Handling the parsed commands
    if args.command == 'generate':
        polyseed = generate(args.password)
        show_polyseed(polyseed)
        exit(0)
    elif args.command == 'recover':
        try:
            polyseed = recover(args.phrase, args.password)
            show_polyseed(polyseed)
        except Exception as e:
            print(e)
            exit(1)
        exit(0)
    elif args.command == 'pbkdf2_sha256':
        pbkdf2(args.password, args.salt, args.rounds, args.bytes)
    elif args.command == 'test':
        if args.generate:
            print('Test generate functionality')
        if args.recover:
            print('Test recover functionality')
        if args.pbkdf2_sha:
            print('Test pbkdf2_sha functionality')
