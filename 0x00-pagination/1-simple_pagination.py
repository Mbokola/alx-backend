#!/usr/bin/env python3
""" 1-simple_pagination module """
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple:
        """
        return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        return ((page * page_size) - page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets the page """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        idx = self.index_range(page, page_size)
        dataset = self.dataset()
        if idx[1] > len(dataset):
            return []
        return dataset[idx[0]:idx[1]]
