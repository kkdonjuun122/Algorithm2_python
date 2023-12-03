## 순차 탐색 알고리즘 응용 예시
def se_serach(n,tg,arr): # 길이, 찾고자 하는 문자열, 배열
    for i in range(n):
        if arr[i] == tg: 
            return i + 1 # 인덱스 반환 , 인덱스는 0부터 시작하니까 +1 하기

arr = ["숫자","테이프","인덱스","복잡도","시간","스탠드"] # 배열 생성
target = "스탠드" # 찾고자 하는 문자열 설정
print("{}번째에서 데이터를 찾았습니다.".format(se_serach(len(arr),target,arr)))