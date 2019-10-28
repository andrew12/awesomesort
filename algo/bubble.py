def sort(seq):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq.swap(i, i + 1)
                swapped = True
