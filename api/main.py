import sys, sqlite3, logging
from datetime import datetime
from api.boj_user_page import boj_user_data
from api.solved_user_page import solved_user_data

logger = logging.getLogger(__name__)

def main(username):
    information = (username,0,0,0,0,'2000-01-01')
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
            information = (username,0,0,0,0,'2000-01-01')
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", information)
            connection.commit()

        if information[5] != date:
            boj_data = boj_user_data(username)
            
            if boj_data['fixedCount'] == -1: return information

            solved_data = solved_user_data(username)
            
            for label in ['solvedCount','voteCount','tier','class']:
                if solved_data[label] < 0: return information
            
            cursor.execute(
                "UPDATE users SET made=?, verified=?, contributed=?, vote=?, date=? WHERE handle=?",
                (int(boj_data['createdCount']), int(boj_data['reviewedCount']), int(boj_data['fixedCount']), solved_data['voteCount'], date, username)
            )
            connection.commit()
            information = (username, int(boj_data['createdCount']), int(boj_data['reviewedCount']), int(boj_data['fixedCount']), solved_data['voteCount'], date)
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