from html.parser import HTMLParser

class PokeParser(HTMLParser):
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
    data_type = ''

    def handle_starttag(self, tag, attrs):
        #global expression_list, read_data, type_num, data_type, debug
        if self.debug:
            print("Start tag:", tag)
        for attr in attrs:
            if self.debug:
                print("     attr:", str(attr))
            for exp in self.expression_list:
                exp_tuple = exp.split(',')
                attr_type = exp_tuple[0]
                attr_value = exp_tuple[1]
                if attr_type in str(attr) and attr_value in str(attr):
                    if self.debug:
                        print(f"Found: {attr_value}")
                    self.read_data = True
                    self.data_type = attr_value
                    if attr_value == 'type-icon type-':
                        self.type_num += 1

    def handle_data(self, data):
        #global read_data, pdata, pokedex, type_num, data_type, stat_count
        if self.debug:
            print("Data     :", data)
        if self.read_data:
            self.read_data = False
            if self.debug:
                print(f"We are saving the data:{data}")
            self.pdata.append(data)

        if self.data_type == 'cell-num':
            self.data_type = ''
            if len(self.pdata) == 10 and self.type_num == 1 or len(self.pdata) == 11 and self.type_num == 2:
                if self.type_num == 1:
                    self.pdata.insert(3, 'na')
                #here if we have recorded all datapoints for a single pokemon
                stats = [self.pdata[0],
                         self.pdata[1],
                         self.pdata[2],
                         self.pdata[3],
                         self.pdata[4],
                         self.pdata[5],
                         self.pdata[6],
                         self.pdata[7],
                         self.pdata[8],
                         self.pdata[9],
                         self.pdata[10]]
                self.pokedex.append(stats)
                if self.debug:
                    print(f"Just saved: {self.pdata}")
                self.type_num = 0
                self.pdata.clear()
