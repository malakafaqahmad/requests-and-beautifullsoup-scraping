import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

payload = {
    'username': 'your_credentials',
    'password': 'your_credentials',
    'Action': 'Login'
}




def set_sessions(login_url, secure_url):
    with requests.session() as session:
        session.post(login_url, data=payload, headers=headers)
        response = session.get(secure_url, headers=headers)
        return response

def __getsoup(response):
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.title)






if __name__ == '__main__':
    print('welcome to ucx_6 scrapper')
    print('wait while we fetch you some results!!!')

    # Specify the URL you want to scrape
    login_url = ('')
    secure_url = ('')

    response = set_sessions(login_url, secure_url)
    soup = __getsoup(response)
