# Andres Julian
from builtins import print
from time import time
from pip._vendor.distlib.compat import raw_input
import Funciones1
#poblacion
Matriz = []
Fitnes = []
hijos = []
Ganadores = []
nr = int(raw_input('Ingrese el numero de reinas: '))
poblacion = int(raw_input('Ingrese el numero de individuos: '))
re = int(raw_input('Ingrese el numero de Repeticiones: '))
bandera = True
while (bandera):
    proCruse = float(raw_input('Ingrese la probabilidad de cruce (0.65 a 0.85): '))
    if (proCruse >= 0.65):
        if (proCruse <= 0.85):
            print("Probabilidad de cruce establecida: ", proCruse)
            bandera = False
        else:
            print("Inserte una probabilidad válida.")
    else:
        print("Inserte una probabilidad válida.")
bandera=True
while(bandera):
    proMutacion = float(raw_input('Ingrese la probabilidad de mutacion (0.01 a 0.1): '))
    if (proMutacion >= 0.01):
        if(proMutacion <= 0.1):
            print("Probabilidad de cruce establecida: ", proMutacion)
            bandera = False
        else:
            print("Inserte una probabilidad válida.")
    else:
        print("Inserte una probabilidad válida.")
#Crea la poblacion
start_time = time()
for m in range(poblacion):
    Matriz.append(Funciones1.cadenaN(nr + 1))
for i in range(poblacion):
    print ("Individuo", (i+1), ": ", Matriz[i])
for secuencia in range(re):
    print("Repeticion ",secuencia+1)
    #Sacamos Fitness
    Fitnes = (Funciones1.valoracion(Matriz, poblacion, nr))
    #for fit in range (poblacion):
        #print("Fitnes Individuo", (fit+1),":", Fitnes[fit])
    axx = Fitnes.count(0)
    #Obtener ganadores
    Ganadores=(Funciones1.torneo(Fitnes, poblacion))
    #for gan in range (2):
        #print("Padre", (gan+1),":", Ganadores[gan])
    #Probabilidad Cruse
    probCruce = Funciones1.Probabilidad()
    #print("Probabilidad aleatoria: ", probCruce)
    if(probCruce > proCruse):
        hijos = []
        #print("hijos igual a los padres")
        Ganadores[0] = Ganadores[0]-1
        Ganadores[1] = Ganadores[1]-1
        for hj in range(2):
            hij = Matriz[Ganadores[hj]]
            hijos.append(hij)
    else:
        hijos=Funciones1.cruse(Ganadores, Matriz, nr)
    #Fin Probabilidad Cruse
    #for hj in range(2):
        #print("hijo",hj+1,": ",hijos[hj])
    #Probabilidad Mutacion
    probMutacion = Funciones1.Probabilidad()
    #print("Probabilidad aleatoria: ", probMutacion)
    if(probMutacion>proMutacion):
        #print("sin mutacion")
        pass
    else:
        for hm in range(2):
            hijos[hm] = Funciones1.mutacion_un_hijo(hijos[hm], nr)
        #for hj in range(2):
            #print("hijo", hj + 1, ": ", hijos[hj])
    #Fin Probabilidad Mutacion
    FitnesHijos=Funciones1.valoracion(hijos, 2, nr)
    #for fh in range(2):
        #print("hijo Fitnes", fh + 1, ": ", FitnesHijos[fh])
    sel=Funciones1.seleccion(Ganadores, FitnesHijos, Fitnes)
    if(sel[0]==11):
        Matriz[Ganadores[0]]=hijos[0]
    if(sel[1]==22):
        Matriz[Ganadores[1]]=hijos[1]
    #for i in range(poblacion):
        #print ("Individuo", (i+1), ": ", Matriz[i])
elapsed_time = time() - start_time
print("-------------------------Fin-----------------------------------")
Fitnes = (Funciones1.valoracion(Matriz, poblacion, nr))
Ganador=0
libro=open('Ganadores.txt','a')
for i in range(poblacion):
       print ("Individuo", (i+1), ": ", Matriz[i],"Fitnes :",Fitnes[i])
       if(Fitnes[Ganador]>Fitnes[i]):
            Ganador=i
       if (Fitnes[i] == 0):
           parrafo="Inividuo",(i+1),": ",Matriz[i],"Fitness: ",Fitnes[i]
           parrafo=str(parrafo)
           libro.write('\n' + parrafo)
libro.write('\n')
libro.close()

print("Lapso de tiempo: %.10f segundos." % elapsed_time)
print("numero de individuaos con un 0: ",axx)
print("Ganador: ",Ganador+1)
print("Ganador: ",Matriz[Ganador],"Fitness: ",Fitnes[Ganador])