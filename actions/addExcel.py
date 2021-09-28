import pandas as pd
import numpy as np
from datetime import date, timedelta
import actions


def thisMonth() :
    today = date.today()
    day = today.strftime('%Y-%m')
    return day

def lastMonth() :
    today = date.today()
    first = today.replace(day=1)
    lastMonth = first - timedelta(days=1)
    day = lastMonth.strftime("%Y-%m")
    return day

def toXlsxThisMonth() :
    WorkerName = []
    WorkerInJob = []
    Worker2Gis = []
    WorkerSendDate = []
    workers = actions.getWorkerss()
    locations = actions.getLocation()
    for worker in workers :
        for location in locations :
            if thisMonth() == location['date_today'] :
                if location['user_tg_id'] == worker['tg_id'] :
                    WorkerName.append(worker['name'])
                    if str(location['location_longitude']) > str(76.900000) and str(location['location_longitude']) < str(76.913000) and str(location['location_latitude']) < str(43.286000) and str(location['location_latitude']) > str(43.284000) :
                        WorkerInJob.append('Да')
                    else :
                        WorkerInJob.append('Нет')
                    Worker2Gis.append('https://2gis.kz/almaty?m='+location['location_longitude']+ '%2C'+location['location_latitude']+'%2F19.35')
                    WorkerSendDate.append(location['send_date'])
    workersss = np.array([WorkerName, WorkerInJob, Worker2Gis, WorkerSendDate])

    dataset = pd.DataFrame()
    dataset['Имя работника'] = workersss[0].tolist()
    dataset['Возле работы? Да/Нет'] = workersss[1].tolist()
    dataset['Ссылка на карту'] = workersss[2].tolist()
    dataset['Дата/время получения получения'] = workersss[3].tolist()
    print('Вывели xlsx')
    dataset.to_excel('./static/teams.xlsx', index=False)

def toXlsxLastMonth() :
    WorkerName = []
    WorkerInJob = []
    Worker2Gis = []
    WorkerSendDate = []
    workers = actions.getWorkerss()
    locations = actions.getLocation()
    for worker in workers :
        for location in locations :
            if lastMonth() == location['date_today'] :
                if location['user_tg_id'] == worker['tg_id'] :
                    WorkerName.append(worker['name'])
                    if str(location['location_longitude']) > str(76.900000) and str(location['location_longitude']) < str(76.913000) and str(location['location_latitude']) < str(43.286000) and str(location['location_latitude']) > str(43.284000) :
                        WorkerInJob.append('Да')
                    else :
                        WorkerInJob.append('Нет')
                    Worker2Gis.append('https://2gis.kz/almaty?m='+location['location_longitude']+ '%2C'+location['location_latitude']+'%2F19.35')
                    WorkerSendDate.append(location['send_date'])
    workersss = np.array([WorkerName, WorkerInJob, Worker2Gis, WorkerSendDate])

    dataset = pd.DataFrame()
    dataset['Имя работника'] = workersss[0].tolist()
    dataset['Возле работы? Да/Нет'] = workersss[1].tolist()
    dataset['Ссылка на карту'] = workersss[2].tolist()
    dataset['Дата/время получения получения'] = workersss[3].tolist()
    print('Вывели xlsx')
    dataset.to_excel('./static/last.xlsx', index=False)

