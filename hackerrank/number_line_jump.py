def kangaroo(x1, v1, x2, v2):
    # starting point is x1 and x2, and the distance to move is v1 and v2
    # condition 1 : if one of kangaroo has both position ahead and bigger velocity, they will not be meet
    # condition 2 : check the time is will be zero using kinematics equations
    if ((x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or (v2 == v1 and x2 != x1)):
        return 'NO'

    return 'YES' if (x2 - x1)%(v2 - v1) == 0 else 'NO'

if __name__ == '__main__':
    print(kangaroo(0, 3, 4, 2))
    print(kangaroo(0, 2, 5, 3))
    print(kangaroo(43, 2, 70, 2))