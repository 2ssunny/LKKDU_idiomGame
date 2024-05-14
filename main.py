import random

question_set=["노마십가", "우공이산", "자승자강", "사석위호", "고진감래",
              "수적천석", "괄목상대", "한단지보", "초지일관", "형설지공"] #사자성어 리스트
meaning_set=["둔한말이 열수레를 끈다.", "어리석은 사람이 산을 옮긴다.",
              "자신을 이기는 자가 강한 자다.", "노력이 없으면 아무 일도 이룰 수 없다.",
              "괴로움이 다하면 달콤함이 온다.", "물방울이 떨어져 바위에 구멍을 뚫는다.",
              "눈을 비비고 다시 본다.", "자기를 버리고 타인의 행위를 따라하면 두가지를 모두 놓친다.",
              "처음 품은 뜻을 한결같이 밀고 나간다.", "반딧불과 눈과 함께하는 노력."] #각 사자성어별 뜻

usedNo_list=[] #이미 출제된 문제 번호 저장

correct_times=0 #정답횟수
false_times=0 #오답횟수
correct_items=[] #맞춘 문제 번호 저장
false_items=[] #틀린 문제 번호 저장

while len(usedNo_list)<len(question_set): #사용된 숫자 리스트 크기가 문제 리스트 크기보다 작을 때 반복
  indexNo=random.randint(0,len(question_set)-1) #랜덤으로 문제 번호 선정

  selected_idiom = question_set[indexNo] #선정 문제 저장
  selected_idiom_list = list(selected_idiom) #선정 문제 리스트화
  random.shuffle(selected_idiom_list) #리스트 요소들 순서 섞기
  shuffled_idiom = ''.join(selected_idiom_list) #문자열으로 되돌리기

  if shuffled_idiom==question_set[indexNo]: 
    pass #섞은 후와 원래 문자열이 동일한 경우: 진행하지 않음
  else: #섞은 후와 원래 문자열이 동일하지 않은 경우=제대로 섞인 경우: 계속해서 진행
    try:
      usedNo_list.index(indexNo)==False #사용된 숫자 리스트에서 선정된 숫자 있는지 체크
    
    except(ValueError): #없는 경우 ValueError가 발생하기에, 정상적인 sequnce로 간주하고 진행
      print(len(usedNo_list)+1,"번째 문제")
      print("사자성어의 의미:\n", meaning_set[indexNo])
      print(shuffled_idiom) #문제 출력

      answer=str(input("정답을 입력해 주세요: ")) #정답 입력받기
      usedNo_list.append(indexNo) #정답 입력 받은 후 사용된 번호 리스트에 문제 번호 추가
    
      if answer==question_set[indexNo]: #정답이 맞을 경우
        correct_times=correct_times+1
        correct_items.append(question_set[indexNo]) #정답 횟수를 1 늘리고, 문제 번호 저장
      else: #오답의 경우
        false_times=false_times+1
        false_items.append(question_set[indexNo]) #오답 횟수 1 늘리고, 문제 번호 저장

print("게임이 종료되었습니다.")
print("맞춘 횟수: ",correct_times,"틀린 횟수: ", false_times)
print("맞춘 문제: ", correct_items)
print("틀린 문제: ",false_items) #종료 이후 통계 표시
print("\n Developed in 2024 by Juho \"Andrew\" Lee, all rights reserved.")