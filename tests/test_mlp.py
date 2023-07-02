from typing import List, Tuple

import pytest
from torch import nn

from mypkg.models import MLP


@pytest.mark.parametrize(
    "input_size, hidden_sizes, output_size, expected_layer_sizes",
    [
        (784, [128, 64], 10, [(784, 128), (128, 64), (64, 10)]),  # 2 hidden layers
        (784, [], 10, [(784, 10)]),  # no hidden layers
        (784, [128], 10, [(784, 128), (128, 10)]),  # 1 hidden layer
        (784, [128, 64, 32], 10, [(784, 128), (128, 64), (64, 32), (32, 10)]),  # 3 hidden layers
    ],
)
def test_make_layers(
    input_size: int,
    hidden_sizes: List[int],
    output_size: int,
    expected_layer_sizes: List[Tuple[int, int]],
):
    """Test the _make_layers method of MLP class.

    Verifies the returned layers' types and sizes.
    """
    layers = MLP.make_layers(input_size, hidden_sizes, output_size)
    assert isinstance(layers, nn.Sequential)
    # Multiply by 2 for ReLU layers and subtract 1 as there's no ReLU after last Linear layer
    assert len(layers) == len(expected_layer_sizes) * 2 - 1

    # Check types and sizes of layers
    # Indices of Linear layers (0, 2, 4, ...)
    linear_layer_indices = range(0, len(layers), 2)
    for i, layer in enumerate(layers):
        if i in linear_layer_indices:
            assert isinstance(layer, nn.Linear)
            assert layer.in_features == expected_layer_sizes[i // 2][0]
            assert layer.out_features == expected_layer_sizes[i // 2][1]
        else:
            # ReLU layers at other indices
            assert isinstance(layer, nn.ReLU)
