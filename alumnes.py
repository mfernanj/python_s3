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


#MAIN        
num_alumne=0
llista_noms_alumnes=[]
llista_notes_alumnes=[]
menu = True

num_total_alumnes=intro_total_alumnes()

while (num_total_alumnes<1) or (num_total_alumnes>5):
    
    num_total_alumnes=intro_total_alumnes()

for num_alumne in range(num_total_alumnes):
    nom=intro_noms_alumnes(num_alumne,llista_noms_alumnes)
    llista_noms_alumnes.append(nom)
    nota=intro_nota_alumne()
    llista_notes_alumnes.append(nota)

print("MENÚ D\'OPCIONS")
print("1.- Visualitza l'alumne amb major nota")
print("2.- Visualitza l'alumne amb menor nota")
print("3.- Calcular el nº d\'aprovats")
print("4.- Calcular el nº de Notables")
print("5.- Sortir")
triar= int(input("Tria opció (1-5):")  )  
    
while triar not in range(1,5):
   print("Ha de ser una opció vàlida. Torna a provar...")
   triar= int(input("Tria opció (1-5):"))

if triar==1
    [nota,alumne]=visualitza_alumne_major_nota(llista_noms_alumnes,llista_notes_alumnes)
    print(alumne,nota)


    
    
