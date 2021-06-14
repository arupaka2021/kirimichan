import psycopg2, os, sys
from psycopg2.extras import DictCursor

class dmy:

    conn = None     # コネクション用クラス変数

    def __init__(self):

        PGHOST = '127.0.0.1'
        PGUSER = 'postgres'
        PGNAME = 'postgres'

        try:
            self.conn = psycopg2.connect('dbname={dbname} host={host} user={user}'.format(dbname=PGNAME, host=PGHOST, user=PGUSER))

        except Exception:
            self.conn = None


def main():

    db = dmy()

    sql = "SELECT id, lname, fname FROM dmy LIMIT 3"

    cur = db.conn.cursor(cursor_factory=DictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()

    for r in rows:
        print('{}: {} {}'.format(r['id'], r['lname'], r['fname']))


if __name__ == '__main__':
    main()
