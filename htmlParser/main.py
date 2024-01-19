import requests
from pokemon import Pokemon
from html.parser import HTMLParser
from html.entities import name2codepoint

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#
debug = True
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
            if data_type == 'infocard-cell-data':
                pdata.append(f"dexnum:{data}")
            elif data_type == 'ent-name':
                pdata.append(f"name:{data}")
            elif data_type == 'type-icon type-':
                pdata.append(f"type:{data}")
            else:
                #here if a stat
                #there are 7 stat numbers
                #in order, those stats are total, hp, atk, def, spatk, spdef, speed
                stat_count += 1
                if   stat_count == 1:
                    pdata.append(f"total:{data}")
                elif stat_count == 2:
                    pdata.append(f"hp:{data}")
                elif stat_count == 3:
                    pdata.append(f"atk:{data}")
                elif stat_count == 4:
                    pdata.append(f"def:{data}")
                elif stat_count == 5:
                    pdata.append(f"spatk:{data}")
                elif stat_count == 6:
                    pdata.append(f"spdef:{data}")
                else:
                    pdata.append(f"speed:{data}")

        if data_type == 'cell-num':
            data_type = ''
            if len(pdata) == 10 and type_num == 1 or len(pdata) == 11 and type_num == 2:
                #here if we have recorded all datapoints for a single pokemon
                pokedex.append(pdata)
                print(f"Just saved: {pdata}")
                type_num = 0
                stat_count = 0
                pdata.clear()

parser = PokemonDBHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')

#url = 'https://pokemondb.net/pokedex/all'
#r = requests.get(url)

'''
Looking for: [0]dex num, [1]name, [2]type1, [3]type2, [4]stat total, [5]hp, [6]atk, [7]def, [8]spatk, [9]spdef, [10]spe
'''

parser.feed('<table id="pokedex" class="data-table sticky-header block-wide">'
            '<thead>'
            '<tr>'
            '<th class="sorting" data-sort-type="int"><div class="sortwrap">#</div></th> <th class="sorting" data-sort-type="string"><div class="sortwrap">Name</div></th> <th><div class="sortwrap">Type</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Total</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">HP</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Attack</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Defense</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Sp. Atk</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Sp. Def</div></th> <th class="sorting" data-sort-type="int"><div class="sortwrap">Speed</div></th> </tr>'
            '</thead>'
            '<tbody>'
            '<tr>'
            '<td class="cell-num cell-fixed" data-sort-value="557"><span class="infocard-cell-img"><img class="img-fixed icon-pkmn" src="https://img.pokemondb.net/sprites/sword-shield/icon/dwebble.png" alt="Dwebble" width="56" height="42" loading="lazy"></span><span class="infocard-cell-data">0557</span></td> <td class="cell-name"><a class="ent-name" href="/pokedex/dwebble" title="View Pokedex for #0557 Dwebble">Dwebble</a></td><td class="cell-icon"><a class="type-icon type-bug" href="/type/bug">Bug</a><br> <a class="type-icon type-rock" href="/type/rock">Rock</a></td>'
            '<td class="cell-num cell-total">325</td>'
            '<td class="cell-num">50</td>'
            '<td class="cell-num">65</td>'
            '<td class="cell-num">85</td>'
            '<td class="cell-num">35</td>'
            '<td class="cell-num">35</td>'
            '<td class="cell-num">55</td>'
            '</tr>'
            '</tbody>'
            '</table>')

parser.feed('<tr>'
            '<td class="cell-num cell-fixed" data-sort-value="4"><span class="infocard-cell-img"><img class="img-fixed icon-pkmn" src="https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png" alt="Charmander" width="56" height="42" loading="lazy"></span><span class="infocard-cell-data">0004</span></td> <td class="cell-name"><a class="ent-name" href="/pokedex/charmander" title="View Pokedex for #0004 Charmander">Charmander</a></td><td class="cell-icon"><a class="type-icon type-fire" href="/type/fire">Fire</a><br> </td>'
            '<td class="cell-num cell-total">309</td>'
            '<td class="cell-num">39</td>'
            '<td class="cell-num">52</td>'
            '<td class="cell-num">43</td>'
            '<td class="cell-num">60</td>'
            '<td class="cell-num">50</td>'
            '<td class="cell-num">65</td>'
            '</tr>')

#ndex_puke = open("pokemon_national_dex_puke.txt", "r")
#parser.feed(ndex_puke.read())
