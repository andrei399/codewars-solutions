#https://www.codewars.com/kata/536e9a7973130a06eb000e9f/
def calculate_damage(your_type, opponent_type, attack, defense):
    #for this kata if enemy pokemon is the same type as your pokemon the attack will be ineffective!!!
    if your_type == opponent_type: return 50*attack/defense/2
    else:
        multiplier = 1
        if your_type == 'fire':
            if opponent_type == 'grass': multiplier = 2
            if opponent_type == 'water': multiplier = 0.5
        elif your_type == 'water':
            if opponent_type == 'fire': multiplier = 2
            else: multiplier = 0.5
        elif your_type == 'grass':
            if opponent_type == 'water': multiplier = 2
            elif opponent_type == 'electric': multiplier = 1
            else: multiplier = 0.5
        elif your_type == 'electric':
            if opponent_type == 'water': multiplier = 2
    return 50*attack/defense*multiplier


def main():
    print(calculate_damage("fire", "water", 100, 100))

if __name__ == '__main__':
    main()
