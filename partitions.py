import math
import numpy
def pentagonal_number(k):
    return int(k*(3*k-1) / 2)

def compute_partitions(n):
    partitions = [1]
    for i in range(1,n+1):
        partitions.append(0)
        for k in range(1,i+1):
            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                s=math.ceil(((numpy.sign(i-t)+1)/2))
                partitions[i] = partitions[i] + s*((-1)**(k+1))*partitions[s*(i-t)]
    return partitions

print(compute_partitions(5))
