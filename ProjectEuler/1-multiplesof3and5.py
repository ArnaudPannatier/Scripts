import numpy as np

bond = 1000
sum = 0

for i in range(bond):
	if i%3 == 0 or i%5 == 0:
		
		sum += i

print(sum)

## Analytical way of doing it 

mult = [3,5,-15]

sum2 = 0;

for n in mult:
	partialsum = 0
	for i in range(int(np.floor(bond/np.abs(n)))+1):
		partialsum += i
	partialsum *= n
	sum2 += partialsum

print(sum2-1000)

