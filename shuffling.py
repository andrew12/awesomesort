import vis

import pygame
import random

def shuffle(seq):
  for i in range(len(seq) - 1):
    seq.swap(i, random.randrange(i, len(seq)))

lst = range(512)
pygame.init()
screen = pygame.display.set_mode((512, 512))
seq = vis.Sequence(screen, lst, True, True)
while True:
  shuffle(seq)