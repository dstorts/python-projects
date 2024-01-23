'''
equip_param_weapon.csv == base stats of every weapon
    - 'Reinforce Type ID' associates multipliers used to determine growth from weapon upgrades
        - use that id in reinforce_param_weapon.csv to get corresponding multipliers

calc_correct_graph.csv == player stat growth multipliers
    - 'CalcCorrectGraph IDs' from equip_param_weapon.csv used in calc_correct_graph for accurate calculations

attack_element_correct_param.csv == boolean table to show which stats scale which damage types
    - 'AttackElementCorrect ID' from equip_param_weapon.csv associates the scaling booleans to this table


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Use the players Str, Dex, Int stats and the weapon's associated 'CalcCorrectGraph Data' and
plug into the formula below
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    Ratio = (INPUT - StatMIN) / (StatMAX - StatMIN)
    If ExponentMIN > 0
    Growth = Ratio^ExponentMIN
    If ExponentMIN < 0
    Growth = 1 - [(1 - Ratio)^|ExponentMIN|]
    OUTPUT = GrowMIN + [(GrowMAX - GrowMIN) * Growth]
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

'''
import pandas

raw_weapon_data = pandas.read_csv('./data/raw_data.csv')

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
weapon_name = 'Bloodhound Claws'
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

for index, row in raw_weapon_data.iterrows():
    if row['Name'] == weapon_name:
        print(row.Name)
        print(f"Physical Dmg = {row['Physical Attack']}")
