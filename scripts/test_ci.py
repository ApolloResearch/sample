import os
from typing import Callable

import torch

TTC = Callable[[torch.Tensor], torch.Tensor]


class MLP(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear: TTC = torch.nn.Linear(10, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    model = MLP()
    print(model)
    print(model(torch.zeros(10)))
    print("Success!")
