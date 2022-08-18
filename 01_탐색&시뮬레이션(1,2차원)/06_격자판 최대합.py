"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.
▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.
"""
import sys
sys.stdin=open("input.txt","rt")
n = int(input())
arrSquare=[]
for i in range(0,n):
    arr=list(map(int, input().split()))
    arrSquare.append(arr)
arrHap=[0]*(n*2+2)
for i in range(0,n):
    for j in range(0,n):
        arrHap[i]+=arrSquare[i][j]
        arrHap[n+i]+=arrSquare[j][i]
for j in range(0,n):
    arrHap[2*n]+=arrSquare[j][j]
    arrHap[2*n+1]+=arrSquare[j][n-1-j]
max=0
for i in range(0,n*2+2):
    if max<arrHap[i]:
        max=arrHap[i]
print(max)