import pymysql
import config


def getMessages() :
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
                select_all_rows = "SELECT * FROM `message_for_bot`"
                cursor.execute(select_all_rows)
                rowMessages = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowMessages

def deleteMessages(id) :
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
                delete_query = f"DELETE FROM `message_for_bot` WHERE id={id}"
                cursor.execute(delete_query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

def addMesages(message_text, message_date) :
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
                insert_query = "INSERT INTO `message_for_bot` (msg_text, msg_date) VALUES (%s,%s);"
                cursor.execute(insert_query, (message_text, message_date,))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)