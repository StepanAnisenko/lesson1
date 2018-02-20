def get_answer(question,answer):
	return answer[question]
quest=input()
ans={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
result=get_answer(quest,ans)
print(result)
