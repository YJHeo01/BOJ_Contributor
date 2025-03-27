import requests

def solved_user_data(username):
    url = "https://solved.ac/api/v3/user/show"
    
    querystring = {"handle":username}
    headers = {
        "x-solvedac-language": "",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers,params=querystring)
    
    return [response.json()['voteCount']]