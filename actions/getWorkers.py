import pymysql
import config


def addWorkers(new_worker_name, new_worker_b_day, new_worker_tg_id) :
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
                insert_query = "INSERT INTO `workers` (name, b_day, tg_id) VALUES (%s,%s,%s);"
                cursor.execute(insert_query, (new_worker_name, new_worker_b_day, new_worker_tg_id))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

def getWorkerss() :
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
                select_all_rows = "SELECT * FROM `workers`"
                cursor.execute(select_all_rows)
                workers = cursor.fetchall()
                # for row in workers :
                #     print(row)
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

    return workers

def updateWorker(worker_name, worker_b_day, worker_tg_id) :
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
                update_query = "UPDATE `workers` SET b_day=%s, tg_id=%s WHERE name=%s;"
                cursor.execute(update_query, (worker_b_day, worker_tg_id, worker_name))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

def removeWorkers(worker_id) :
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
                delete_query = "DELETE FROM `workers` WHERE id=%s"
                cursor.execute(delete_query, (worker_id))
                connection.commit()
                print('removed removeWorkers')
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
