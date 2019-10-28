def sort(seq):
  begin, end = 0, len(seq) - 1
  swapped = True
  while swapped:
    swapped = False
    for i in range(begin, end):
      if seq[i] > seq[i + 1]:
        seq.swap(i, i + 1)
        swapped = True
    end -= 1
    for i in reversed(range(begin, end)):
      if seq[i] > seq[i + 1]:
        seq.swap(i, i + 1)
        swapped = True
    begin += 1