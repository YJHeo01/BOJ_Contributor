import requests

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    return response.text
    #print(response)

    if response.status_code == 200:
        html_doc = response.text  # HTML 문서 내용
    else:
        print("웹 페이지를 불러오는 데 실패했습니다.")
