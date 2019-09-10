from itertools import combinations

if __name__ == '__main__':
    inputstr = str(input()).split(' ')

    tmp = sorted(inputstr[0])
    val = int(inputstr[1])

    [print (''.join(i)) for x in range(1, val+1) for i in combinations(tmp, x)]
