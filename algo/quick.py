def sort(seq, left=0, right=None):
    if right is None:
        right = len(seq) - 1
    if left <= right:
        l, r = left, right
        mid = seq[(left + right) // 2]
        while l <= r:
            while l <= right and seq[l] < mid:
                l += 1
            while r > left and seq[r] > mid:
                r -= 1
            if l <= r:
                if l != r:
                    seq.swap(l, r)
                l += 1
                r -= 1
        sort(seq, left, r)
        sort(seq, l, right)
