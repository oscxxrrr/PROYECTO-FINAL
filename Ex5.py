import requests  # Importa el módulo requests para hacer solicitudes HTTP

def PP_Ex5():
    for i in range(180):  # Itera sobre los primeros 180 Pokémon (de 0 a 179)
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{i}/"  # Construye la URL para cada Pokémon usando su ID
        response = requests.get(pokemon_url)  # Hace una solicitud GET a la URL

        if response.status_code == 200:  # Verifica si la solicitud fue exitosa (código de estado 200)
            data = response.json()  # Convierte la respuesta JSON a un diccionario de Python
            name = data["name"]  # Obtiene el nombre del Pokémon
            move = data["moves"][0]["move"]["name"] if data["moves"] else "ninguno"  # Obtiene el primer movimiento si existe, si no, asigna "ninguno"
            print("El nombre del Pokémon es: {}, y su movimiento es: {}".format(name, move))  # Imprime el nombre y el primer movimiento del Pokémon
        else:
            print("No se encontraron datos.")  # Imprime un mensaje si la solicitud no fue exitosa

    print("Fin del scrapping.")  # Imprime un mensaje indicando que el scraping ha terminado
