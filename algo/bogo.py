import random


def is_sorted(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            return False
    return True


# Fisher-Yates shuffle
def shuffle(seq):
    for i in range(len(seq) - 1, 0, -1):
        seq.swap(i, random.randrange(i))


def sort(seq):
    while not is_sorted(seq):
        shuffle(seq)
