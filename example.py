#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import interactive_argparse

parser = argparse.ArgumentParser(description='Example parser')

parser.add_argument('-a1', '--argument_one', type=str, required=True, help='A random string')
parser.add_argument('-a2', '--argument_two', type=str, choices=['legal1', 'legal2'], help='One of these values')
parser.add_argument('-a3', '--argument_three', type=int, help='Some integer')
parser.add_argument('-a4', type=int, help='Some other integer')

if __name__ == '__main__':
    args = interactive_argparse.interactive_argument_resolver(parser) if len(sys.argv) == 1 else parser.parse_args()
    print('Resulting arguments namespace: {}'.format(args))

