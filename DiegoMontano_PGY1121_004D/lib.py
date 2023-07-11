def validaDatos(mens,inf,sup):
	while True:
		try:
			n=int(input(mens))
			if(n>=inf and n<=sup):
				break
			else:
				print("\n\tDebe estar en el rango "+str(inf)+"-"+str(sup))
		except ValueError:
			print("\n\tDebe ser un numero entero")
	return n
def asignardepartamento(casa):
	cont=1
	for i in range(10):
		for j in range(4):
			casa[i][j]=cont
			cont+=1
def vender(mat,n):
	for i in range(10):
		for j in range(4):
			if(mat[i][j]==n):
				mat[i][j]="X"
def mostrardepartamento(mat):
    for i in range(10):
        for j in range(4):
            x=mat[i][j]
            if((mat[i][j])==1):
                x=str(x)+(" ")
def estaDisponible(mat,n):
	ban=0
	for i in range(10):
		for j in range(4):
			if(mat[i][j]==n):
				ban=1
	return ban


def rutcomprador(mat,n,a,ru):
	for i in range(10):
		for j in range(4):
			if(mat[i][j]==n):
				a.append(n)
				ru.append(validaDatos("\nIngrese su rut: ",1111111,99999999))

def precio(mat,n):
    valor=0
    for i in range (10):
        for j in range(4):
            if (mat[i][j]==n):
                if(j==0):
                    valor=3800
                if(j==1):
                    valor=3000
                if(j==2):
                    valor=2000
                if(j==3):
                    valor=3500
                
    return valor
def totalPagadoA(mat):
    total=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==0):
                    total+=3800
    return total
def totalPagadoB(mat):
    total=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==1):
                    total+=3000
    return total
def totalPagadoC(mat):
    total=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==2):
                    total+=2000
    return total
def totalPagadoD(mat):
    total=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==3):
                    total+=3500
    return total
def cantA(mat):
    cont=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==0):
                    cont+=1
    return cont
def cantB(mat):
    cont=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==1):
                    cont+=1
    return cont
def cantC(mat):
    cont=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==2):
                    cont+=1
    return cont
def cantD(mat):
    cont=0
    for i in range(10):
        for j in range (4):
            if(mat[i][j]=="X"):
                if(j==3):
                    cont+=1
    return cont