class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, newname):
        self.players.append(newname)
    def has_player(self, wanted):
        for player in self.players:
            if wanted == player:
                return True
        return False
    def play_game(self, win_lose):
        if win_lose == True:
            self.points += 3