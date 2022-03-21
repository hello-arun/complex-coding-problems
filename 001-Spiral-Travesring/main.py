def spiralTraverse(a, n, m):
    top = 0
    down = n-1
    left = 0
    right = m-1
    dir = 0
    res = []

    while(top <= down and left <= right):
        # if(dir == 0):
        for i in range(left, right+1):
            res.append(a[top][i])
        top += 1
    # elif(dir == 1):
        for i in range(top, down+1):
            res.append(a[i][right])
        right -= 1
    # elif(dir == 2):
        for i in range(right, left-1, -1):
            res.append(a[down][i])
        down -= 1
    # elif(dir == 3):
        for i in range(down, top-1, -1):
            res.append(a[i][left])
        left += 1

        # dir = (dir+1) % 4
    return(res)


# Driver Code
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]]
print(spiralTraverse(a, len(a), len(a[0])))
