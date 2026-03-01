#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # (Holberton starter mentions truncation, but expected output uses full set)
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page starting at `index`.

        Args:
            index (Optional[int]): Start index (0-based). Defaults to 0 if None.
            page_size (int): Number of items to return. Defaults to 10.

        Returns:
            Dict: {
                'index': current index,
                'next_index': next index to query,
                'page_size': current page size,
                'data': page data
            }
        """
        if index is None:
            index = 0

        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        dataset_len = len(self.dataset())

        # index must be within original dataset bounds
        assert 0 <= index < dataset_len

        data: List[List] = []
        current = index

        # Collect exactly page_size existing rows, skipping deleted indexes
        while len(data) < page_size and current < dataset_len:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
