def sort(seq):
  gap = len(seq)
  swapped = True
  while swapped or gap > 1:
    gap = int(gap / 1.25)
    swapped = False
    for i in range(len(seq) - gap):
      if seq[i] > seq[i + gap]:
        seq.swap(i, i + gap)
        swapped = True
