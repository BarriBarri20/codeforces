
for i in range(int(input())):
    _=input()
    s=1
    l=[int(j) for j in input().split()]
    h=sorted(l,reverse=1)
    x=h[0]
    for i in range(1,len(h)):
        x-=h[i]

    if any(h):
        if x <= 0 :
            print(1)
        else :
            print(x)
    else :
        print(0)
    