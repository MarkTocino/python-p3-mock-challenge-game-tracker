class Game:
    def __init__(self, title):

        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception
        self._results = []
        self._players = []

    def get_title(self):
        return self._title
    
    title = property(get_title)
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
        
    
    def average_score(self, player):
        result = [game.score for game in self._results if game.player == player]
        return sum(result) / len(result)
    