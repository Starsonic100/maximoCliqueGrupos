import sys
import random
maxClique=[]
def inicP(nom,n):
	for i in range(int(n)):
		k=0
		actividad=0
		nombre=raw_input("Inserte nombre:") #Insercion de los nombres de personas
		nom[i]=str(nombre)


def inicGraf(graf,nom,n,vec):
	for i in range(int(n)):
		opcR=-1
		while int(opcR)!=int(n):
			opcR=-1
			ins="Elija con quien tiene relacion "
			ins=ins+str(nom[i])+"\n"
			if i==0:
				for j in range (1,int(n)):
					ins=ins+str(j)+"-"+str(nom[j])+"\n"
			elif i>0 and i<int(n-1):
				for j in range (i):
					ins=ins+str(j)+"-"+str(nom[j])+"\n"
				for k in range (i+1,int(n)):
					ins=ins+str(k)+"-"+str(nom[k])+"\n"
			elif i==int(n-1):
				j=1
				for j in range (int(n-1)):
					ins=ins+str(j)+"-"+str(nom[j])+"\n"
			ins=ins+str(n)+"-Continuar\n"
			opcR=input(ins)
			if int(opcR)!=int(n) and int(opcR)!=i:
				if  graf[i][int(opcR)]==0:
					graf[i][int(opcR)]=1
					graf[int(opcR)][i]=1
					vec[i]=vec[i]+1
					vec[int(opcR)]=vec[int(opcR)]+1
				elif graf[i][int(opcR)]==1:
						print("Ya hay relacion\n")
			elif int(opcR)==i or int(opcR)>int(n) or int(opcR)<0:
				print("Opcion no disponible\n")	
def archivos(arch):
	file=""
	archivo=raw_input("Inserte nombre de archivo con datos de grafo:\n")
	file=str(archivo)+".txt"
	f=open(file,"r")
	f1=f.readlines()
	for x in f1:
		arch.append(x)

def N(v,graf):
	c=0
	inter=[]
	for i in graf[v]:
		if i is 1:
			inter.append(c)
		c=c+1
	return inter
def bronkerbosch(R,P,X,graf):
	if len(P)==0 and len(X)==0:
		maxClique.append(R)
	else:
		vp=random.choice(P+X)#El pivote se obtiene de forma aleatoria
		for v in P[:]:
			if graf[vp][v]==0: #Comprueba si v no es vecino de vp
				Rnew=R+[v]
				Pnew=[value for value in P if value in N(v,graf)]
				Xnew=[value for value in X if value in N(v,graf)]
				bronkerbosch(Rnew,Pnew,Xnew,graf)
				P.remove(v)
				X.append(v)

def obtMaxClique(maxClique):
	max=0
	for i in range(len(maxClique)):
		if len(maxClique[i])>=len(maxClique[max]):
			max=i
	return max

print("Simulacion Clique")
opc=0
P=[]  #Lista con todos los nodos
nom=[] #Lista con todos los nombres
R=[]
X=[]
graf=[] #Matriz de grafaciones entre los sujetos.
while int(opc)!=4:
	opc=input("Eliga opcion: \n1)Insertar de forma manual \n2)Insertar por medio de archivo \n3)Simulacion grafica \n4)Salir \n")
	if int(opc)==1:
		n=input("Inserte numero de personas:") 
		P=range(int(n))
		nom=range(int(n))
		vec=range(int(n))
		for i in range(int(n)):
			graf.append([0]*(int(n)))
		for i in range(int(n)):
			vec[i]=0
		inicP(nom,int(n))
		#print(P)
		#print(nom)
		#print (act)
		inicGraf(graf,nom,int(n),vec)
		#print (graf)
	elif int(opc)==2:
		arch=[]
		archivos(arch)
		P=eval(arch[0])
		nom=eval(arch[1])
		graf=eval(arch[2])
	elif int(opc)==3:
		bronkerbosch(R,P,X,graf)
		print("Conjuntos de cliques: "+str(maxClique))
		max=obtMaxClique(maxClique)
		print("Clique Maximo: "+str((maxClique[max]))) #Obtencion del maximo Clique
	elif int(opc)==4:
		sys.exit()
