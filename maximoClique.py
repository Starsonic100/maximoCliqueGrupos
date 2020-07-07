import sys

def inicG(nom,act,n):
	for i in range(int(n)):
		k=0
		actividad=0
		nombre=raw_input("Inserte nombre:") #Insercion de los nombres de personas
		nom[i]=str(nombre)
		while (int(actividad))!=4: #Se eligen tres gustos, pueden ser de 1 a 3
			if k==0:
				actividad=raw_input("Elija gustos de la persona:\n1)Cine\n2)Teatro\n3)Musica\n")
			else:
				actividad=raw_input("Elija gustos de la persona:\n1)Cine\n2)Teatro\n3)Musica\n4)Continuar\n")
			if(int(actividad)<4): #Se cambia una posicion de la lista de la actividad elegida a 1, lo que permite indicar que algun gusto lo tiene cierta persona
				act[int(actividad)-1][i]=1
			k=k+1

def inicRel(rel,act,nom,n):
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
				if (act[0][i]==act[0][int(opcR)]==1 or act[1][i]==act[1][int(opcR)]==1 or act[2][i]==act[2][int(opcR)]==1):
					if  rel[i][int(opcR)]==0:
						rel[i][int(opcR)]=1
						rel[int(opcR)][i]=1
					elif rel[i][int(opcR)]==1:
						print("Ya hay relacion\n")
				elif act[0][i]!=act[0][int(opcR)] or act[1][i]!=act[1][int(opcR)] or act[2][i]!=act[2][int(opcR)]:
					print("No comparten gustos \n")
			elif int(opcR)==i or int(opcR)>int(n) or int(opcR)<0:
				print("Opcion no disponible\n")		
print("Simulacion Clique")
opc=0
P=[]  #Lista con todos los nodos
nom=[] #Lista con todos los nombres
while int(opc)!=4:
	opc=input("Eliga opcion: \n1)Insertar de forma manual \n2)Insertar por medio de archivo \n3)Simulacion grafica \n4)Salir \n")
	if int(opc)==1:
		n=input("Inserte numero de personas:") 
		P=range(int(n))
		nom=range(int(n))
		act=[] #Lista multidimensional de gustos, las listas dentro contienen tres gustos y la informacion de estas determina a que personas corresponden estos
		rel=[] #Matriz de relaciones entre los sujetos.
		for i in range(3):
			act.append([0]*(int(n)))
		for i in range(int(n)):
			rel.append([0]*(int(n)))
		inicG(nom,act,int(n))
		print(P)
		print(nom)
		print (act)
		inicRel(rel,act,nom,int(n))
		print (rel)
	elif int(opc)==4:
		sys.exit()