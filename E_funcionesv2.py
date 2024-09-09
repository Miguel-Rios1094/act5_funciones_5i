print("funciones creadas por el usuario")
#las funciones 
def MiLista():
    amigos=["Homero","Paty","Lety"]
    for Miguel in amigos:
        print(Miguel)
        
def MiTupla():
    Vecinos = ("Rafael", "Federico", "Cesar")
    print(Vecinos)
    
def MiConjunto():
    Alumno = {"Edad", "Escuela", "Nombre"}
    print(Alumno)

def MiDiccionario():
    Escuela = {
    "Nombre": "Miguel",
    "Especialidad": "Programacion",
    "Grupo": 5,
    "Grado":"I"
    }
    print(Escuela)
    for x in Escuela:
        print(x)
# Llamadas a funciones
print("Mi Lista")
MiLista()
print("Tupla")
MiTupla()
print("Conjunto")
MiConjunto()
print("Diccionario")
MiDiccionario()
