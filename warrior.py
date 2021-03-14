#https://www.codewars.com/kata/5941c545f5c394fef900000c
warrior_status = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran",
                  "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]


class Warrior:

    def __init__(self):
        '''
        Initialize function
        '''
        self.level = 1
        self.rank = warrior_status[0]
        self.experience = 100
        self.achievements = []

    def level_up(self):
        '''
        Level up after gaining experience
        !!!TO BE CALLED AFTER GAINING EXPERIENCE!!!
        '''
        self.level = self.experience // 100
        if self.level > 100:
            self.level = 100
        if self.level == 100 and self.experience > 10000:
            self.experience = 10000
        self.rank = warrior_status[self.level//10]

    def battle(self, enemy_level):
        '''
        Battle an enemy to gain experience!
        CALL level_up() after every experience gain!!
        '''
        if enemy_level > 100 or enemy_level < 1:
            return 'Invalid level'
        if enemy_level - 5 >= self.level and enemy_level//10 > self.level / 10:
            return "You've been defeated"
        if enemy_level == self.level:
            self.experience += 10
        elif enemy_level + 1 == self.level:
            self.experience += 5
        elif enemy_level + 2 <= self.level:
            self.experience += 0
        else:
            self.experience += 20 * (enemy_level - self.level) ** 2
        prev_level = self.level
        self.level_up()
        if prev_level - 2 >= enemy_level:
            return "Easy fight"
        elif prev_level - 1 == enemy_level or prev_level == enemy_level:
            return "A good fight"
        else:
            return "An intense fight"

    def training(self, trainers):
        '''
        Training, call leve_up() before return
        '''
        if self.level < trainers[2]:
            return "Not strong enough"
        self.achievements.append(trainers[0])
        self.experience += trainers[1]
        self.level_up()
        return trainers[0]


def main():
    bruce_lee = Warrior()
    print(bruce_lee.level)  # => 1
    print(bruce_lee.experience)  # => 100
    print(bruce_lee.rank)  # => "Pushover"
    print(bruce_lee.achievements)  # => []
    print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))  # => "Defeated Chuck Norris"
    print(bruce_lee.experience)  # => 9100
    print(bruce_lee.level)  # => 91
    print(bruce_lee.rank)  # => "Master"
    print(bruce_lee.battle(90))  # => "A good fight"
    print(bruce_lee.experience)  # => 9105
    print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]

if __name__ == '__main__':
    main()
