d=[0]*100
d[1]=1
d[2]=1
#큰 문제를 작은 문제로 나눠서 작은문제에서 풀어나가는 알고리즘.
#이미 해결결과가 메모리에 있음.
for i in range(3,100):
    d[i]=d[i-1]+d[i-2]
print(d[99])