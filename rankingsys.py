#https://www.codewars.com/kata/51fda2d95d6efda45e00004e
class User:
    possible_ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.total_progress = 0
    def inc_progress(self, challenge_rank):
        difference = User.possible_ranks.index(self.rank) - User.possible_ranks.index(challenge_rank)
        if difference == 1:
            self.progress += 1
            self.total_progress += 1
        elif difference == 0:
            self.progress += 3
            self.total_progress += 3
        elif difference < 0:
            self.progress += 10*difference**2
            self.total_progress += 10*difference**2
        self.rank = User.possible_ranks[self.total_progress//100]
        if self.progress >=  100:
            self.progress -= 100

