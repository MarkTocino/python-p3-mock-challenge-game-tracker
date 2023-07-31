class Player:

    all = []

    def __init__(self, username):

        self.username = username
        self._results = []
        self._games_played = []
        self.players(self)
    @classmethod
    def players(cls, players):
        cls.all.append(players)
        
    def get_username(self):
       return self._username
    def set_username(self, username):
        if 2 <= len(username) <= 16:
           self._username = username
        else:
            raise Exception("Username must be 2-16 long")
        
    username = property(get_username, set_username)
    
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
        pass
    
    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False
        
    
    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])
        
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
