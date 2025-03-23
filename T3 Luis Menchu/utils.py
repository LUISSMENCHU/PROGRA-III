def load_from_file(bst, path):
    try:
        with open(path, "r") as file:
            for line in file:
                for number in line.strip().split():
                    if number.isdigit():
                        bst.insert(int(number))
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")
