# import cors cookie-parser
from flask import Flask, g, redirect, render_template, request, session, url_for
import time
from datetime import datetime

from datetime import date
import actions


# import config


# gmaps.configure(api_key = os.environ[config.gmap_api])
def allDates() :
    cloak_date = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    today = date.today()
    day = today.strftime('%Y-%m-%d')
    return cloak_date, day
class User :
    def __init__(self, id, username, password) :
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
users = []
for row in actions.getUser():
    users.append(User(id=row['id'], username=row['name'], password=row['password']))

application = Flask(__name__)
application.secret_key = 'somesecretkeythatonlyishouldknow'
@application.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
    
# Авторизация администратора
@application.route('/', methods= ['POST', 'GET'])
def login() :
    if g.user :
        return redirect(url_for('profile'))
    if request.method == 'POST' :
        session.pop('user_id', None)

        username = request.form['login']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password :
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))
    return render_template('login.html')

# Работники компании
@application.route('/profile', methods= ['POST', 'GET'])
def profile() :
    if not g.user :
        return redirect(url_for('login'))
    getWorker = actions.getWorkerss()
    getLocat = actions.getLocation()
    if request.method == 'POST' :
        worker_name = request.form['worker_name']
        worker_b_day = request.form['b_day']
        worker_tg_id = request.form['tg_id']
        actions.updateWorker(worker_name, worker_b_day, worker_tg_id)
    return render_template('index.html', workers = getWorker, locations = getLocat, date = allDates()[0])

# Добавить работника
@application.route('/get-profile', methods=['POST', 'GET'])
def putProfile() :
    if not g.user :
        return redirect(url_for('login'))
    if request.method == 'POST' :
        new_worker_name = request.form['new_worker_name']
        new_worker_b_day = request.form['new_worker_b_day']
        new_worker_tg_id = request.form['new_worker_tg_id']
        actions.addWorkers(new_worker_name, new_worker_b_day, new_worker_tg_id)
    return render_template('putProfile.html')

@application.route('/delete-profile', methods=['POST', 'GET'])
def deleteProfile() :
    if not g.user :
        return redirect(url_for('login'))
    getWorker = actions.getWorkerss()
    if request.method == 'POST' :
        worker_id = request.form['worker_id']
        actions.removeWorkers(worker_id)
    return render_template('deleteProfile.html', workers = getWorker)



# Пользователи телеграм
@application.route('/users', methods= ['GET'])
def tgUsers() :
    if not g.user :
        return redirect(url_for('login'))
    TeleUsers = actions.getTelegramUser()
    return render_template('users.html', users = TeleUsers)


# Архив локации
@application.route('/location/<user_id>', methods= ['GET'])
def locationArchive(user_id):
    getWorker = actions.getWorkerss()
    getLocat = actions.getLocation()
    if not g.user :
        return redirect(url_for('login'))
    return render_template('location-id.html', workers = getWorker, locations = getLocat, user_id = user_id)

# Местоположение сегодня
@application.route('/location', methods= ['GET'])
def locationToday():
    getWorker = actions.getWorkerss()
    getLocat = actions.getLocation()
    if not g.user :
        return redirect(url_for('login'))
    return render_template('location.html', workers = getWorker, locations = getLocat, date = allDates()[1])

getLocat = actions.getLocation()
print(getLocat)
for location in getLocat :
    if  76.913000 < int(location['location_longitude']) > 76.900000 :
        print('ДААААА')
    else :
        print('Нет')
# Жалобы и предложения
@application.route('/zhaloba', methods= ['GET'])
def zhaloba() :
    zhaloba = actions.getZhaloba()
    if not g.user :
        return redirect(url_for('login'))
    return render_template('zhaloba.html', users = zhaloba)


# Аванс архив
@application.route('/avans')
def avans() :
    getWorker = actions.getWorkerss()
    avans = actions.getAvans()
    if not g.user :
        return redirect(url_for('login'))
    return render_template('avans.html', workers = getWorker, users = avans)


# Отложенные сообщения в Telegram app
@application.route('/message', methods= ['POST', 'GET'])
def message() :
    if not g.user :
        return redirect(url_for('login'))
    
    message = actions.getMessages()
    if request.method == 'POST' :
        message_id = request.form['message_id']
        actions.deleteMessages(message_id)
    return render_template('message.html', messages = message)

@application.route('/add-message', methods= ['POST', 'GET'])
def addMessage() :
    if not g.user :
        return redirect(url_for('login'))
    if request.method == 'POST' :
        message_text = request.form['msg_text']
        message_date = request.form['msg_date']
        actions.addMesages(message_text, message_date)
    return render_template('add-message.html')

# Выйти из системы
@application.route('/get_out')
def getOut() :
    if not g.user :
        return redirect(url_for('login'))
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    # application.run( debug=True)
    application.run(host='0.0.0.0', port=80)
    # debug ошибки на странице