# Answer from teacher #
password = 'a123456'
i = 3
i = int(i)

while True:
	pwd = input('Please enter Password:')
	if pwd == password:
		print('Successfully login...')
		break
	else:
		i = i - 1
		print('You entered a wrong Password, please try again.', i, 'times left.')
		if i == 0:
			print('Please try to reset Password.')
			break