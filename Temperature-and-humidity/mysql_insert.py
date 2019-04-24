import pymysql
from config import *
import time
import numpy as np

sql_time = "insert into vul_info(date,admin,happen,temper,mosi,time) values ('%s','%s',%d,%d,%d,'%s')"
sql_test = "insert into day(time,1_tep,2_tep,3_tep,4_tep,5_tep,6_tep,7_tep,8_tep,9_tep,10_tep,11_tep,12_tep,1_hum,2_hum,3_hum,4_hum,5_hum,6_hum,7_hum,8_hum,9_hum,10_hum,11_hum,12_hum,h_tep,m_tep,l_tep,h_hum,m_hum,l_hum) values (%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%f,%d,%d,%f,%d)"

connect = pymysql.connect(

    host = MYSQL_HOST,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    passwd = MYSQL_PASSWD,
    db = MYSQL_DBNAME,
    charset = MYSQL_CHARSET
)

def insert_data(test):

    sql_insert = sql_test % (
    test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7], test[8], test[9], test[10], test[11],
    test[12], test[13], test[14], test[15], test[16], test[17], test[18], test[19], test[20], test[21], test[22],
    test[23], test[24], test[25], test[26], test[27], test[28], test[29], test[30])
    cursor = connect.cursor()
    try:
        cursor.execute(sql_insert)
        connect.commit()
    except Exception as e:
        connect.rollback()
        print(e)

def deal_data(data_list):

    max_data = max(data_list)
    min_data = min(data_list)
    ave_data = np.mean(data_list)
    ave_data = round(ave_data,2)
    data_list.append(max_data)
    data_list.append(ave_data)
    data_list.append(min_data)
    return data_list


def unite_data(datatime,tem_list,hum_list):

    unite_list = []
    unite_list.append(datatime)
    for i in range(len(tem_list)-3):
        unite_list.append(tem_list[i])
    for i in range(len(hum_list)-3):
        unite_list.append(hum_list[i])
    for i in range(len(tem_list)-3,len(tem_list)):
        unite_list.append(tem_list[i])
    for i in range(len(hum_list)-3,len(hum_list)):
        unite_list.append(hum_list[i])
    return unite_list



def vul_data(tem_data,hum_data):

    vul_list = []
    admin = "admin"
    happen = 0
    day_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    accurate_time = time.strftime('%H:%M:%S', time.localtime(time.time()))

    if tem_data >= 70 and hum_data >= 20:
        happen = 1
    if tem_data <= 70 and hum_data <= 20:
        happen = 2
    if tem_data >= 70 and hum_data <= 20:
        happen = 3
    vul_list.append(day_time)
    vul_list.append(admin)
    vul_list.append(happen)
    vul_list.append(tem_data)
    vul_list.append(hum_data)
    vul_list.append(accurate_time)
    return vul_list

def insert_vul(vul_list):

    if vul_list[2] != 0:
        sql_insert_time = sql_time % (vul_list[0],vul_list[1],vul_list[2],vul_list[3],vul_list[4],vul_list[5])
        cursor = connect.cursor()
        try:
            print("******************** Warning !!! ***********************")
            cursor.execute(sql_insert_time)
            connect.commit()
        except Exception as e:
            connect.rollback()
            print(e)
    else:
        pass






