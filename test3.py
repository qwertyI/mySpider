import requests, sys

reload(sys)
sys.setdefaultencoding('utf-8')

LOGIN_URL = 'https://testserver.comein.cn/ComeinManager/login'
HOME_URL = 'https://testserver.comein.cn/ComeinManager/'

login_data = {}
login_data['key'] = '888e707a0e5a171a037f82ecaad3d800fd6981233792d4417' \
                    'c2825cf12e11d68e80cd33d50c5ac4d8fd30f6328a52d82f76' \
                    'bb659d9de50eae1b2f3efc240b6fc7c8685c35c1d0fad4582ef' \
                    '2101b99a10e14b740625a32a396ab637dae230ee627d23f97df6' \
                    '587c890c4429674181a546fe06a91ed5ea724f3020bdaea72475e8'
my_cookie = {}
my_cookie['JSESSIONID'] = '27921dda-04ca-4b6e-bb50-6ed1481c5fba'
# my_cookie['rememberMe'] = 'fgiqQiitOcrZLxVsJWftwyiUuahxH03Wvkhb63NI69wRLT4JK3divg8AheLqb0Ryvvl94eUPwMJaN792FFXC1HpQYl50bXJd9DDYaKNqneJIZn+o60jNTjQYoX09TArVG/0lEYXVHgxBhBn6olskBe4DmALrUehWSgUPElXzB5CJ9UIzQcmpUeZUbiaMgeG5urKFRMLoEEu95YqIlEKr/PlVZlc6cQixuW/TiZvQn0iCFU4wPU1G2/YwNm3flL2upvWzmcSHmIfL9qjpyGfv16M9qkS1QSdcpKi7/BNxMXyJHcThmxxdouY1o3JZnLTC9vO3WdmncCYeY3E9ORvq0qp1WZea6CxSDggVQeOZiwU3BWQpi0hb5s33tdSi6b2ZHOoZ7KJf19CyoHNhSvetk5WJsJJuJi0KUiCIw4NlGEr9m++XvAbRS9WXOsZmFQilXtwND8Y8fY7AwtQEKpvpVWrCU/AmCE9xBw1HSMIZrh2sMRxqBNCeau29s84u87x6'

login_session = requests.session()
ls = login_session.post(LOGIN_URL, login_data)
print ls.cookies
print login_session.get(HOME_URL).url
print requests.get(HOME_URL, cookies=ls.cookies).url

with open('./testserver.txt', 'wb') as f:
    f.write(requests.get(HOME_URL, cookies=my_cookie).text.encode('utf-8'))