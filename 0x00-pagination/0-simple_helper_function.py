#!/usr/bin/env python3
""" takes two integer arguments page and page_size """


def index_range(page: int, page_size: int) -> tuple:
    """ function parameters"""
    start_index = (page - 1) * page_size
    end_index = start_idex + page_size
    return start_index, end_index