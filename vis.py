import gevent
import pygame
import sys


class Item:
    def __init__(self, seq, i, v):
        self.seq = seq
        self.i = i
        self.v = v

    def __lt__(self, other):
        self.seq.cmp(self, other)
        return self.v < other.v

    def __le__(self, other):
        self.seq.cmp(self, other)
        return self.v <= other.v

    def __eq__(self, other):
        self.seq.cmp(self, other)
        return self.v == other.v

    def __ne__(self, other):
        self.seq.cmp(self, other)
        return self.v != other.v

    def __gt__(self, other):
        self.seq.cmp(self, other)
        return self.v > other.v

    def __ge__(self, other):
        self.seq.cmp(self, other)
        return self.v >= other.v

    def __repr__(self):
        return "Item(%r, %r)" % (self.i, self.v)


def index(i):
    if isinstance(i, Item):
        return i.i
    else:
        return i


def value(i):
    if isinstance(i, Item):
        return i.v
    else:
        return i


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (64, 64, 64)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Sequence:
    def __init__(self, surface, lst, swaps=True, compares=True):
        self.surface = surface
        self.items = [Item(self, i, v) for i, v in enumerate(lst)]
        self.swaps = swaps
        self.compares = compares
        self.draw()
        self.flip()

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __setitem__(self, i, v):
        item = self.items[i]
        item.v = value(v)
        self.draw()
        if self.swaps:
            self.rect(item, BLUE)
            self.flip()
        self.update()

    def __delitem__(self, i):
        del self.items[i]
        self.update()

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, v):
        v = value(v)
        for i in self.items:
            if i.v == v:
                return True
        return False

    def __repr__(self):
        return "Sequence(%r)" % self.items

    def flip(self):
        gevent.sleep()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        for i, item in enumerate(self.items):
            item.i = i

    def cmp(self, a, b):
        if self.compares:
            self.draw()
            self.rect(a, RED)
            self.rect(b, RED)
            self.flip()

    def swap(self, i, j):
        i, j = index(i), index(j)
        a, b = self.items[i], self.items[j]
        self.draw()
        if self.swaps:
            self.rect(a, BLUE)
            self.rect(b, BLUE)
            self.flip()
        self.items[i], self.items[j] = b, a
        self.update()

    def move(self, i, j):
        i, j = index(i), index(j)
        a, b = self.items[i], self.items[j]
        self.draw()
        if self.swaps:
            self.rect(a, BLUE)
            self.rect(b, BLUE)
            self.flip()
        self.items.insert(j, self.items.pop(i))
        self.update()

    def rect(self, i, color):
        x = i.i * self.surface.get_width() / len(self.items)
        w = self.surface.get_width() / len(self.items)
        # self.surface.fill(WHITE, (x, 0, w, self.surface.get_height()))
        y = (len(self.items) - i.v - 1) * self.surface.get_height() / len(self.items)
        h = self.surface.get_height() - y
        self.surface.fill(color, (x, y, w, h))

    def draw(self):
        self.surface.fill(WHITE)
        for i in self.items:
            if i.i == i.v:
                self.rect(i, GREEN)
            else:
                self.rect(i, BLACK)
