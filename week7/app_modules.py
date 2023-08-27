from flask import Flask, Blueprint, current_app
import mysql.connector

from api import blueprint

def create_app():
    app = Flask(__name__, static_folder = "public", static_url_path = "/")
    app.debug = True
    app.threaded = True
    app.secret_key = "I wanna be"
    register_blue(app)
    return app

def register_blue(app):
    app.register_blueprint(blueprint)

# get pool
def create_connection_pool():
    db_config = {
        "host" : "localhost",
        "username" : "root",
        "password" : "12345678",
        "database" : "website",
    }
    db_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "my_pool", pool_size = 10, **db_config)
    return db_pool

# get connection
def get_connection_from_pool(db_pool):
    db_connection = db_pool.get_connection()
    return db_connection

# get cursor
def get_cursor(db_connection):
    db_cursor = db_connection.cursor(dictionary = True)
    return db_cursor

# decorator of CRUD
def preprocessing(func):
    def wrapper(paras):
        db_pool = current_app.config['connection_pool']
        db_connection = get_connection_from_pool(db_pool)
        db_cursor = get_cursor(db_connection)
        command = combine_query(func.__name__, paras)
        try:
            return func(db_connection, db_cursor, command, paras.get('target'))
        except Exception as err:
            print(err)
        finally:
            db_cursor.close()
            db_connection.close()
    return wrapper

# process control of combine query 
def combine_query(func_name, paras):
    if func_name == "query_create":
        return combine_create_query(paras)
    if func_name == "query_fetch_one" or func_name == "query_fetch_all":
        return combine_read_query(paras)
    if func_name == "query_update":
        return combine_update_query(paras)
    if func_name == "query_del":
        return combine_delete_query(paras)

# query combine create
def combine_create_query(paras):
    res = "INSERT INTO"
    if paras.get("table"):
        res += f" {paras['table']} ( {paras['columns']} )"
    if paras.get("values"):
        res += f" VALUES ( {paras['values']} )"
    return res

# query combine read
def combine_read_query(paras):
    res = "SELECT"
    if paras.get("columns"):
        res += f" {paras['columns']}"
    if paras.get("table"):
        res += f" FROM {paras['table']}"
    if paras.get("where"):
        res += f" WHERE {paras['where']}"
    if paras.get("order"):
        res += f" ORDER BY {paras['order']}"
    if paras.get("order_ordered"):
        res += f" {paras['order_ordered']}"
    if paras.get("limit"):
        res += f" LIMIT {paras['limit']}"
    return res

# query combine update
def combine_update_query(paras):
    res = "UPDATE"
    if paras.get("table"):
        res += f" {paras['table']}"
    if paras.get("set"):
        res += f" SET {paras['set']}"
    if paras.get("where"):
        res += f" WHERE {paras['where']}"
    return res

# query combine delete
def combine_delete_query(paras):
    res = "DELETE"
    if paras.get("table"):
        res += f" FROM {paras['table']}"
    if paras.get("where"):
        res += f" WHERE {paras['where']}"
    return res

# C
@preprocessing
def query_create(db_connection, db_cursor, command, target) -> bool:
    db_cursor.execute(command, target)
    db_connection.commit()
    return True

# R_fetch_one
@preprocessing
def query_fetch_one(db_connection, db_cursor, command, target) -> dict:
    db_cursor.execute(command, target)
    return db_cursor.fetchone()


# R_fetch_all
@preprocessing
def query_fetch_all(db_connection, db_cursor, command, target) -> dict:
    db_cursor.execute(command, target)
    return db_cursor.fetchall()

# U
@preprocessing
def query_update(db_connection, db_cursor, command, target) -> bool:
    db_cursor.execute(command, target)
    db_connection.commit()
    return True

# D
@preprocessing
def query_del(db_connection, db_cursor, command, target) -> bool:
    db_cursor.execute(command, target)
    db_connection.commit()
    return True