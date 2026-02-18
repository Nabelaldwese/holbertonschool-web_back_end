#!/usr/bin/env python3
"""Module that contains a type-annotated element_length function."""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
