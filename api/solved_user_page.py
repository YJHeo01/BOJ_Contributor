import requests, logging

logger = logging.getLogger(__name__)

def solved_user_data(username):
    url = "https://solved.ac/api/v3/user/show"
    
    querystring = {"handle":username}
    headers = {
        "x-solvedac-language": "",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers,params=querystring)
    if response.status_code == 404: return [0,0,0,0,'0']
    if response.status_code != 200: return [-1,-1,-1,-1,'-1']
    tmp = response.json()
    ret_value = [tmp['solvedCount'],tmp['voteCount'],tmp['tier'],tmp['class'],tmp['classDecoration']]
    return ret_value
