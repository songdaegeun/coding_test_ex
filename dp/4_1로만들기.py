#%5, %3, %2, -1을 사용할 수 있다.
#매 연산마다 최소가 되는 값을 선택해야한다. 
#반복되는 부분이 있다. (f(6)을 기준으로 한번 도식을 그려봐라.)
#구조를 찾고 bottom up을 사용하자.
#bottom up으로 가면 dp테이블체크할 필요없다.

x=int(input())
#d는 각 수에 도달하기까지 연산횟수를 count하기위해 사용한다.
d=[0]*(x+1)

for i in range(2,x+1):
    #규칙이 있는게 아니다. 큰 x에 대한 연산횟수를 알려면 작은 x에 대한 연산횟수를 알아야하기 때문에 반복문으로 작은 x에 대한 결과부터 얻는 것이다.
    # -1을 하는 경우
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
print(d[x])    