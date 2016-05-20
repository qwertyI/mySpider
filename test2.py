import requests, sys

reload(sys)
sys.setdefaultencoding('utf-8')

login_url = 'http://192.168.1.88/bugfree/index.php/site/login'
home_url_2 = 'http://192.168.1.88/bugfree/index.php/bug/list/2'

login_cookie = '33_product=d5e0121d62d81c633347eb9cb1dcfb4e8c8e11e9s%3A1%3A%223%22%3B; ' \
               'pageSize=4a634a46b3691d708a05ba276841dd25c535eea8s%3A2%3A%2220%22%3B; ' \
               'PHPSESSID=v3o1i0sl8kmt39misesog43ab2; ' \
               'language=2470c92f0603e5fb7db237fcf3ccbf0cce076868s%3A5%3A%22zh_cn%22%3B'
login_headers = {}
login_headers['Host'] = '192.168.1.88'
login_headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"
login_headers['Referer'] = "http://192.168.1.88/bugfree/index.php/site/login"
login_headers['Cookie'] = login_cookie

login_data = 'LoginForm%5Busername%5D=yuanning&LoginForm%5Bpassword%5D=123456&LoginForm%5Blanguage%5D=zh_cn&LoginForm%5BrememberMe%5D=0'
login_data_dict = {}
login_data_dict['LoginForm[username]']="yuanning"
login_data_dict['LoginForm[password]']="123456"
login_data_dict['LoginForm[language]']="zh_Cn"
login_data_dict['LoginForm[rememberMe]']="0"

login_session = requests.session()
print login_session.cookies.get_dict()
login_session.post(login_url, login_data_dict)
print login_session.cookies.get_dict()
print login_session.get(home_url_2).url

with open('./bugfree.txt', 'wb') as f:
    f.write(requests.get(home_url_2, cookies=login_session.cookies.get_dict()).content.decode('utf-8'))
