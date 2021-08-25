import pymysql

import config

def getUser() :
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
                select_all_rows = "SELECT * FROM `users`"
                cursor.execute(select_all_rows)
                rowUsers = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowUsers

def getTelegramUser() :
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
                select_all_rows = "SELECT * FROM `telegram_users`"
                cursor.execute(select_all_rows)
                telegram_users = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return telegram_users