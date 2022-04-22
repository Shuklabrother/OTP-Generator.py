import random
generatorotp = random.randint(000000, 100000)
username = input('username:')
print('Hello', username)
print('OTP:', generatorotp)
password = input('Write password')
if password == str(generatorotp):
	print("Login success")
	
else:
	password != str(generatorotp)
	print("Login failed")