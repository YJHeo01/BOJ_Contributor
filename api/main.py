import sys, sqlite3, logging
from datetime import datetime
from api.boj_user_page import boj_user_data
from api.solved_user_page import solved_user_data

logger = logging.getLogger(__name__)

def main(username):
    ret_value = {
        'handle':username,
        'solvedCount': '0',
        'createdCount':'0',
        'reviewedCount':0,
        'fixedCount':0,
        'voteCount':0,
        'tier': 0,
        'class':0  
    }
    try:
        date = datetime.now()
        date = date.isoformat()[:10]

        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                handle VARCHAR(51) PRIMARY KEY,
                solvedCount INTEGER,
                createdCount VARCHAR(7),
                reviewedCount VARCHAR(7),
                fixedCount INTEGER,
                voteCount INTEGER,
                tier INTEGER,
                class INTEGER,
                date CHAR(10)
            )
        ''')

        cursor.execute("SELECT * FROM users WHERE handle = ?", (username,))

        stats = cursor.fetchone()

        if stats is None:
            stats = (username, 0, '0', '0', 0, 0, 0, 0, '2000-01-01')
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?)", stats)
            connection.commit()
        
        if stats[8] != date:
            boj_data = boj_user_data(username)
            
            if boj_data['fixedCount'] == -1: return stats

            solved_data = solved_user_data(username)
            
            for label in ['solvedCount','voteCount','tier','class']:
                if solved_data[label] < 0: return stats
            
            cursor.execute(
                "UPDATE users SET createdCount=?, reviewedCount=?, fixedCount=?, voteCount=?, date=? WHERE handle=?",
                (boj_data['createdCount'], boj_data['reviewedCount'], boj_data['fixedCount'], solved_data['voteCount'], date, username)
            )
            connection.commit()
        ret_value = convert_data(stats)
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        if connection:
            connection.close()

    return ret_value

def convert_data(data):
    ret_value = {}
    labels = ['handle','solvedCount','createdCount','reviewedCount','fixedCount','voteCount','tier','class']
    for i in range(8):
        ret_value[labels[i]] = data[i]
    return ret_value
    
if __name__ == "__main__":
    main(sys.argv[1])