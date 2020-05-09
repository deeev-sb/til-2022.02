# 시공의 폭풍 속으로 (Level 1)

def choice(team, my):
	selectable = 0
	for i in my:
		if i not in team:
			selectable += 1
	return selectable

team_choice = list(map(int, input().split()))
my_choice = list(map(int, input().split()))
print(choice(team_choice, my_choice))

