password = 'a123456'
i = 3
while i > 0:
	pwd = input('請輸入密碼: ')
	i = i - 1
	if pwd == password:
		print('登入成功! ')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('尚有' , i ,'次機會')
		else:
			print('三次機會已用畢，請稍後再嘗試')