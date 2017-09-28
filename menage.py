import numpy as np

#Each 2 weeks
Taches = ["Aspi", "patte", "Grande Toilettes", "Petites Toilettes"]

#Each week
Tache = ["Aspi"]

Colocs = ["Adrien", "Arnaud", "Duc", "Greg"]
Colocs = np.random.permutation(Colocs)
C = Colocs.tolist()
for i in range(3,14):
	if i%2 == 0:
		print(C[0]);
		C.append(C[0])
		del C[0]
		print(C)
	




print(Colocs)