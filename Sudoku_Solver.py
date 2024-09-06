import copy


def check(vec):
    for val in set(vec):
        if val != 0:
            if vec.count(val) > 1:
                return True
    return False


def square(puzzle, i, j):
    reshaped = [puzzle[i//3*3 + loc//3][j//3*3 + loc % 3] for loc in range(9)]
    return check(reshaped)


def viable(puzzle, i, j):
    row = check(puzzle[i])
    column = check([row[j] for row in puzzle])
    segment = square(puzzle, i, j)
    if sum([row, column, segment]) > 0:
        return False
    return True


def sudoku(puzzle):
    solution = copy.deepcopy(puzzle)
    separate = [[0]*9 for i in range(9)]
    loc = 0
    iteration = 0
    while loc < 9*9:
        iteration += 1
        i = loc//9
        j = loc % 9
        if viable(solution, i, j):
            if puzzle[i][j] == 0:
                if solution[i][j] < 9:
                    solution[i][j] += 1
                    separate[i][j] += 1
                if viable(solution, i, j):
                    loc += 1
            else:
                loc += 1
        elif viable(separate, i, j):
            if separate[i][j] < 9:
                solution[i][j] += 1
                separate[i][j] += 1
                if viable(solution, i, j):
                    loc += 1
            else:
                while puzzle[loc // 9][loc % 9] != 0 or separate[loc // 9][loc % 9] == 9:
                    if separate[loc // 9][loc % 9] == 9:
                        solution[loc // 9][loc % 9] = 0
                        separate[loc // 9][loc % 9] = 0
                    loc -= 1
        elif solution[i][j] < 9:
            solution[i][j] += 1
            separate[i][j] += 1
            if viable(solution, i, j):
                loc += 1
        else:
            solution[i][j] = 0
            separate[i][j] = 0
            loc -= 1
            while puzzle[loc//9][loc % 9] != 0 or separate[loc//9][loc % 9] == 9:
                if separate[loc//9][loc % 9] == 9:
                    solution[loc//9][loc % 9] = 0
                    separate[loc // 9][loc % 9] = 0
                loc -= 1
    return solution
