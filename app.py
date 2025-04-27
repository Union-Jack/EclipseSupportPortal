import os
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        connection = sqlite3.connect('EclipseSupportPortal.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id INTEGER PRIMARY KEY, forname TEXT)''')

        cursor.execute('''INSERT OR IGNORE INTO users VALUES
                (1, 'Jack')''')

        connection.commit()        
        
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        results_string = "\n".join(str(row) for row in results)
        return results_string

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug = True, host="0.0.0.0", port=port)


