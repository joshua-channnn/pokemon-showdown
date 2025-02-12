from poke_env.player import (
    Player,
    RandomPlayer,
    cross_evaluate,
    background_cross_evaluate,
    background_evaluate_player,
)
import asyncio

        

class MaxDamage2v2Player(Player):
    def choose_move(self, battle):
        if battle.available_moves:
            best_move = max(battle.available_moves, key=lambda move: move.base_power)

            if battle.can_tera:
                return self.create_order(best_move, terastallize=True)

            return self.create_order(best_move)
        else:
            return self.choose_random_move(battle)

# Create players
player3 = RandomPlayer(
    battle_format="gen9randombattle2v2",
)
player4 = MaxDamage2v2Player(
    battle_format="gen9randombattle2v2",
)

# Run a battle
async def main():
    await player3.battle_against(player4, n_battles=5)
    print(f"Result: {player3.n_won_battles} wins, {player4.n_won_battles} losses")
    	

asyncio.run(main())