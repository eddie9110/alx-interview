#!/usr/bin/python3
"""Module contains function to make a pascal triangle"""

def pascal_triangle(n):
    """Creates a pascal triangle"""
    if n <= 0:
        return []
    list_row = []
    for a in range(n):
        tmp_list = []
        for x in range (a+1):
            if x==0 or x==a:
                tmp_list.append(1)
            else:
                tmp_list.append(list_row[a-1][x-1] + list_row[a-1][x])
        list_row.append(tmp_list)
    return list_row
