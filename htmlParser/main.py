import requests
import pandas as panda
import pokeparser

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#
poke_parser = pokeparser.PokeParser()
master_list = 'https://pokemondb.net/pokedex/all'
barbaracle = 'https://pokemondb.net/pokedex/barbaracle'
r = requests.get(barbaracle)

print(r.text)

'''
poke_parser.feed(r.text)
poke_dataframe = panda.DataFrame(poke_parser.pokedex, columns=['dexnum', 'name', 'type1', 'type2', 'total', 'hp', 'atk', 'def', 'spatk', 'spdef', 'speed'])
poke_dataframe.to_csv(path_or_buf="national_pokedex.csv", mode='x')
'''