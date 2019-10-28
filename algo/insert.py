def sort(seq):
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] < seq[j]:
                seq.move(i, j)
                break
