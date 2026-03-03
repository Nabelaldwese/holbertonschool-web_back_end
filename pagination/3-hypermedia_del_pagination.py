#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

This module defines a Server class that paginates a CSV dataset using an
indexed dictionary to remain resilient to deletions between requests.
"""

import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with cached dataset and indexed dataset."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset loaded from the CSV file (without header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Return a dataset indexed by its original position (starting at 0).

        The dataset is truncated to the first 1000 rows, as specified by the task.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Return deletion-resilient pagination information starting at index."""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        assert index < len(indexed)

        data: List[List[str]] = []
        current = index

        while len(data) < page_size and current < len(indexed) + page_size:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": page_size,
            "data": data,
        }
