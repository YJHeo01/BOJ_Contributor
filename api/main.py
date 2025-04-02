import sys, sqlite3, logging
from datetime import datetime
from api.boj_user_page import boj_user_data
from api.solved_user_page import solved_user_data

logger = logging.getLogger(__name__)

def main(username):
    information = (username,0,0,0,0)
    try:
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
            information = (user_data[0], 0, 0, 0, 0, '2000-01-01')
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", information)
            connection.commit()

        #print(information[5])
        if information[5] != date:
            user_data = boj_user_data(username) + solved_user_data(username)
            if min(user_data[1:5]) >= 0:
                cursor.execute(
                    "UPDATE users SET made=?, verified=?, contributed=?, vote=?, date=? WHERE handle=?",
                    (int(user_data[1]), int(user_data[2]), int(user_data[3]), int(user_data[4]), date, username)
                )
                connection.commit()
                information = (username, int(user_data[1]), int(user_data[2]), int(user_data[3]), int(user_data[4]), date)
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        if connection:
            connection.close()

    return information
    
if __name__ == "__main__":
    main(sys.argv[1])