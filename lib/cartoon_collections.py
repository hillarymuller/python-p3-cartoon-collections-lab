CHEESE_LIST = ['cheddar', 'gouda', 'camembert']
def roll_call_dwarves(list):
    for dwarf in list:
        print(f'{list.index(dwarf) + 1}. {dwarf}')

def summon_captain_planet(list):
    return [f'{item.title()}!' for item in list]

def long_planeteer_calls(list):
    true_or_false = [True for item in list if len(item) > 4]
    return True if true_or_false else False

def find_the_cheese(list):
    for item in list:
        if item in CHEESE_LIST:
            return item
    return None
