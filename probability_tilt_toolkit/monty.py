import random
from typing import List

class MontyGame:
    """Generic N-door Monty Hall simulator."""

    def __init__(self, n_doors: int = 3):
        if n_doors < 3:
            raise ValueError("n_doors must be \u2265 3")
        self.n = n_doors
        self.reset()

    def reset(self):
        self.prize = random.randrange(self.n)
        self.player_choice = None
        self.revealed: List[int] = []

    def _host_reveal(self):
        choices = [d for d in range(self.n)
                   if d != self.player_choice and d != self.prize]
        self.revealed = random.sample(choices, self.n - 2)

    def first_pick(self, door: int):
        self.player_choice = door
        self._host_reveal()
        return self.revealed

    def stick(self) -> bool:
        return self.player_choice == self.prize

    def switch(self) -> bool:
        remaining = [d for d in range(self.n)
                     if d not in self.revealed and d != self.player_choice][0]
        return remaining == self.prize
