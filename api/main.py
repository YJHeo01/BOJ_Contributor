import sys
from api.boj_user import boj_user_data

def main(username):
    user_data = boj_user_data(username) 
    return sum(user_data)
    
if __name__ == "__main__":
    main(sys.argv[1])