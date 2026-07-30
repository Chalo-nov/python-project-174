import json


def generate_diff(file_path1, file_path2):
    # Cargar el contenido de los dos archivos JSON
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    # Por ahora, podemos retornar o imprimir ambos diccionarios
    return data1, data2