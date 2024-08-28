def addition(x,y):
    if(x<0): x*=-1
    if(y<0): y*=-1
    return x+y

x = -3
y = 5
ans = addition(x,y)
print(ans)