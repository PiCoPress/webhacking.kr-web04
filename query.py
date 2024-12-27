import pickle

with open('dat.bin', 'rb') as f:
	dat: dict = pickle.load(f)
	N = input('input> ').strip()
	print(dat.get(N))
