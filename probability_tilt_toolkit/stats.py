import pandas as pd
from .monty import MontyGame
from typing import Literal

def run_trials(n_trials: int = 10000, n_doors: int = 3,
               strategy: Literal["stick", "switch"] = "switch"):
    wins = 0
    game = MontyGame(n_doors)
    for _ in range(n_trials):
        game.reset()
        game.first_pick(0)           # arbitrary first door
        wins += game.switch() if strategy == "switch" else game.stick()
    return wins / n_trials

def summary_df(n_doors_list=(3, 10, 50, 100), trials=10000):
    rows = []
    for n in n_doors_list:
        for strat in ("stick", "switch"):
            rows.append(dict(n_doors=n,
                             strategy=strat,
                             win_rate=run_trials(trials, n, strat)))
    return pd.DataFrame(rows)
