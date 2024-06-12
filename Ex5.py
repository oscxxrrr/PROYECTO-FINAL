
import requests

def PP_Ex5():
    for i in range(180):
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
        response = requests.get(pokemon_url)
        
        if response.status_code == 200:
            data = response.json()
            name = data["name"]
            move = data["moves"][0]["move"]["name"] if data["moves"] else "ninguno"
            print("El nombre del Pokémon es: {}, y su movimiento es: {}".format(name,move))
        else:
            print("No se encotraron datos.".format(i))
    print("Fin del scrapping.")
    
