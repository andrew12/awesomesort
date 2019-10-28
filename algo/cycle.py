def sort(seq):
    for i in range(len(seq)):
        if i != seq[i]:
            n = i
            while True:
                tmp = seq[n]
                if n != i:
                    seq[n] = last_value
                else:
                    seq[n] = None
                last_value = tmp
                n = last_value
                if n == i:
                    seq[n] = last_value
                    break
