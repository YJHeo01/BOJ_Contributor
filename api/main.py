import sys, sqlite3
from datetime import datetime
from api.boj_user_page import boj_user_data
from api.solved_user_page import solved_user_data

def main(username):

    date = datetime.now()
    date = date.isoformat()[:10]

    connection = sqlite3.connect("user_data.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            handle VARCHAR(51) PRIMARY KEY,
            made INTEGER,
            verified INTEGER,
            contributed INTEGER,
            vote INTEGER,
            date CHAR(10)
        )
    ''')

    cursor.execute("SELECT * FROM users WHERE handle = ?", (username,))

    information = cursor.fetchone()

    if information is None:
        # 레코드가 없으면 새로 INSERT
        user_data = boj_user_data(username) + solved_user_data(username)
        mydata = (user_data[0], int(user_data[1]), int(user_data[2]), int(user_data[3]), int(user_data[4]), date)
        cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", mydata)
        connection.commit()

    cursor.execute("SELECT * FROM users WHERE handle = ?", (username,))

    information = cursor.fetchone()
    #print(information[5])
    if information[5] != date:
        user_data = boj_user_data(username) + solved_user_data(username)
        cursor.execute(
            "UPDATE users SET made=?, verified=?, contributed=?, vote=?, date=? WHERE handle=?",
            (int(user_data[1]), int(user_data[2]), int(user_data[3]), int(user_data[4]), date, username)
        )
        connection.commit()

    cursor.execute("SELECT * FROM users WHERE handle = ?", (username,))

    information = cursor.fetchone()

    #print(information)

    connection.close()
    
    return information
    
if __name__ == "__main__":
    main(sys.argv[1])