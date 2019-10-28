def sort(seq):
  for j in range(len(seq) - 1):
    m = j
    for i in range(j + 1, len(seq)):
      if seq[i] < seq[m]:
        m = i
    if m != j:
      seq.swap(m, j)
