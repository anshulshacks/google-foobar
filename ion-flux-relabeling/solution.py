def getParent(parent, root, height, target):
    if (root == target):
        return parent
    left_child = root - 2**(height - 1)
    right_child = root - 1
    height -= 1
    if (target <= left_child):
        return getParent(root, left_child, height, target)
    return getParent(root, right_child, height, target)


def solution(h, q):
    ans = []
    for node in q:
        ans.append(getParent(-1, 2**h - 1, h, node))
    return ans
