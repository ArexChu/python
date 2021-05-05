#encoding=utf-8

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

s = list(map(lambda x,y:x+y,m[1],n[1]))
print(s)
