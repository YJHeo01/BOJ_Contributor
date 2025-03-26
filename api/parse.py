from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # "만든 문제" 항목의 <th> 태그를 찾고, 그 다음 <td> 태그에서 값을 추출
    made_tag = soup.find('th', text='만든 문제')
    made_value = made_tag.find_next_sibling('td').get_text(strip=True) if made_tag else 0
    
    # "문제를 검수" 항목도 동일한 방식으로 처리
    verified_tag = soup.find('th', text='문제를 검수')
    verified_value = verified_tag.find_next_sibling('td').get_text(strip=True) if verified_tag else 0
    
    fix_value = 0
    
    data = {
        'made': made_value,
        'verified': verified_value,
        'fixed': fix_value
    }

    return data