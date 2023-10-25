import torch
import matplotlib.pyplot as plt

words = open('names.txt', 'r', encoding="utf-8").read().splitlines()

# Table for which char follows which char how often
N = torch.zeros((28,28), dtype=torch.int32)

# List of all possible characters from names
chars = sorted(list(set(''.join(words))))

# Making lookup table - dictionary which character has which index
stoi = {s:i for i,s in enumerate(chars)}
stoi['<S>'] = 26
stoi['<E>'] = 27

# Count which char follows which char how often
for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[(ix1, ix2)] += 1

plt.imshow(N)
plt.show()
