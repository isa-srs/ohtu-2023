class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_names = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty'
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def even_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        return "Deuce"
    
    def uneven_score(self):
        return f'{self.score_names[self.m_score1]}-{self.score_names[self.m_score2]}'

    def advantage_or_win(self):
        diff = self.m_score1 - self.m_score2

        score = ""
        if diff == 1:
            return "Advantage player1"
        elif diff == -1:
            return "Advantage player2"
        elif diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            score = self.even_score()
        
        elif self.m_score1 < 4 and self.m_score2 < 4:
            score = self.uneven_score()

        else:
            score = self.advantage_or_win()

        return score
