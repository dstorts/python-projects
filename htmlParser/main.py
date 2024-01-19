import requests
from pokemon import Pokemon
from html.parser import HTMLParser
from html.entities import name2codepoint

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#

expression_list = ['class,infocard-cell-data',
                   'class,ent-name',
                   'class,/type/',
                   'class,/type/',
                   'class,cell-total',
                   'class,cell-num',
                   'class,cell-num',
                   'class,cell-num',
                   'class,cell-num',
                   'class,cell-num',
                   'class,cell-num']
pokedex = []
curr_exp_index = 0
read_data = False
is_single_type = False

pdata = []

class PokemonDBHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global expression_list, curr_exp_index, read_data, is_single_type
        print("Start tag:", tag)
        exp = expression_list[curr_exp_index].split(',')
        attr_type = exp[0]
        attr_value = exp[1]
        next_exp = expression_list[curr_exp_index +1].split(',')
        next_attr_value = next_exp[1]

        for attr in attrs:
            print("     attr:", str(attr))
            # if we are looking for type, but currently seeing total
            is_single_type = True if attr_value == 'type-icon type-' and next_attr_value in str(attr) else False
            if attr_type in str(attr) and attr_value in str(attr) and not is_single_type:
                    print(f"Found: {attr_type}")
                    print(f"Found: {attr_value}")
                    read_data = True

    def handle_data(self, data):
        global read_data, is_single_type, curr_exp_index, pdata, pokedex
        print("Data     :", data)
        if read_data and not is_single_type:
            print(f"We are saving the data:{data}")
            pdata.append(data)
            read_data = False
            curr_exp_index += 1
        if read_data and is_single_type:
            #here if we are looking at a single type pokemon and have already read the type
            curr_exp_index += 1 #increment expression index
            pdata.append('na') #handle non-existent 2nd typing
            pdata.append(data) #now add the current data, which is the next data for a dual typed pokemon
            read_data = False
            is_single_type = False
        if len(pdata) == 11:
            #here if we have recorded the 11 sequential datapoints for a single pokemon
            p = Pokemon()
            p.dex = pdata[0]
            p.name = pdata[1]
            p.type1 = pdata[2]
            p.type2 = pdata[3]
            p.total = pdata[4]
            p.hp = pdata[5]
            p.atk = pdata[6]
            p.dfn = pdata[7]
            p.spatk = pdata[8]
            p.spdfn = pdata[9]
            p.spe = pdata[10]
            pokedex.append(p)
            print(f"Just saved: {p.name}")
            curr_exp_index = 0
            pdata.clear()

parser = PokemonDBHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')

#url = 'https://pokemondb.net/pokedex/all'
#r = requests.get(url)

'''
Looking for: [0]dex num, [1]name, [2]type1, [3]type2, [4]stat total, [5]hp, [6]atk, [7]def, [8]spatk, [9]spdef, [10]spe
'''
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
'''
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
#ndex_puke = open("pokemon_national_dex_puke.txt","r")
#parser.feed(ndex_puke.read())

print(f"Name:{pokedex[0].name},dex:{pokedex[0].dex},type1:{pokedex[0].type1},type2:{pokedex[0].type2},total:{pokedex[0].total},hp:{pokedex[0].hp},atk:{pokedex[0].atk},dfn:{pokedex[0].dfn},spatk:{pokedex[0].spatk},spdfn:{pokedex[0].spdfn},speed:{pokedex[0].spe}")
#print(len(pokedex))
