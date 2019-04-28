import pymysql
import time
from config import *


sql_six_table = "select date,admin,happen,temper,mosi,time from vul_info order by date DESC,time DESC"
sql_all_table = "select date,admin,happen,temper,mosi,time from vul_info order by date ASC,time ASC"

connect = pymysql.connect(

    host = MYSQL_HOST,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    passwd = MYSQL_PASSWD,
    db = MYSQL_DBNAME,
    charset = MYSQL_CHARSET
)


def judge(happen):

    if happen == 1:
        zn_happen = "温度异常"
    if happen == 2:
        zn_happen = "湿度异常"
    if happen == 3:
        zn_happen = "温湿度异常"
    return zn_happen

def select_six_notice():

    table_six = []
    cursor = connect.cursor()
    cursor.execute(sql_six_table)
    result = cursor.fetchall()
    for i in range(6):
        data_list = list(result[i])
        zn_happen = judge(data_list[2])
        data_list[2] = zn_happen
        table_six.append(data_list)
    return table_six


def select_all_notice():

    time_list = []
    cursor = connect.cursor()
    cursor.execute(sql_all_table)
    result = cursor.fetchall()
    for i in result:
        data_list = list(i)
        zn_happen = judge(data_list[2])
        data_list[2] = zn_happen
        time_list.append(data_list)
    return time_list


