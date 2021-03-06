'''
버블 정렬
단순 선택 정렬
단순 삽입 정렬은
O(n^2)으로 원소 수가 많아지만 계산 비용이 증가한다. 이를 대비하기 위한 방법이 이진 삽입 정렬
'''

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    '''
    n개 원소 리스트 a의 길이 n
    1. 1부터 n까지 순회
    '''
    for i in range (1, n):
        key = a[i]
        pl  = 0
        pr  = i - 1
        '''
        검색 범위는 i 번째 원소까지이다.
            검색 범위의 첫 번째 인덱스와 마지막 인덱스를 pl, pr에 할당
                1. 만약에 중간 인덱스 i인덱스의 원소가 0 ~ i-1 범위의 중간 인덱스와 같으면 ㅓㅁ춤
                2. 만야에 중간 인덱스 우ㅜㅜㅜㅜㅜㅝ
        '''
        
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range (i, pd, -1):
            a[j] = a[j-1]

        a[pd] = key

if __name__ == "__main__":
    print("이진 삽입 정렬을 수행합니다.")

    num = int(input("원소 수를 입력하세요. "))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)

    print("오름차순으로 정렬합니다. ")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')