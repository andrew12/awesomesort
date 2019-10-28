def sift(seq, start, count):
    root = start
    while root * 2 + 1 < count:
        child = root * 2 + 1
        if child < (count - 1) and seq[child] < seq[child + 1]:
            child += 1
        if seq[root] < seq[child]:
            seq.swap(root, child)
            root = child
        else:
            return


def sort(seq):
    start = len(seq) // 2 - 1
    finish = len(seq) - 1
    while start >= 0:
        sift(seq, start, len(seq))
        start -= 1
    while finish > 0:
        seq.swap(0, finish)
        sift(seq, 0, finish)
        finish -= 1
