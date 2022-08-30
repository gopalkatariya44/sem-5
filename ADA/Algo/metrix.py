# def matrix_90(ls):
#     for i in range(len(ls)):
#

if __name__ == '__main__':
    ls = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



    ls_90 = []
    l = []
    for i in range(len(ls) - 1, -1, -1):
        l.append(ls[i][0])
    ls_90.append(l)
    l = []
    for i in range(len(ls) - 1, -1, -1):
        l.append(ls[i][1])
    ls_90.append(l)
    l = []
    for i in range(len(ls) - 1, -1, -1):
        l.append(ls[i][2])
    ls_90.append(l)

    # for i in range(len(ls) - 1, -1, -1):
    #     for j in range(len(ls)):
    #         if ls[i][j]


    print(ls_90)
