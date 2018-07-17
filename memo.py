## Pycharm 사용법
#######################################################################################
# Ctrl + Shift + F10 : 메인모둘 선택 후 처음 실행하기
#                      ( Shift+F10 눌렀을 경우 기본실행되는 프로그램 지정하는 효과있음)
# Shift + F10 : 수정한 소스를 자동 저장하고, Ctrl + Shift + F10에 지정한 프로그램을 실행함
#               ※ 소스를 저장하고, 메인함수를 선택한 후 Run 할 필요없어 Tool 조작시간 단축
# Ctrl + F8 : Debugging을 위한 break point 토글키
# Shift + F9 : Debugging 시작하기. 사전에 적정위치에 break point (Ctrl + F8) 설정해 줘야 함
# F8 : Step Over (Next Step으로 Debugging 하기)
# F7 : Step Into (한단계 더(깊숙히) 내려가기, 예)함수 호출 시 해당 함수로 진입됨)
# Shift + F8 : Step Out(한 단계 밖으로 빠져 나오기)

## Dictionary Key 또는 Value로 Sort (2차원리스트 2번째 요소로 정렬)
## Dictionary Sort
import operator
myDic = {'d':1, 'a': 10,  'b': 14,  'c': 9}
smyDic = sorted(myDic.items(), key=operator.itemgetter(0), reverse = False)
#smyDic = sorted(myDic.items(), key=operator.itemgetter(0), reverse = True)
#smyDic = sorted(myDic.items(), key=operator.itemgetter(1), reverse = False)
#smyDic = sorted(myDic.items(), key=operator.itemgetter(1), reverse = True)
print('before sort: ', myDic)
print('after sort: ', smyDic)

## List Sort
import operator
myList = [['d', 1], ['a',10], ['b', 14], ['c', 9]]
smyList = sorted(myList, key=operator.itemgetter(0), reverse = False)
#smyList = sorted(myList, key=operator.itemgetter(0), reverse = True)
#smyList = sorted(myList, key=operator.itemgetter(1), reverse = False)
#smyList = sorted(myList, key=operator.itemgetter(1), reverse = True)
print('before sort: ', myList)
print('after sort: ', smyList)

## m x n 2차원 리스트 0으로 초기화 하기
m, n = 5, 3
rooms = [[0 for _ in range(n)] for _ in range(m)]
print(rooms)

## 문자열 뒤집기
name = 'Good Morning'
rname = name[::-1]
print(name)
print(rname)

## 리스트 뒤집기
input = [1,2,3]
input.reverse()
print(input)

## 문자열 정수로 변환하기
sNum = ['1', '2', '3', '4', '5']
iNum = list(map(int, sNum))
print(sNum, iNum)

## 1~10 정수 리스트 생성하기
inumList = [i*2 for i in range(1,11)]
print(inumList)

## 자료구조
myList = [1,2,3]
myTuple = (1,2,3)
myDic = {'a': 5, 'b': 6}
mySet = set()
mySet.add('a')
mySet.add('b')
mySet.add('a')
print(myList, myTuple, myDic, mySet)

## a, b값 설정 및 Swap
a, b = 5, 3    # a = 5, b = 3
a, b = b, a    # a, b의 값을 서로 교체함


#######################################################################################
## 정렬알고리즘(http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html)
#######################################################################################
## Bubble Sort (버블정렬)
# 이웃한 두 값을 비교하여 정렬한다. 큰 값이 오론쪽으로 이동하는 과정이 반복되면서 비교했던 모든 값들의 최댓값이 맨 오른쪽으로 옮겨지게 된다.
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)

## Selection Sort (선택정렬)    <==  Insertion 명칭으로 설명드렸는데, Selection Sort로 명칭 정정합니다.
# 주어진 배열에서 최댓값(최솟값)을 찾아 맨 오른쪽(왼쪽)값과 교체한다.
# 최댓값을 맨 오른쪽으로 보낸다는 점에서 버블정렬과 비슷하지만,
# 이웃한 두 값을 정렬하는 과정이 없기 때문에 대체로 버블정렬보다 빠르다.
# 최댓값을 찾아야 하므로 정렬 상태에 관계없이 언제나 O(n2)이다.
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)
