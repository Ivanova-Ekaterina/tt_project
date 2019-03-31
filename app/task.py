from flask import Flask
from flask_mail import Mail
from flask_mail import Message
from app import app
from .flask_celery import make_celery
from .db import send_ms

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'katyna1816@gmail.com'
app.config['MAIL_PASSWORD'] = 'ester_95'

ADMINS = ['ivanova.eka.v@gmail.com']

mail = Mail(app)

app.config.update(
    broker_url='redis://localhost:6379',
    result_backend='redis://localhost:6379'
)

celery = make_celery(app)


@celery.task(name='add_task')
def add_together(a, b):
    return a + b


@celery.task(name='ping')
def send_ping_message(nick, topic):
    send_ms(nick, topic, 'ping')
    return 'ok'


@celery.task(name='create_chat')
def send_create_chat(topic):
    msg = Message(
        "New chat" + topic + " create",
        sender="katyna1816@gmail.com",
        recipients=["ivanova.ev@phystech.edu"]
    )
    msg.body = "New chat was created"
    msg.html = "<b>'New chat</b>"
    with app.app_context():
        mail.send(msg)
    return 'ok'


celery.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'ping',
        'schedule': 60.0,
        'args': (1, 3)
    }, }
celery.conf.timezone = 'UTC'
