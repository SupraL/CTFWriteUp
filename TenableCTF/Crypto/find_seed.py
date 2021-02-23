import random

rands_lst = [
	[22, 67, 142],
	[57, 51, 53],
	[97, 114, 14],
	[16, 94, 107],
	[187, 79, 172],
	[138, 138, 118],
	[32, 41, 8],
	[93, 104, 248],
	[112, 33, 215],
	[22, 163, 8],
	[170, 21, 156],
	[183, 196, 255],
	[62, 160, 64],
	[93, 124, 68],
	[53, 227, 187],
	[234, 44, 74],
	[96, 171, 138],
	[161, 46, 45],
	[186, 114, 154],
	[188, 137, 120],
	[239, 44, 13]]

seeds = [0] * len(rands_lst)

enc_flag = [209, 17, 111, 78, 180, 98, 205, 186, 202, 124, 139, 37, 57, 95, 47, 136, 114, 168, 139, 204, 165]
xor_key = [0] * len(rands_lst)

for i in range(len(rands_lst)):
	for j in range(0, 10000):
		random.seed(j)
		tmp = []
		for k in range(0, 4):
			tmp.append(random.randint(0, 255))

		tmp_key = tmp[i%4]
		del tmp[i%4]
		if tmp == rands_lst[i]:
			seeds[i] = j
			xor_key[i] = tmp_key
			print(seeds)
			print(xor_key)

flag = ""
for c, k in zip(enc_flag, xor_key):
	flag += chr(c ^ k)
print(flag)
