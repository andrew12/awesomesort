GAPS = [701, 301, 132, 57, 23, 10, 4, 1]


def sort(seq):
    for h in GAPS:
        for j in range(h, len(seq)):
            i = j - h
            r = seq[j]
            while i >= 0 and r < seq[i]:
                seq.swap(i, i + h)
                i -= h
            seq[i + h] = r
