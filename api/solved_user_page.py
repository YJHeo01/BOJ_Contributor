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
    
    ret_value = {
        'solvedCount': 0,
        'voteCount': 0,
        'tier': 0,
        'class': 0
    }
    
    labels = ['solvedCount','voteCount','tier','class']
    
    if response.status_code == 200:
        information = response.json()
        for label in labels:
            ret_value[label] = information[label]
        ret_value['class'] *= 3
        if information['classDecoration'] == "silver": ret_value['class'] += 1
        if information['classDecoration'] == "gold": ret_value['class'] += 2
    else:
        if response.status_code != 404:
            for label in labels:
                ret_value[label] = -1
    return ret_value
