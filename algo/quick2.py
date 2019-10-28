def partition(seq, left, right):
    pivot = left
    v = seq[pivot]
    right -= 1
    seq.swap(pivot, right)
    for i in range(left, right):
        if seq[i] <= v:
            seq.swap(i, left)
            left += 1
    seq.swap(left, right)
    return left


def sort(seq, left=0, right=None):
    if right is None:
        right = len(seq)
    if left < right:
        pivot = partition(seq, left, right)
        sort(seq, left, pivot)
        sort(seq, pivot + 1, right)
