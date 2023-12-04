#김명헌, 권주은, 김성진, 김두영, 김수겸, 김동준
#순차탐색 응용 프로그램
#이름이 key인 data 예제
data = [('홍길동', 21, '컴퓨터공학과', '대전'),
        ('김철수', 23, '심리학과', '서울'),
        ('이순신', 22, '경제학과', '부산'),
        ('박하나', 20, '응용소프트웨어공학과', '세종'),
        ('김민수', 24, '멀티미디어학과','수원')]

def sequential_search(A,  key): #A[i][0]에서 key를 순차탐색
    for i in range(len(A)):
        if A[i][0] == key: #A[i][0]에 이름이 있음
            return i #key를 찾는 경우 index 반환
    return -1 #key가 없는 경우

#예제
while True:
    key=input("--->") #key를 키보드에서 직접 입력하여 순차탐색
    k = sequential_search(data, key)
    if k >= 0: #key에 레코드가 있는 경우
        print(f"{key}의 레코드 : {data[k]}")
    else: #key에 레코드가 없는 경우
        print(f"{key}가 data에 없습니다.")
        break #없는 경우에는 반복문 종

