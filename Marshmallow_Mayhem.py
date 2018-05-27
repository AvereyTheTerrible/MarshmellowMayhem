# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 06:58:48 2018
@author: Averey
"""
RANK_NAME = ['General', 'Commander', 'Spy']
TEAM_CONFIG = [1, 2, 1]

COUNTDOWN = 3
 
class GamePiece:
    def __init__(self, rank):
        self.rank = rank
        self.is_live = True
        self.countdown_mobile = 0
        self.countdown_hidden = 0
        self.team = None
    
    def __repr__(self):
        return '{}-{}'.format(self.team, RANK_NAME[self.rank])
    
    def attack(self, opponent):
        print('{} attacks {}'.format(self, opponent))
        if self.rank == 0 and opponent.rank == len(RANK_NAME) - 1:
            self.is_live = False
        elif (self.rank == len(RANK_NAME) - 1 and opponent.rank == 0) or \
            (self.rank < opponent.rank):
            print('Attacker wins and immobolized!')
            self.countdown_mobile = COUNTDOWN
            self.countdown_hidden = COUNTDOWN
        elif self.rank >= opponent.rank:



            print('Attackers loses.')
        else:
            print('THIS SHOULD NEVER HAPPEN!')
        
    def move(self):
        print('I am moving')
    
    def run(self):
        if self.countdown_mobile > 0:
            self.countdown_mobile -=1
        if self.countdown_hidden > 0:
            self.countdown_hidden -=1

def test_attack(attacker, defender):
    if attacker.team == defender.team:
        print("You are cannot attack your own army.")
    else:
        attacker.attack(defender) 

class Team:
    def __init__(self, name):
        self.is_live = True
        self.name = name
        self.soldiers = list()
    
        print('Creating Team {}'.format(self.name))
        for i in range(len(TEAM_CONFIG)):
            n = TEAM_CONFIG[i]
            r_num = i
            r_name = RANK_NAME[i]
            print("\t{} X {}(s)".format(n, r_name))
            for _ in range(n):
                p = GamePiece(r_num)
                p.team = self
                self.soldiers.append(p)
        print('Team {} creation is finished!\n'.format(self.name))
        
    def run(self):
        c = 0
    
        for p in self.soldiers:
            if p.is_live == True:
                c += 1
                print('Game piece {} {} is alive!'.format(self.name, RANK_NAME[p.rank]))
            else:
                print('Game piece is dead!')
        self.is_live = c > 0
    
    def __repr__(self):
        return 'Team {}, number of soldiers = {}'.format(self.name, len(self.soldiers))
    
        

class Game:
    def __init__(self, team_names):
        self.teams = list()
        self.turns = 0
        for name in team_names:
            self.teams.append(Team(name))
            
    def run(self, n = 3):
        for _ in range(n):
            self.turns += 1
            for team in self.teams:
                team.run()
                if team.is_live == True:
                    print('Team {} is still alive!'.format(self.teams))
                else:
                    print('Team is dead!')
                    
if __name__ == '__main__':
    game1 = Game(['green','black'])
    game1.run()
    test_attack(game1.teams[0].soldiers[0],
                game1.teams[1].soldiers[1])
    test_attack(game1.teams[0].soldiers[3],
                game1.teams[0].soldiers[3])
    test_attack(game1.teams[1].soldiers[3],
                game1.teams[0].soldiers[0])
                    
            