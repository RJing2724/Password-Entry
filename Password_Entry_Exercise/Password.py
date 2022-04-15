# Password entry Exercise #
Password = input('Please enter Password:')

i = 3 # 3 times are given to enter password
i = int(i)

if Password == 'a123456':
	print('Successfully login...')

while Password != 'a123456':
	i = i - 1
	if i >= 0:
		print('You entered a wrong Password, please try again.', i, 'times left.')
		Password = input('Please enter Password:')
	else:
		print('Please try to reset Password.')
		break
