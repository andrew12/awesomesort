def sort(seq):
  i = 0
  while i < len(seq):
    if i == 0 or seq[i] > seq[i - 1]:
      i += 1
    else:
      seq.swap(i, i - 1)
      i -= 1