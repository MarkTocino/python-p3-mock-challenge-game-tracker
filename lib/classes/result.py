class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
        player.results(self)
        player.games_played(self)
        game.results(self)
        game.players(self)
        self.result_append(self)
    @classmethod
    def result_append(cls, results):
        cls.all.append(results)
    def get_score(self):
        return self._score
    def set_score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else: 
            raise Exception
    score = property (get_score, set_score)

    def get_player(self):
        return self._player
    def set_player(self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else: 
            raise Exception ("player must be instance of Player")
        
    player = property(get_player, set_player)

    def get_game(self):
        return self._game
    def set_game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else: 
            raise Exception ("game must be instance of Game")
        
    game = property(get_game, set_game)
    pass