# 행맨 게임(영어 단어 퀴즈) 프로그램 만들기

# 추가한 모듈
from random import randrange
import pandas as pd

# 단어 리스트 및 양 (전역 변수)

global df, out, np

# 파일 경로 설정 (다른 컴퓨터에 사용할 경우 경로를 바꿀 것)
# pd.read_excel('경로명\파일명', sheet_name='', usecols= ["영단어", "뜻"])
df = pd.read_excel('C:\\내 파일\\github private\\Python-Project\\hangman_word.xlsx', sheet_name='Sheet0', usecols=['영단어', '뜻'])
out = list(df)
np = pd.DataFrame.to_numpy(df)

global word_list, TotalWord, Life
word_list = [] # 단어 추가 및 수정 가능
for i in range( 8498 - 1 ):
    word_list.append(np[i][0]) # 엑셀에 있는 단어(8498개) 추가
TotalWord = len(word_list)
Life = 6


# 단어 선정 함수
def word_choice():
    WordChosen = randrange(TotalWord)
    return word_list[WordChosen]


# main 실행
word_answer = word_choice()
word_board = '_ ' * len(word_answer)

# 시작 문자열 출력
print("ANSWER: ", word_answer)
print(word_board)

while 1:
    IsExist = 0 # 단어 존재 여부
    OfferedLetter = input("Input letter > ")

    # 단어(문자열)를 리스트로 치환
    word_board_list = list(word_board)

    # 입력한 문자가 정답에 있는지 확인
    for i in range(len(word_answer)):
        if OfferedLetter == word_answer[i]:
            word_board_list[2 * i] = OfferedLetter
            IsExist = 1

    # 리스트를 문자열로 환원
    word_board = ''.join(s for s in word_board_list)

    # 현재 풀이 현황 출력
    print(word_board)

    # 문자가 포함되지 않은 경우
    if IsExist == 0:
        Life = Life - 1
        print("Wrong  남은 시도 횟수: ", Life)

    # 게임 종료 조건
    if Life == 0:
        break

    if '_' not in word_board:
        break

    # 문자가 포함된 경우
    if IsExist == 1:
        print("Correct")



    print() # 공백

# 정답을 맞춘 경우 출력
if IsExist > 0:
    print("SUCCESS")

# 정답 출력
print("word:", word_answer)