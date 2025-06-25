import subprocess
import pickle
import os

def unsafe_function(user_input):
    subprocess.call("echo " + user_input, shell=True)

def insecure_pickle_load(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data

def hardcoded_password():
    password = "SuperSecret123"
    print("La contraseña es:", password)

def use_eval(data):
    print(eval(data))

def temp_file_insecure():
    temp_filename = "/tmp/mi_archivo_temp.txt"
    with open(temp_filename, "w") as temp_file:
        temp_file.write("Archivo temporal inseguro")
    print("Archivo temporal creado:", temp_filename)

if __name__ == "__main__":
    user_input = input("Escribe algo para el shell: ")
    unsafe_function(user_input)

    archivo_pickle = input("Nombre del archivo pickle a cargar: ")
    insecure_pickle_load(archivo_pickle)

    hardcoded_password()

    expresion = input("Escribe una expresión para evaluar: ")
    use_eval(expresion)

    temp_file_insecure()
