class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def sort_by_points(self, player):
        return player.goals + player.assists

    def top_scorers_by_nationality(self, nationality):     
        players = []
        for player in self.reader.get_players():
            if player.nationality == nationality:
                players.append(player)

        return sorted(players, key=self.sort_by_points, reverse=True)