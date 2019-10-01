#FUNCIONS
def intro_total_alumnes():

    num_total_alumnes=input("Nombre d\'alumnes de la classe:")
    return int(num_total_alumnes)

def intro_noms_alumnes(num_alumne,llista_noms_alumnes):
    
    print("ALUMNE nº",num_alumne+1)
    nom=input("Introdueix el nom:")
    
    while nom in llista_noms_alumnes:
        print("Aquest alumne ja està a llista")
        nom=input("Introdueix el nom:")
    return nom
    
def intro_nota_alumne():

    nota= float(input("Introdueix nota alumne (0-10):"))
    while (nota<0) or (nota>10):
        print("Error. Cal que siga un valor entre 0 i 10.")
        nota= float(input("Introdueix nota alumne (0-10):"))
    return nota    

def mostra_menu():
    print("")
    print("MENÚ D\'OPCIONS")
    print("1.- Visualitza l'alumne amb major nota")
    print("2.- Visualitza l'alumne amb menor nota")
    print("3.- Calcular el nº d\'aprovats")
    print("4.- Calcular el nº de Notables")
    print("5.- Sortir")
    triar= int(input("Tria opció (1-5):"))
    while triar not in range(1,6):
       print("Ha de ser una opció vàlida. Torna a provar...")
       triar= int(input("Tria opció (1-5):"))

    print("")

    return triar

def visualitza_alumne_major_nota(llista_noms_alumnes,llista_notes_alumnes):
    nota=max(llista_notes_alumnes)
    for index in range(len(llista_notes_alumnes)):
        if llista_notes_alumnes[index]==nota:
            alumne=llista_noms_alumnes[index]

    return(alumne,nota)

def visualitza_alumne_menor_nota(llista_noms_alumnes,llista_notes_alumnes):
    nota=min(llista_notes_alumnes)
    for index in range(len(llista_notes_alumnes)):
        if llista_notes_alumnes[index]==nota:
            alumne=llista_noms_alumnes[index]
       # break;

    return(alumne,nota)


def calcula_num_aprovats(llista_noms_alumnes,llista_notes_alumnes):

    num_aprovats=0
    llista_aprovats=[]
    for index in range(len(llista_notes_alumnes)):
        if llista_notes_alumnes[index]>=5.0:
            alumne=llista_noms_alumnes[index]
            llista_aprovats.append(alumne)
            num_aprovats+=1

    return llista_aprovats

def calcula_num_notables(llista_noms_alumnes,llista_notes_alumnes):

    num_notables=0
    llista_notables=[]
    for index in range(len(llista_notes_alumnes)):
        if llista_notes_alumnes[index]>=7.0 and llista_notes_alumnes[index]<9.0:
            alumne=llista_noms_alumnes[index]
            llista_notables.append(alumne)
            num_notables+=1

    return llista_notables

#MAIN        
num_alumne=0
llista_noms_alumnes=[]
llista_notes_alumnes=[]
menu = True
triar = 0

num_total_alumnes=intro_total_alumnes()

while (num_total_alumnes<1) or (num_total_alumnes>5):
    
    num_total_alumnes=intro_total_alumnes()

for num_alumne in range(num_total_alumnes):
    nom=intro_noms_alumnes(num_alumne,llista_noms_alumnes)
    llista_noms_alumnes.append(nom)
    nota=intro_nota_alumne()
    llista_notes_alumnes.append(nota)

triar=mostra_menu()
    
while menu:
    if triar==1:
        alumne_major_nota=visualitza_alumne_major_nota(llista_noms_alumnes,llista_notes_alumnes)
        print("L\'alumne de major nota és:",end=" ")
        for i in range(len(alumne_major_nota)):
            print(alumne_major_nota[i],end=" ")
        #triar=mostra_menu()
        triar= int(input("Tria opció (1-5):"))
         
    elif triar==2:
        alumne_menor_nota=visualitza_alumne_menor_nota(llista_noms_alumnes,llista_notes_alumnes)
        print("L\'alumne de menor nota és:",end=" ")
        for i in range(len(alumne_menor_nota)):
            print(alumne_menor_nota[i],end=" ")    
        triar=mostra_menu()

    elif triar==3:
        llista_aprovats=calcula_num_aprovats(llista_noms_alumnes,llista_notes_alumnes)
        num_aprovats=len(llista_aprovats)
        print("Han aprovat",num_aprovats)
        print(llista_aprovats)
        triar=mostra_menu()

    elif triar==4:
        llista_notables=calcula_num_notables(llista_noms_alumnes,llista_notes_alumnes)
        num_notables=len(llista_notables)
        print("Hi ha",num_notables,"notables")
        print(llista_notables)
        triar=mostra_menu()

    else:
        menu = False


    
