from classes_and_objects_exercise.project_guild.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for man in self.players:
            if man.name == player_name:
                self.players.remove(man)
                man.guild = 'Unaffiliated'
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for p in self.players:
            result += f"\n{p.player_info()}"

        return result
