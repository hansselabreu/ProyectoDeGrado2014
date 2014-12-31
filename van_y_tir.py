def VAN():
	print("INSERTE LA INVERSIÓN K:")
	K = float(input())
	print("INSERTE LA CANTIDAD DE AÑOS: ")
	n = int(input())
	print("INSERTE LA TASA DE INTERÉS: ")
	r = float(input())
	total = 0.0
	for i in range(n):
		print("FLUJO DE CAJA " + str(i + 1) + " : ")
		FC = float(input())
		total += (FC/((1 + (r/100))**(i+1)))
		print(" %f/((%i + %f)^%i) = %f " %(FC, 1, r/100, i+1, total))
		FC = 0.0
	van = total - K
	return van
