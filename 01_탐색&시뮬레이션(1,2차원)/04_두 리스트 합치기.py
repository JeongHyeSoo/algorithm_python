"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
"""

import sys
sys.stdin=open("input.txt","rt")
n1=int(input())
a1=list(map(int, input().split()))
n2=int(input())
a2=list(map(int, input().split()))

for j in range(0,n2):
    for i in range(0,n1):
        if a1[i]>a2[j]:
            a1.insert(i,a2[j])
            n1+=1
            break
    else:
            a1.append(a2[j])
for i in a1:
    print(i,end=' ')