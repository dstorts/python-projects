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
attack_element_correct_param = pandas.read_csv('./data/attack_element_correct_param.csv')

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
            return pandas.Series([equip_weapon.reinforceTypeId, equip_weapon.attackElementCorrectId, equip_weapon.attackBasePhysics, equip_weapon.attackBaseMagic, equip_weapon.attackBaseFire, equip_weapon.attackBaseThunder, equip_weapon.attackBaseDark, equip_weapon.correctStrength, equip_weapon.correctAgility, equip_weapon.correctMagic, equip_weapon.correctMagic, equip_weapon.correctFaith],
                                         index=['reinforce_type_id', 'attack_element_correct_id', 'phys_atk', 'magic_atk', 'fire_atk', 'thun_atk', 'holy_atk', 'str_scale', 'dex_scale', 'int_scale', 'fai_scale', 'arc_scale'])

def get_upgrading_multipliers(reinforce_type_id, upgrade_level):
    global reinforce_param_weapon
    uid = reinforce_type_id + upgrade_level
    for index, stats in reinforce_param_weapon.iterrows():
        if stats['ID'] == uid:
            return pandas.Series([stats['Physical Attack'], stats['Magic Attack'], stats['Str Scaling'], stats['Dex Scaling'], stats['Int Scaling'], stats['Fai Scaling'], stats['Arc Scaling']],
                                        index=['phys_atk', 'magic_atk', 'str_scaler', 'dex_scaler', 'int_scaler', 'fai_scaler', 'arc_scaler'])

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
    for index, weapon in calc_correct_graph_ids.iterrows():
        if weapon['Name'] == wep_name:
            #CalcCorrectGraph ID (Physical),CalcCorrectGraph ID (Magic),CalcCorrectGraph ID (Fire),CalcCorrectGraph ID (Lightning),CalcCorrectGraph ID (Holy)
            return pandas.Series([weapon.Physical, weapon.Magic, weapon.Fire, weapon.Lightning, weapon.Holy],
                                 index=['physical', 'magic', 'fire', 'lightning', 'holy'])

def get_calc_correct_params(calc_correct_id):
    global calc_correct_graph
    print(calc_correct_id)
    for index, stats in calc_correct_graph.iterrows():
        if stats['ID'] == calc_correct_id:
            return stats

def get_stat_scale_bools(attack_element_id):
    global attack_element_correct_param
    for index, element_bools in attack_element_correct_param.iterrows():
        if element_bools['ID'] == attack_element_id:
            return element_bools

def helper_get_stat_min(calc_correct_params, player_stat):
    if player_stat < calc_correct_params['Stat1']:
        return calc_correct_params['Stat0']
    elif player_stat < calc_correct_params['Stat2'] and player_stat > calc_correct_params['Stat1']:
        return calc_correct_params['Stat1']
    elif player_stat < calc_correct_params['Stat3'] and player_stat > calc_correct_params['Stat2']:
        return calc_correct_params['Stat2']
    elif player_stat < calc_correct_params['Stat4'] and player_stat > calc_correct_params['Stat3']:
        return calc_correct_params['Stat3']

def helper_get_stat_max(calc_correct_params, player_stat):
    if player_stat < calc_correct_params['Stat1']:
        return calc_correct_params['Stat1']
    elif player_stat < calc_correct_params['Stat2'] and player_stat > calc_correct_params['Stat1']:
        return calc_correct_params['Stat2']
    elif player_stat < calc_correct_params['Stat3'] and player_stat > calc_correct_params['Stat2']:
        return calc_correct_params['Stat3']
    elif player_stat < calc_correct_params['Stat4'] and player_stat > calc_correct_params['Stat3']:
        return calc_correct_params['Stat4']

def helper_get_grow_min(calc_correct_params, player_stat):
    if player_stat < calc_correct_params['Stat1']:
        return calc_correct_params['Grow0']
    elif player_stat < calc_correct_params['Stat2'] and player_stat > calc_correct_params['Stat1']:
        return calc_correct_params['Grow1']
    elif player_stat < calc_correct_params['Stat3'] and player_stat > calc_correct_params['Stat2']:
        return calc_correct_params['Grow2']
    elif player_stat < calc_correct_params['Stat4'] and player_stat > calc_correct_params['Stat3']:
        return calc_correct_params['Grow3']

def helper_get_grow_max(calc_correct_params, player_stat):
    if player_stat < calc_correct_params['Stat1']:
        return calc_correct_params['Grow1']
    elif player_stat < calc_correct_params['Stat2'] and player_stat > calc_correct_params['Stat1']:
        return calc_correct_params['Grow2']
    elif player_stat < calc_correct_params['Stat3'] and player_stat > calc_correct_params['Stat2']:
        return calc_correct_params['Grow3']
    elif player_stat < calc_correct_params['Stat4'] and player_stat > calc_correct_params['Stat3']:
        return calc_correct_params['Grow4']

def helper_get_exp_min(calc_correct_params, player_stat):
    if player_stat < calc_correct_params['Stat1']:
        return calc_correct_params['Exponent0']
    elif player_stat < calc_correct_params['Stat2'] and player_stat > calc_correct_params['Stat1']:
        return calc_correct_params['Exponent1']
    elif player_stat < calc_correct_params['Stat3'] and player_stat > calc_correct_params['Stat2']:
        return calc_correct_params['Exponent2']
    elif player_stat < calc_correct_params['Stat4'] and player_stat > calc_correct_params['Stat3']:
        return calc_correct_params['Exponent3']

def get_phys_atk_calc_correction_factor(calc_correct_params, player_stat):
    stat_min = helper_get_stat_min(calc_correct_params, player_stat)
    stat_max = helper_get_stat_max(calc_correct_params, player_stat)
    exp_min = helper_get_exp_min(calc_correct_params, player_stat)
    grow_min = helper_get_grow_min(calc_correct_params, player_stat)
    grow_max = helper_get_grow_max(calc_correct_params, player_stat)

    ratio = (player_stat - stat_min) / (stat_max - stat_min)
    if exp_min > 0:
        growth = ratio**exp_min
    elif exp_min < 0:
        growth = 1 - ((1 - ratio)**abs(exp_min))
    return (grow_min + ((grow_max - grow_min) * growth)) / 100

weapon_stats = get_weapon_stats(weapon_name, False)
print(f"Attack Element ID: {weapon_stats.attack_element_correct_id}")
weapon_scalers = get_upgrading_multipliers(weapon_stats.reinforce_type_id, weapon_upgrade_lvl)
upgraded_weapon_stats = get_upgraded_weapon_stats(weapon_stats, weapon_scalers)
print(upgraded_weapon_stats)
calc_correct_ids = get_calc_correct_graph_ids(weapon_name)
calc_correct_graph_params = get_calc_correct_params(calc_correct_ids.physical)
#print(calc_correct_graph_params)
stat_scale_bools = get_stat_scale_bools(weapon_stats.attack_element_correct_id)
#print(stat_scale_bools)
str_calc_correction = get_phys_atk_calc_correction_factor(calc_correct_graph_params, player_str)
print(str_calc_correction)