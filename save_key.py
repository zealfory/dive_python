# -*- encoding: utf-8 -*-
# @File:   save_key.py    
# @Time: 2020-05-20 15:15
# @Author: ZHANG
# @Description: 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

import pymysql
import string
import random

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return string.ascii_letters + string.digits


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(str(key_gen()))
    return result


class mysql_init(object):

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="123456",
            db="test",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, pymysql.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryData(conn)
    dbconn.commit()
    dbconn.close()


def query(sql, conn):
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS user_key")


def CreateTable(conn):
    sql_create = '''CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)


def InsertDatas(conn):
    insert_sql = "INSERT INTO user_key values (%(value)s)"  # ??
    key_list = key_num(KEY_ALL)
    conn.executemany(insert_sql, [dict(value=v) for v in key_list])


def DeleteData(conn):
    del_sql = "DELETE FROM user_key where id=2"
    conn.execute(del_sql)


def QueryData(conn):
    sql = "SELECT * FROM user_key"
    rows = query(sql, conn)
    printResult(rows)


def printResult(rows):
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)


if __name__ == "__main__":
    dbconn = mysql_init()
    process()


