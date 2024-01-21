import requests
import pandas as panda
import pokeparser

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#
poke_parser = pokeparser.PokeParser()
url = 'https://pokemondb.net/pokedex/all'
r = requests.get(url)
poke_parser.feed(r.text)
#ndex_puke = open("pokemon_national_dex_puke.txt", "r")
#parser.feed(ndex_puke.read())
print(len(poke_parser.pokedex))

poke_dataframe = panda.DataFrame(poke_parser.pokedex, columns=['dexnum', 'name', 'type1', 'type2', 'total', 'hp', 'atk', 'def', 'spatk', 'spdef', 'speed'])
print(poke_dataframe)

poke_dataframe.to_csv(path_or_buf="national_pokedex.csv", mode='x')