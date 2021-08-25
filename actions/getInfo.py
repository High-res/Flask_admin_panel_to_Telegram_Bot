import pymysql

import config


def getLocation() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `user_location`"
                cursor.execute(select_all_rows)
                rowLocation = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowLocation


def getAvans() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `avans_from_user`"
                cursor.execute(select_all_rows)
                rowAvans = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowAvans


def getZhaloba() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `zhaloba_from_user`"
                cursor.execute(select_all_rows)
                rowZhaloba = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowZhaloba