"""
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
"""

import sys
sys.stdin=open("input.txt","rt")
n, m=map(int, input().split())
hapMax = n+m
perMax = 0
cnt = [0]*(hapMax+3)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
for i in range(hapMax+1):
    if perMax < cnt[i]:
        perMax=cnt[i]
for i in range(hapMax+1):
    if cnt[i]==perMax:
        print(i, end=' ')