import flask
import psycopg2
#import config
from app.config import ProductionConfig, TestingConfig
import psycopg2.extras


def get_connection ():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            database=TestingConfig.DB_NAME, host=TestingConfig.DB_HOST,
            user=TestingConfig.DB_USER, password=TestingConfig.DB_PASS)
    return flask.g.dbconn

def get_cursor ():
    return get_connection().cursor(
        cursor_factory=psycopg2.extras.DictCursor)

def query_one (sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return dict(cur.fetchone())

def query_all (sql, **params):
     with get_cursor() as cur:
        cur.execute(sql, params)
        value = []
        for row in cur.fetchall():
            value.append(row)
        index = list(range(0, len(value)))
        print (dict(zip(index, value)))
        return dict(zip(index, value))
        
def insert (sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)

def _rollback_db (sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')

def _commit_db (sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.commit()
        conn.close()
        #delattr(flask.g, 'dbconn')




