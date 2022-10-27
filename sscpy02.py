from cgi import print_arguments


arr = [1, 2, 3 "문자열" ture] # 정수형 쓰다 문자열 부울 선언 가능

# for문 
for i in range(시작값, 끝값+1, 증가값): # for문 기본형태
  print("반복명령문")

  # while문
  while 변수 < 끝값:
    실행명령문
    변수 = 변수 + 증가값
# 추가 
while num == 1:
    print(1)
else:
    print(3) # 윗 문장이 실행 되지 않을때 else문이 출력 

    # 빈 리스트 출력 방법
    arr = []
    arr2 = list()

    append() # 요소의 추가
    arr.append(2)
    print(2)

    len(arr) # 배열의 길이

    # 이중 리스트
    arr = [1, 2, 3, 4], [5, 6, 7, 8]
    print(arr[0]) # [1, 2, 3, 4]
    pritn(arr)[1] # [5, 6, 7, 8]

    arr2 = [1, 2, 3, 4]
    print([0][0]) # 1 출력

    # sort문 오름차순

    arr = [4, 2, -20, -10]
    arr.sort()
    print(sort) #-20, -10, 2, 4

    # reverse 현재 리스트 뒤집기
    arr.reverse()
   
    # remove(x) 요소x 없애기
    arr.remove(x)
   
    # count 요소x의 개수 세기
    arr.count(x)
  
    # insert(인덱스, 값)
    arr.insert()
    
    #index(값) 특정값의 요소 위치
    arr.index()

    # 딕셔너리

    #이름 = key
    #존재 = 값

    #빈 딕셔너리 생성
    phone_book{}

    # 값 불러오기
    print(phoen_book[])

    # 삭제
    print(phone_book.get())
    del phone_book[]