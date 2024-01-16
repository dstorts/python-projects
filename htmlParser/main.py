import requests

from html.parser import HTMLParser
from html.entities import name2codepoint

# parser doc - https://docs.python.org/3/library/html.parser.html#examples
# request doc - https://requests.readthedocs.io/en/latest/
#
#

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')

#url = 'https://pokemondb.net/pokedex/all'
#r = requests.get(url)
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
parser.get_starttag_text()