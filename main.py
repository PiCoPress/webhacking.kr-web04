from hashlib import sha1
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map
import pickle
# import multiprocessing

conc = 128
start = 10000
end = 99999 + 1
hash_repeat = 500
target = '' # hashcode
prefix = ''
suffix = 'salt_for_you'
# dat = multiprocessing.Manager().dict()

def multi(s):
	dat = {}
	for i in tqdm(range(start + s, end, conc), position=s):
		k = prefix + str(i) + suffix
		dat[k] = sha1(k.encode()).hexdigest()
		for _ in range(hash_repeat - 1):
			dat[k] = sha1(dat[k].encode()).hexdigest()
		
		dat[dat[k]] = k
		dat.pop(k) # swap
		if len(target) == 0: continue
		if target in dat:
			with open('result.txt', 'w') as f:
				f.write(k)
				f.write('\n')

			print(f'\nprocess {s}: found! - {k}')
			exit()

	return dat

res = {}
ps = process_map(multi, range(conc), max_workers=conc)
for e in ps:
	res |= e


with open('dat.bin', 'wb') as f:
	print(len(res))
	pickle.dump(res, f)

#print()
#N = input('input> ').strip()
# print(dat.get(N))
