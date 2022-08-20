"""
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저
있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서
남겨놓는다.
현수과 수확하는 사과의 총 개수를 출력하세요.
▣ 입력설명
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.
"""

import sys
sys.stdin=open("input.txt","rt")
n = int(input())
arrSquare=[]
hap=0
for i in range(0,n):
    arr=list(map(int, input().split()))
    arrSquare.append(arr)
m=n//2
for i in range(0,n):
    if i<m:
        for j in range(m-i,m+i+1):
            hap += arrSquare[i][j]
    elif i==m:
        for j in range(n):
            hap += arrSquare[i][j]
    else:
        for j in range(m-(n-1-i),m+(n-1-i)+1):
            hap += arrSquare[i][j]
print(hap)