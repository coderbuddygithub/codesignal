def shapeArea(n):
    sum=0
    for i in range(1,n+1):
        sum=i+sum 
    return ((sum*4)-(n*4)+1)