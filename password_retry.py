password = input('請輸入密碼: ')
if password == 'a123456':
	print('登入成功!')
i = 3
while password != 'a123456':
	i = i - 1
	print('密碼錯誤! 還有', i ,'次機會')
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!')
		break
	if i < 2:
		break