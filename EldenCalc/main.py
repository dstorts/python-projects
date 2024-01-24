'''
equip_param_weapon.csv == base stats of every weapon
    - 'Reinforce Type ID' associates multipliers used to determine growth from weapon upgrades
        - use that id in reinforce_param_weapon.csv to get corresponding multipliers

calc_correct_graph.csv == player stat growth multipliers
    - 'CalcCorrectGraph IDs' from calc_correct_graph_id.csv used in calc_correct_graph for accurate calculations

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
equip_param_weapon = pandas.read_csv('./data/equip_param_weapon.csv')
reinforce_param_weapon = pandas.read_csv('./data/reinforce_param_weapon.csv')
calc_correct_graph_ids = pandas.read_csv('./data/calc_correct_graph_id.csv')
calc_correct_graph = pandas.read_csv('./data/calc_correct_graph.csv')

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
weapon_name = 'Cold Dagger'
weapon_upgrade_lvl = 5
player_str = 14
player_dex = 14
player_int = 40
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

def get_weapon_stats(wep_name, print_table):
    global equip_param_weapon
    for index, equip_weapon in equip_param_weapon.iterrows():
        if equip_weapon['Name'] == wep_name:
            if print_table:
                print( "Phys. Atk | Magic Atk | Fire Attack | Lightning Atk | Holy Atk")
                print(f" {equip_weapon.attackBasePhysics}         {equip_weapon.attackBaseMagic}          {equip_weapon.attackBaseFire}             {equip_weapon.attackBaseThunder}               {equip_weapon.attackBaseDark}")
                print( "Str Scale | Dex Scale | Int Scale   | Fai Scale     | Arc Scaling")
                print(f" {equip_weapon.correctStrength}         {equip_weapon.correctAgility}          {equip_weapon.correctMagic}            {equip_weapon.correctMagic}              {equip_weapon.correctFaith}")
            weapon_stats = pandas.Series([equip_weapon.reinforceTypeId, equip_weapon.attackBasePhysics, equip_weapon.attackBaseMagic, equip_weapon.attackBaseFire, equip_weapon.attackBaseThunder, equip_weapon.attackBaseDark, equip_weapon.correctStrength, equip_weapon.correctAgility, equip_weapon.correctMagic, equip_weapon.correctMagic, equip_weapon.correctFaith],
                                         index=['reinforce_type_id', 'phys_atk', 'magic_atk', 'fire_atk', 'thun_atk', 'holy_atk', 'str_scale', 'dex_scale', 'int_scale', 'fai_scale', 'arc_scale'])
            return weapon_stats

def get_upgrading_multipliers(reinforce_type_id, upgrade_level):
    global reinforce_param_weapon
    uid = reinforce_type_id + upgrade_level
    for index, stats in reinforce_param_weapon.iterrows():
        if stats['ID'] == uid:
            upgrade_multipliers = pandas.Series([stats['Physical Attack'], stats['Magic Attack'], stats['Str Scaling'], stats['Dex Scaling'], stats['Int Scaling'], stats['Fai Scaling'], stats['Arc Scaling']],
                                                index=['phys_atk', 'magic_atk', 'str_scaler', 'dex_scaler', 'int_scaler', 'fai_scaler', 'arc_scaler'])
            return upgrade_multipliers

def get_upgraded_weapon_stats(base_stats, attr_scalers):
    up_phys_atk   = base_stats.phys_atk * attr_scalers.phys_atk
    up_maj_atk    = base_stats.magic_atk * attr_scalers.magic_atk
    up_str_scaler = base_stats.str_scale * attr_scalers.str_scaler
    up_dex_scaler = base_stats.dex_scale * attr_scalers.dex_scaler
    up_int_scaler = base_stats.int_scale * attr_scalers.int_scaler
    return pandas.Series([up_phys_atk, up_maj_atk, up_str_scaler, up_dex_scaler, up_int_scaler],
                         index=['phys_atk', 'magic_atk', 'str_scale', 'dex_scale', 'int_scale'])

def get_calc_correct_graph_ids(wep_name):
    global calc_correct_graph_ids
    for index, weapon in calc_correct_graph_ids:
        if weapon['Name'] == wep_name:
            #CalcCorrectGraph ID (Physical),CalcCorrectGraph ID (Magic),CalcCorrectGraph ID (Fire),CalcCorrectGraph ID (Lightning),CalcCorrectGraph ID (Holy)
            return pandas.Series([weapon.Physical, weapon.Magic, weapon.Fire, weapon.Lightning, weapon.Holy],
                                 index=['physical', 'magic', 'fire', 'lightning', 'holy'])

weapon_stats = get_weapon_stats(weapon_name, False)
weapon_scalers = get_upgrading_multipliers(weapon_stats.reinforce_type_id, weapon_upgrade_lvl)
upgraded_weapon_stats = get_upgraded_weapon_stats(weapon_stats, weapon_scalers)
calc_correct_ids = get_calc_correct_graph_ids(weapon_name)