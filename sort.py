import vis

import pygame
from random import shuffle
from argparse import ArgumentParser
from importlib import import_module

parser = ArgumentParser(description='visualize a sorting algorithm')
parser.add_argument('algo', help='sorting algorithm to show')
parser.add_argument('-z', '--size', help='size of the list', type=int, default=128)
parser.add_argument('-w', '--width', help='window width', type=int, default=512)
parser.add_argument('-e', '--height', help='window height', type=int, default=512)
parser.add_argument('-ns', '--no-swaps', action='store_false', dest='swaps', default=True)
parser.add_argument('-nc', '--no-compares', action='store_false', dest='compares', default=True)
args = parser.parse_args()

lst = list(range(args.size))
shuffle(lst)
#lst.reverse()
pygame.init()
screen = pygame.display.set_mode((args.width, args.height))
seq = vis.Sequence(screen, lst, args.swaps, args.compares)
import_module('algo.{}'.format(args.algo)).sort(seq)
