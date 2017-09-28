import numpy as np

#Each 2 weeks
Taches = ["Aspi", "Panosse", "Grande Toilettes", "Petites Toilettes"]

#Each week
Tache = ["Aspi"]

Colocs = ["Adrien", "Arnaud", "Duc", "Greg"]
Colocs = np.random.permutation(Colocs)
C = Colocs.tolist()
for i in range(3,14):
	print("Semaine ", i, ":")
	if i%2 == 0:
		print(C[0]), " passe l'aspi";

	else:
		print(Taches)
		D = C.copy()
		Aspi = D[0]
		del D[0]
		print(Aspi,np.random.permutation(D))
	
	C.append(C[0])
	del C[0]	





print(Colocs)