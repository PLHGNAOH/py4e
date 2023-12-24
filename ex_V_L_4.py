for i in range(10,100):
    dv = i % 10
    c = i // 10
    if dv * c == (dv+c)*2:
        print(i)