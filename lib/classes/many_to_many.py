class Game:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        player_results = [result for result in self.results() if result.player == player]
        if not player_results:
            return 0
        return sum(result.score for result in player_results) / len(player_results)


class Player:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = value

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
