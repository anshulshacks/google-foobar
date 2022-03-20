
import collections
import copy


def get_predecessor(col):
    n = len(col)
    prior = [[2 for _ in range(n + 1)] for _ in range(2)]
    d = {
        1: [
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ],
        0: [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
        ],
    }
    left_counts = collections.defaultdict(list)
    right_counts = collections.defaultdict(list)
    boards = set()
    dq = collections.deque()
    dq.append((prior, 0))
    while len(dq):
        curr, row = dq.popleft()
   
        if row == n:
            board_tup = tuple(map(tuple, curr))
            if board_tup not in boards:
                left_counts[board_tup[1]].append(board_tup[0])
                right_counts[board_tup[0]].append(board_tup[1])
            boards.add(board_tup)
            continue
        if curr[0][row] == 2 and curr[1][row] == 2:
            for nums in d[col[row]]:
                next = copy.deepcopy(curr)
                next[0][row] = nums[0]
                next[1][row] = nums[1]
                next[1][row + 1] = nums[2]
                next[0][row + 1] = nums[3]
                dq.append((next, row + 1))
        else:
            for nums in d[col[row]]:
                if curr[0][row] == nums[0] and curr[1][row] == nums[1]:
                    next = copy.deepcopy(curr)
                    next[1][row + 1] = nums[2]
                    next[0][row + 1] = nums[3]
                    dq.append((next, row + 1))
    return left_counts, right_counts

def solution(in_data):
    g = [[ 1 if in_data[r][c] else 0 for c in range(len(in_data[0]))] for r in range(len(in_data))]
    columns = []
    for c in range(len(g[0])):
        col = [g[r][c] for r in range(len(g))]
        columns.append(col)
    old_num_boards = collections.defaultdict(int)

    lc, _ = get_predecessor(columns[0])
    for right_most, col_list in lc.items():
        for col in col_list:
            old_num_boards[right_most] += 1

    for i in range(1, len(columns)):
        column = columns[i]
        lc, _ = get_predecessor(column)
        new_num_boards = collections.defaultdict(int)
        for right_most, col_list in lc.items():
            for col in col_list:
                new_num_boards[right_most] += old_num_boards[col]
        old_num_boards = new_num_boards

    return sum(old_num_boards.values())
