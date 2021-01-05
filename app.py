import datetime
import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def index():
    # Connect to database
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all GET requests
    sql_all = """SELECT COUNT(*) FROM weblogs;"""
    cur.execute(sql_all)
    all = cur.fetchone()[0]

    # Get number of all succesful requests
# and source = local vs remote
# 
    localsql_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source = 'local';"""
    cur.execute(localsql_success)
    localsuccess = cur.fetchone()[0]

    remotesql_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source = 'remote';"""
    cur.execute(remotesql_success)
    remotesuccess = cur.fetchone()[0]

    # Determine rate if there was at least one request
    rate = "No entries yet!"
    if all != 0:
        localrate = str(localsuccess / all)
        remoterate = str(remotesuccess / all)

    return render_template('index.html', localrate = localrate, remoterate = remoterate)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
