def sol(chess, q_x, q_y, possible_moves = 0):
    x, y = q_x - 1, q_y - 1
    
    
    possible_moves += get_moves(chess, x, y, "x - 1", "y - 1", "x >= 0", "y >= 0")# diagonally top left
    possible_moves += get_moves(chess, x, y, "x - 1", "y + 1", "x >= 0", "y < len(chess)")# diagonally top right
    possible_moves += get_moves(chess, x, y, "x - 1", "y", "x >= 0", "True")# up
    possible_moves += get_moves(chess, x, y, "x + 1", "y", "x < len(chess)", "True")# down
    possible_moves += get_moves(chess, x, y, "x + 1", "y + 1", "x < len(chess)", "y < len(chess)")# diagonally down right
    possible_moves += get_moves(chess, x, y, "x + 1", "y - 1", "x < len(chess)", "y >= 0")# diagonally down left
    possible_moves += get_moves(chess, x, y, "x", "y + 1", "True", "y < len(chess)")# right
    possible_moves += get_moves(chess, x, y, "x", "y - 1", "True", "y >= 0")# left
    
    return possible_moves
    
def get_moves(chess, x, y, expression_x, expression_y, bound_x, bound_y, possible_moves = 0):
    x, y = eval(expression_x), eval(expression_y) 
    while eval(bound_x) and eval(bound_y) and chess[x][y] != "X":
        possible_moves += 1
        x, y = eval(expression_x), eval(expression_y)
    return possible_moves
    
    
if __name__ == "__main__":
    n, obstacles = map(int, input().split())
    chess = [["_" for _ in range(n)] for _ in range(n)]
    queen_row, queen_col = map(int, input().split())
    chess[queen_row - 1][queen_col - 1] = "Q"
    
    
    coordinates = []
    for _ in range(obstacles):
        x, y = map(int, input().split())
        chess[x - 1][y - 1] = "X"
    
    print (sol(chess, queen_row, queen_col))
    