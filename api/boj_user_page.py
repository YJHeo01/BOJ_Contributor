import requests
from bs4 import BeautifulSoup

def boj_user_data(username):
    boj_url = 'https://www.acmicpc.net/user/{}'.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    boj_response = requests.get(boj_url, headers=headers)
    boj_data = parse_html(boj_response.text)
    ret_value = [username,int(boj_data['made']),int(boj_data['verified']),boj_data['contributed']]
    #print(ret_value)
    return ret_value

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # "만든 문제" 항목의 <th> 태그를 찾고, 그 다음 <td> 태그에서 값을 추출
    made_tag = soup.find('th', text='만든 문제')
    made_value = made_tag.find_next_sibling('td').get_text(strip=True) if made_tag else 0
    
    # "문제를 검수" 항목도 동일한 방식으로 처리
    verified_tag = soup.find('th', text='문제를 검수')
    verified_value = verified_tag.find_next_sibling('td').get_text(strip=True) if verified_tag else 0
    
    tags = ['번역한 문제','오타를 찾음','잘못된 데이터를 찾음','잘못된 조건을 찾음','데이터를 추가','문제를 각색','빠진 조건을 찾음','잘못된 번역을 찾음','데이터를 만듦','어색한 표현을 찾음','스페셜 저지를 만듦','시간 제한을 수정','메모리 제한을 수정','문제를 재창조','스페셜 저지 오류를 찾음','내용을 추가','문제를 다시 작성','입력 형식 오류를 찾음음']
    contributed_value = 0
    for tag in tags:
        contributed_tag = soup.find('th',text=tag)
        tmp = contributed_tag.find_next_sibling('td').get_text(strip=True) if contributed_tag else 0
        if type(tmp) == str: contributed_value += int(tmp)
    
    data = {
        'made': made_value,
        'verified': verified_value,
        'contributed': contributed_value
    }

    return data