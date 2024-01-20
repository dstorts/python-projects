import pandas
import requests
from pokemon import Pokemon
from html.parser import HTMLParser
import pandas as panda

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#
debug = False
expression_list = ['class,infocard-cell-data',
                   'class,ent-name',
                   'class,type-icon type-',
                   'class,cell-total',
                   'class,cell-num']
pokedex = []
pdata = []
read_data = False
type_num = 0
stat_count = 0
data_type = ''

class PokemonDBHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global expression_list, read_data, type_num, data_type, debug
        if debug:
            print("Start tag:", tag)
        for attr in attrs:
            if debug:
                print("     attr:", str(attr))
            for exp in expression_list:
                exp_tuple = exp.split(',')
                attr_type = exp_tuple[0]
                attr_value = exp_tuple[1]
                if attr_type in str(attr) and attr_value in str(attr):
                    if debug:
                        print(f"Found: {attr_value}")
                    read_data = True
                    data_type = attr_value
                    if attr_value == 'type-icon type-':
                        type_num += 1

    def handle_data(self, data):
        global read_data, pdata, pokedex, type_num, data_type, stat_count
        if debug:
            print("Data     :", data)
        if read_data:
            read_data = False
            if debug:
                print(f"We are saving the data:{data}")
            pdata.append(data)

        if data_type == 'cell-num':
            data_type = ''
            if len(pdata) == 10 and type_num == 1 or len(pdata) == 11 and type_num == 2:
                if type_num == 1:
                    pdata.insert(3, 'na')
                #here if we have recorded all datapoints for a single pokemon
                stats = [pdata[0], pdata[1], pdata[2], pdata[3], pdata[4], pdata[5], pdata[6], pdata[7], pdata[8], pdata[9], pdata[10]]
                pokedex.append(stats)
                if debug:
                    print(f"Just saved: {pdata}")
                type_num = 0
                stat_count = 0
                pdata.clear()

parser = PokemonDBHTMLParser()
url = 'https://pokemondb.net/pokedex/all'
r = requests.get(url)

'''
Looking for: [0]dex num, [1]name, [2]type1, [3]type2, [4]stat total, [5]hp, [6]atk, [7]def, [8]spatk, [9]spdef, [10]spe
'''
parser.feed(r.text)
#ndex_puke = open("pokemon_national_dex_puke.txt", "r")
#parser.feed(ndex_puke.read())
print(len(pokedex))

poke_dataframe = panda.DataFrame(pokedex, columns=['dexnum', 'name', 'type1', 'type2', 'total', 'hp', 'atk', 'def', 'spatk', 'spdef', 'speed'])

print(poke_dataframe)

poke_dataframe.to_csv(path_or_buf="national_pokedex.csv", mode='x')