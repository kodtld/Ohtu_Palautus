from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player("home", player1_name, 0)
        self.player2 = Player("away", player2_name , 0)
        self.scores = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}
        self.overtime = 0

    def won_point(self, player_team):
        if player_team == "home":
            self.player1.points += 1
        elif player_team == "away":
            self.player2.points += 1

    def get_tie(self):
        return self.player1.points == self.player2.points

    def get_points(self):
        return {"home": self.player1.points, "away": self.player2.points}        
    
    def get_deuce(self):
        if self.get_points()['home'] >= 4 and self.get_points()['away'] >= 4:
            if self.player1.points == self.player2.points:
                self.overtime = 1
                return True 

    def get_winner(self):
        if self.overtime == 0:
            
            if (self.player1.points == 4 and self.player2.points == 3) or self.player2.points == 4 and self.player1.points == 3:
                self.overtime = 1
                
            elif self.player1.points == 4 and self.player2.points < 4:
                return "Win for player1" 
            
            elif self.player2.points == 4 and self.player1.points < 4:
                return "Win for player2" 

            elif self.player1.points > 4 and self.player2.points < self.player1.points and self.player1.points - self.player2.points == 2:
                return "Win for player1" 

            elif self.player2.points > 4 and self.player1.points < self.player2.points and self.player2.points - self.player1.points == 2:
                return "Win for player2" 

        elif self.overtime == 1:
            if self.overtime_win():
                if self.player1.points > self.player2.points:
                    return "Win for player1" 

                elif self.player2.points > self.player1.points:
                    return "Win for player2" 

    def overtime_win(self):
        return self.player1.points - self.player2.points == 2 or self.player2.points - self.player1.points == 2

    def get_overtime(self):
        return self.player1.points >=3 and self.player2.points >=3

    def get_advantage(self):
        if self.get_overtime():
            if self.player1.points > self.player2.points and self.player1.points - self.player2.points == 1:
                return "Advantage player1" #+ self.player1.name

            elif self.player2.points > self.player1.points and self.player2.points - self.player1.points == 1:
                return "Advantage player2" #+ self.player2.name

    def get_score(self):
        if self.get_deuce():
            return "Deuce"
        
        if self.get_tie():
            return self.scores[self.get_points()['home']] + "-All"
        

        if not self.get_tie():
            if self.get_winner():
                return self.get_winner()

            elif self.get_advantage():
                return self.get_advantage()

            else:
                return self.scores[self.get_points()['home']] + "-" + self.scores[self.get_points()['away']]


