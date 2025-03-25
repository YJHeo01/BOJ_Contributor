from data_fetcher import fetch_html
from parser import parse_html

url = 'https://www.acmicpc.net/user/sk14cj'
html_content = fetch_html(url)

if html_content:
    data = parse_html(html_content)
    print("문제 제작 수:", data['made'])
    print("문제 검수 수:", data['verified'])
else:
    print("데이터를 불러오지 못했습니다.")
