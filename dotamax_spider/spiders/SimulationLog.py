import requests
from bs4 import BeautifulSoup as bs

login_url = 'https://testerhome.com/account/sign_in'

print requests.get('https://testerhome.com/qwerty').url
def get_rucaptcha():
    with open('./rucaptcha', 'wb') as f:
        f.write(requests.get(bs_response.img['src']).content)

response = ''
rucaptcha = '1'
while rucaptcha == '1':
    response = requests.get(login_url).text
    bs_response = bs(response)
    get_rucaptcha()
    rucaptcha = raw_input('please enter rucaptcha:')

token = ''
utf8 = ''

print bs_response.find_all('input')
for i in bs_response.find_all('input'):
    if i['name'] == 'authenticity_token':
        token = i['value']
    if i['name'] == 'utf8':
        utf8 = i['value']


login_data = {}
login_data['utf8'] = utf8
login_data['authenticity_token'] = token
login_data['user[login]'] = '727665171@qq.com'
login_data['user[password]'] = '15949552135'
login_data['_rucaptcha'] = rucaptcha
login_data['user[remember_me]'] = '0'
login_data['commit'] = 'Sign+In'
print login_data

login_session = requests.session()
login_session.post(login_url, login_data)
print login_session.cookies.get_dict()
with open('./loginresult', 'wb') as f:
    f.write(requests.get('https://testerhome.com', cookies={'_ga':'GA1.2.356904179.1461145765'}).content)


