"""
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다.
"""
import sys
sys.stdin=open("input.txt","rt")
n=int(input())
firstList=list(map(int, input().split()))
reversedList = []

def reverse(x):
    result=0
    while x>0:
        a=x%10
        result=result*10+a
        x=x//10
    return result

def isPrime(x):
    if x==1:
        return False
    else:
        for j in range(2, x):
            if x % j == 0:
                return False
        else:
            return True

for x in firstList:
    tmp=reverse(x)
    if isPrime(tmp):
        reversedList.append(tmp)
        print(tmp, end=' ')

