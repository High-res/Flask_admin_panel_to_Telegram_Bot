import pymysql
import config


def addChallenge(challenge, yes, no, answerYes, answerNo, send_time_1, date) :
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
            # insert добавить пользователей 
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `bot_challenges` (challenge, yes, no, answerYes, answerNo, send_time_1, date) VALUES (%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(insert_query, (challenge, yes, no, answerYes, answerNo, send_time_1, date))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

def getChallenge() :
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
                select_all_rows = "SELECT * FROM `bot_challenges`"
                cursor.execute(select_all_rows)
                rowChallenge = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowChallenge


def removeChallenge(id) :
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
                delete_query = f"DELETE FROM `bot_challenges` WHERE id={id}"
                cursor.execute(delete_query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

        
def getChallengeAction() :
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
                select_all_rows = "SELECT * FROM `bot_challenges_actions`"
                cursor.execute(select_all_rows)
                rowAction = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowAction

def updateChalenges(challenge, yes, no, answerYes, answerNo, send_time_1, id) :
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
                update_query = "UPDATE `bot_challenges` SET challenge=%s, yes=%s, no=%s, answerYes=%s, answerNo=%s, send_time_1=%s  WHERE id=%s;"
                cursor.execute(update_query, (challenge, yes, no, answerYes, answerNo, send_time_1, id))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)