import pymysql
from config import *


sql_six_table = "select time,m_tep,m_hum from day order by time DESC"
sql_all_table = "select time,m_tep,m_hum from day order by time ASC"
sql_table_notice = "select distinct time from vul_info order by time DESC"
sql_table_notice_six = "select time,m_tep,m_hum from day where time = %d"
sql_detail = "select time,1_tep,2_tep,3_tep,4_tep,5_tep,6_tep,7_tep,8_tep,9_tep,10_tep,11_tep,12_tep,1_hum,2_hum,3_hum,4_hum,5_hum,6_hum,7_hum,8_hum,9_hum,10_hum,11_hum,12_hum,h_tep,m_tep,l_tep,h_hum,m_hum,l_hum from day where time = %d"
connect = pymysql.connect(

    host = MYSQL_HOST,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    passwd = MYSQL_PASSWD,
    db = MYSQL_DBNAME,
    charset = MYSQL_CHARSET
)

def time_deal(date):

    year_date = date[:4]
    mon_date = date[4:6]
    day_date = date[6:8]
    reg_date = year_date + "-" + mon_date + "-" + day_date
    return reg_date

def time_deal_int(date):

    year_date = date[:4]
    mon_date = date[5:7]
    day_date = date[8:10]
    reg_date = year_date + mon_date + day_date
    return int(reg_date)

def select_all_data():

    table_all = []
    cursor = connect.cursor()
    cursor.execute(sql_all_table)
    result = cursor.fetchall()
    for i in result:
        data_list = list(i)
        data_time = time_deal(str(i[0]))
        data_list.append(data_time)
        table_all.append(data_list)
    return table_all

def select_table_six():

    table_six = []
    cursor = connect.cursor()
    cursor.execute(sql_six_table)
    result = cursor.fetchall()
    for i in range(6):
        data_list = list(result[i])
        data_time = time_deal(str(data_list[0]))
        data_list.append(data_time)
        table_six.append(data_list)
    return table_six


def select_table_notice():

    time_list = []
    cursor = connect.cursor()
    cursor.execute(sql_table_notice)
    result = cursor.fetchall()
    for i in range(6):
        data_list = list(result[i])
        data_time = time_deal_int(data_list[0])
        time_list.append(data_time)
    return time_list

def select_table_notice_six(time_list):

    table_all = []
    for i in time_list:
        sql = sql_table_notice_six % i
        cursor = connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            data_list = list(i)
            data_time = time_deal(str(i[0]))
            data_list.append(data_time)
            table_all.append(data_list)
    return table_all

def data_find(time):

    sql = sql_detail % time
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    result_list = list(result)
    time_data = time_deal(str(result_list[0]))
    tem_list = result_list[1:13]
    hum_list = result_list[13:25]
    return time_data,tem_list,hum_list



