# Search Entry Matrix
def find_elem_matrix_bool(m1, value):
    found = False
    row = 0
    col = len(m1[0])-1
    while row < len(m1) and col > 0:
        if m1[row][col] == value:
            found = True
            break
        elif m1[row][col] > value:
            col -= 1
        else:
            row += 1
    return found
