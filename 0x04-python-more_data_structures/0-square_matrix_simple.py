#!/usr/bin/python3
def square_matrix(matrix):
  new_matrix = []
  for row in matrix:
    new_row = []
    for item in row:
      new_row.append(item ** 2)
    new_matrix.append(new_row)
  return new_matrix
