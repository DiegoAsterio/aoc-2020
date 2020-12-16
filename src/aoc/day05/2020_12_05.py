def bsp_to_index(s, ref):
    n = len(s)
    ret = 0
    for i, c in zip(reversed(range(n)), s):
        if c == ref:
           ret += (1 << i) 
    return ret

def index_from_number(n):
    j = n & 0b111
    i = (n >> 3)
    return i, j
           
def load_seats(path):
    ret = []
    with open(path) as f:
        for line in f:
            row = line.strip()[:7]
            col = line.strip()[7:]
            ret.append([row, col])
    return ret
           
if __name__ == "__main__":
    positions = load_seats("2020_12_05.input")

    row = [0]*8
    matrix = [row[:] for x in range(128)]
    max_val = 0
    for row, col in positions:
        index_row = bsp_to_index(row, 'B')
        index_col = bsp_to_index(col, 'R')
        aux_val = index_row*8 + index_col
        if max_val < aux_val:
            max_val = aux_val
        matrix[index_row][index_col]=1

    print(max_val)

    for n in range(1,1023):
        prev_i, prev_j = index_from_number(n-1)
        i, j = index_from_number(n)
        next_i, next_j = index_from_number(n+1)

        prev = matrix[prev_i][prev_j]
        this = matrix[i][j]
        next = matrix[next_i][next_j]

        if prev == 1 and this == 0 and next==1:
            print(n)
