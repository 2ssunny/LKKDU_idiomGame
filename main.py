import random

correct_times=0
false_times=0
usedNo_list=[]

correct_items=[]
false_items=[]

while len(usedNo_list)<8:
  question_set=["노마십가", "우공이산", "자승자강", "사석위호",
                "수적천석", "괄목상대", "한단지보", "형설지공"]
  meaning_set=["둔한말이 열수레를 끈다.", "어리석은 사람이 산을 옮긴다.",
              "자신을 이기는 자가 강한 자다.", "노력이 없으면 아무 일도 이룰 수 없다.",
              "물방울이 떨어져 바위에 구멍을 뚫는다.", "눈을 비비고 다시 본다.",
              "자기를 버리고 타인의 행위를 따라하면 두가지를 모두 놓친다.", "반딧불과 눈과 함께하는 노력."]

  indexNo=random.randint(0,7)

  selected_idiom = question_set[indexNo]
  selected_idiom_list = list(selected_idiom)
  random.shuffle(selected_idiom_list)
  shuffled_idiom = ''.join(selected_idiom_list)

  if shuffled_idiom==question_set[indexNo]:
    pass
  else:
    try:
      usedNo_list.index(indexNo)==False
      
    except(ValueError):
      print(len(usedNo_list)+1,"번째 문제")
      print("사자성어의 의미:\n", meaning_set[indexNo])
      print(shuffled_idiom)

      answer=str(input("정답을 입력해 주세요: "))
      usedNo_list.append(indexNo)
      
      if answer==question_set[indexNo]:
        correct_times=correct_times+1
        correct_items.append(question_set[indexNo])
      else:
        false_times=false_times+1
        false_items.append(question_set[indexNo])


print("게임이 종료되었습니다.")
print("맞춘 횟수: ",correct_times,"틀린 횟수: ", false_times)
print("맞춘 문제: ", correct_items)
print("틀린 문제: ",false_items)