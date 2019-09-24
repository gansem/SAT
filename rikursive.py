import copy
from typing import List

import mxklabs.dimacs


def simplify(_clause_list: List[List[int]], _known_numbers: List[List[int]]):
    for number in _known_numbers:
        for clause in _clause_list[:]:
            try:
                negative_number = -number[0]
            except TypeError:
                print('error')
            if number[0] in clause:
                _clause_list.remove(clause)
            elif negative_number in clause:
                clause.remove(negative_number)
    return _clause_list


def remove_unit_clause(_clause_list, _known_numbers):
    unit_clause_list = []
    for clause in _clause_list:
        if len(clause) == 1:
            unit_clause_list.append(clause)
    for unit_clause in unit_clause_list:
        minus_unit_clause = [-unit_clause[0]]
        if unit_clause in unit_clause_list and minus_unit_clause in unit_clause_list:
            print('cont')
            exit()
            # clause_list, known_numbers = backtracking(clause_list, known_numbers)
        else:
            _known_numbers.append(unit_clause)


def split(_clause_list, _known_numbers):
    remaining_literals = set()
    for clause in _clause_list:
        for literal in clause:
            remaining_literals.add(abs(literal))
    print('split')
    for chosen_number in remaining_literals:
        copy_clause_list = copy.deepcopy(_clause_list)
        copy_known_numbers = copy.deepcopy(_known_numbers)
        copy_known_numbers.append([chosen_number])
        print(chosen_number)
        _success, _result = dp(copy_clause_list, copy_known_numbers)
        if _success:
            return _success, _result
    print('contradiction')
    return False, known_numbers


# def backtracking(_clause_list, _known_numbers):
#     global deepcopy_list
#     global split_value_list
#     # returns clause_list to earlier state
#     _clause_list = deepcopy_list[-1]
#     # determines the last chosen (splitted value)
#     value_to_flip = split_value_list[-1]
#     # returns known_numbers to earlier state
#     target_index = _known_numbers.index(value_to_flip)
#     _known_numbers = _known_numbers[:target_index]
#     # changes last flipped value in know_numbers
#     _known_numbers.append(-value_to_flip)
#
#     return _clause_list, _known_numbers


sudoku_rules = "sudoku-rules.txt"
sudoku_game = "sudoku-example.txt"

clause_list = mxklabs.dimacs.read(sudoku_rules).clauses
known_numbers = mxklabs.dimacs.read(sudoku_game).clauses
deepcopy_list = []
split_value_list = []


def dp(_clause_list: List[List[int]], _known_numbers: List[List[int]]) -> (bool, List[List[int]]):
    while True:
        clause_len = len(_clause_list)
        simplify(_clause_list, _known_numbers)
        remove_unit_clause(_clause_list, _known_numbers)

        if clause_len == len(_clause_list):
            break
    if len(_clause_list) != 0:
        return split(_clause_list, _known_numbers)
    return True, _known_numbers


success, result = dp(clause_list, known_numbers)
print(result)
