class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self.player1_points == self.player2_points:
            score = self.equal_score()

        elif self.player1_points >= 4 or self.player2_points >= 4:
            point_difference = self.player1_points - self. player2_points
            score = self.advantage(point_difference)

        else:
            score = self.form_early_score()

        return score

    def form_early_score(self):
        score = self.early_game_score(self.player1_points, "")
        score += "-"
        score = self.early_game_score(self.player2_points, score)
        return score    
        
    def early_game_score(self, numeric_score, score):
        if numeric_score == 0:
            score += "Love"
        elif numeric_score == 1:
            score += "Fifteen"
        elif numeric_score == 2:
            score += "Thirty"
        elif numeric_score == 3:
            score += "Forty"
        return score

    def equal_score(self):
        if self.player1_points == 0:
            score = "Love-All"
        elif self.player1_points == 1:
            score = "Fifteen-All"
        elif self.player1_points == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"        
        return score
    
    def advantage(self, point_difference):
        if point_difference == 1:
            score = "Advantage player1"
        elif point_difference == -1:
            score = "Advantage player2"
        elif point_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score