'''
재귀 함수의 두 가지 분석 방법
1. 상향식 분석과 하향식 분석
    - 하향식 분석
    가장 위쪽에 위치한 상자의 함수 호출부터 시작하여 계단식으로
    자세히 조사해 나가는 분석

    - 상향식 분석
    가장 아래쪽에 위치한 상자의 함수 호출부터 시작해서 위로 올라가는 것

2.
if n>0:
    recur(n-1)
    print(n)
    recur(n-2)

    의 순서를 바꾸면 거꾸로 출력이 가능
'''

def recur(n: int) -> int:
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input("정숫값을 입력하세요. : "))

recur(x)