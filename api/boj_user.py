import requests
import api.parse as parse

def boj_user_data(username):
    boj_url = 'https://www.acmicpc.net/user/{}'.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    boj_response = requests.get(boj_url, headers=headers)
    boj_data = parse.parse_html(boj_response.text)
    ret_value = [int(boj_data['made']),int(boj_data['verified']),boj_data['fixed']]
    print(ret_value)
    return ret_value