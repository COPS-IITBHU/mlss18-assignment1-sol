import pickle
import numpy as np

with open('check.pickle', 'rb') as p:
	a = pickle.load(p)

with open('submission.pickle', 'rb') as p:
	b = pickle.load(p)

print(np.array_equal(a, b))