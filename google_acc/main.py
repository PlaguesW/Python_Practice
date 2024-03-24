from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from smsactivateru import Sms, SmsTypes, SmsService, GetBalance, GetFreeSlots, GetNumber
import requests
import time
import random
import string

profile = open('profile_id.txt', 'r')
lines = profile.readlines()
profile_id = lines[0].strip()
print('ID profile: %s' % (profile_id))
profile.close()

profile = open('profile_id.txt', 'w')
profile.writelines(lines[1:])
profile.close()

#TODO replace with existing profile ID. Define the ID of the browser profile, where the code will be executed.
mla_profile_id = str(profile_id)

mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id

"""
Send GET request to start the browser profile by profileId. Returns response in the following format: '{"status":"OK","value":"http://127.0.0.1:XXXXX"}', where XXXXX is the localhost port on which browser profile is launched. Please make sure that you have Multilogin listening port set to 35000. Otherwise please change the port value in the url string
"""
resp = requests.get(mla_url)

json = resp.json()

#Define DesiredCapabilities
opts = options.DesiredCapabilities()

#Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})

#Perform automation
driver.get('https://google.com/')
#assert "Multilogin - Replace Multiple Computers With Virtual Browser Profiles - Multilogin" in driver.title

time.sleep(5)


#Click the link which opens in a new window
driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a').click()

time.sleep(5)

#Click the link which opens in a new window
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span').click()

time.sleep(5)

#Click the link which opens in a new window
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[2]').click()

time.sleep(5)

login_first = driver.find_element(By.XPATH, '//*[@id="firstName"]')
login_second = driver.find_element(By.XPATH, '//*[@id="lastName"]')
gmail_login = driver.find_element(By.XPATH, '//*[@id="username"]')
passwd = driver.find_element(By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input')
pass_repeat = driver.find_element(By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


login_first_rand =  generate_random_string(6)
login_second_rand = generate_random_string(8)
gmail_login_rand = generate_random_string(12)

#Read file string
print(gmail_login_rand + '@gmail.com')


#####Вводим логин и пароль#####
delay = 3
login_first.send_keys(login_first_rand) # GG First name
delay = 4
login_second.send_keys(login_second_rand) # GG Last name
delay = 2
gmail_login.send_keys(gmail_login_rand) # GG login name
delay = 4
passwd.send_keys("Passwww1222") #Password
delay = 3
pass_repeat.send_keys("Passwww1222") #Password repeat

#Click the link which opens in a new window
driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]/div/button/span').click()

time.sleep(10)

#####Получаем смс#####
wrapper = Sms('API_KEY_SMSACTIVATE')

# try get phone for Google
activation = GetNumber(
	service=SmsService().Google,
	country=SmsTypes.Country.NL,
	operator=SmsTypes.Operator.any
).request(wrapper)

# show activation id and phone for reception sms
print('id: {} phone: {}'.format(str(activation.id), str(activation.phone_number)))


phone_activ = str(activation.phone_number)
time.sleep(10)

phone = driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]')
delay = 3
phone.send_keys('+' + phone_activ) # GG phone activ
delay = 3
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

# set current activation status as SmsSent (code was sent to phone)
activation.was_sent()

# .. wait code
code = activation.wait_code(wrapper=wrapper, not_end=True)

print('Тест кода: ' + code)


#####Вводим код#####
time.sleep(10)

code_enter = driver.find_element(By.XPATH, '//*[@id="code"]')
delay = 3
code_enter.send_keys(code) # GG code activ
delay = 3
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span').click()

# .. and wait one mode code
# (!) if you not set not_end (or set False) – activation ended before return code
#activation.wait_code(callback=fuck_yeah, wrapper=wrapper)
#####Получаем смс#####


#####Возраст и пол#####
time.sleep(10)

select = Select(driver.find_element(By.XPATH,'//*[@id="month"]'))
# select by value
select.select_by_value('4')

day_enter = driver.find_element(By.XPATH, '//*[@id="day"]')
delay = 3
day_enter.send_keys('14') # GG code activ
delay = 3

year_enter = driver.find_element(By.XPATH, '//*[@id="year"]')
delay = 3
year_enter.send_keys('1960') # GG code activ
delay = 3

gender_enter = Select(driver.find_element(By.XPATH, '//*[@id="gender"]'))
delay = 3
gender_enter.select_by_value('2') # GG code activ
delay = 3
print('Возраст заполнен')
delay = 3
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span').click()
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

print('Регистрация завершена')
#Save email login
email = open('email.txt', 'a')
email.writelines(gmail_login_rand + '@gmail.com\n')
email.close

#profile = open('profile_id.txt', 'w')
#profile.writelines(lines[1:])
#profile.close