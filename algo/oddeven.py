def sort(seq, nloops=2):
    swapped = True
    while swapped:
        swapped = False
        for n in range(nloops):
            for i in range(n, len(seq) - 1, nloops):
                if seq[i] > seq[i + 1]:
                    seq.swap(i, i + 1)
                    swapped = True
