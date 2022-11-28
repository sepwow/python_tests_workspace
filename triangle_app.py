def triangle(a, b, c):
    flag = ''
    if a + b <= c:
        flag = 'c'
    elif a + c <= b:
        flag = 'b'
    elif b + c <= a:
        flag = 'a'
    else:
        return True

    if flag != '':
        return False
        return "'%s' > суммы других" % flag


p = triangle(1, 4, 5)
print(p)
