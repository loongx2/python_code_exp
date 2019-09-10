from itertools import combinations

from itertools import combinations_with_replacement

if __name__ == '__main__':
    inputstr = str(input()).split(' ')

    tmp = sorted(inputstr[0])
    val = int(inputstr[1])
	
	for i in range(1, val+1):
    	for txt in combinations(tmp, i):
        	print ''.join(txt)

    for txt in combinations_with_replacement(tmp, val):
    print(''.join(txt))
