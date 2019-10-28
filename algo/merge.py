def sort(seq, left=0, right=None):
    if right is None:
        right = len(seq) - 1
    if left >= right:
        return
    middle = (left + right) // 2
    sort(seq, left, middle)
    sort(seq, middle + 1, right)
    i, end_i, j = left, middle, middle + 1
    while i <= end_i and j <= right:
        if seq[i] < seq[j]:
            i += 1
        else:
            seq.move(j, i)
            i += 1
            end_i += 1
            j += 1
