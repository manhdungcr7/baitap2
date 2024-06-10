n=int(input())
m=list(map(int,input().split()))
a=int(input())
b=list(map(int,input().split()))
def binary(a,x):
    l=0
    r=len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
        	while m<len(a) :
            		if a[m+1]>x :
            			return m
            		else:
            			m+=1
            	return m
        elif a[m]>x:
            r=m-1
        else:
            l=m+1
    return -1
for x in b:
	print(binary(m,x))
