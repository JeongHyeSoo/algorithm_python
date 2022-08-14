"""
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
"""
import sys
sys.stdin=open("input.txt","rt")
T=int(input())
score=list(map(int, input().split()))
avg=0
hap=0
minDif=100000000
studentNum=0

for t in range(T):
    hap=hap+score[t]
avg=hap/T
avg=round(avg)

#abs() -> 절대값 구하는 함수
for t in range(T):
    if (abs(score[t]-avg)<minDif):
        minDif=abs(score[t]-avg)
        studentNum=t+1
    elif (abs(score[t]-avg)==(abs(score[studentNum-1]-avg))):
        if(score[t]>score[studentNum-1]):
            studentNum=t+1
print("%d %d" %(avg, studentNum))