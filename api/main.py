import sys
from api.boj_user_page import boj_user_data
from api.solved_user_page import solved_user_data

def main(username):
    user_data = boj_user_data(username) + solved_user_data(username)
    return user_data
    
if __name__ == "__main__":
    main(sys.argv[1])