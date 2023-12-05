def roll_call_dwarves(names):
    for index,name in enumerate(names):
        print(f"{index+1}. {name}")

def summon_captain_planet(elements):
    return[element.capitalize()+"!" for element in elements]
   

def long_planeteer_calls(calls):
    for call in calls:
        if len(call)>4:
            return True
    return False


def find_the_cheese(strings):
    for word in strings:
        if word in ["cheddar","gouda","camembert"]:
            return word
   
