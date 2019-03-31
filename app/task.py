from flask import Flask
from flask_mail import Mail
from .config import TestingConfig
from flask_mail import Message
from app import app
from .flask_celery import make_celery
from .db import send_ms

app.config['MAIL_SERVER'] = TestingConfig.MAIL_SERVER
app.config['MAIL_PORT'] = TestingConfig.MAIL_PORT
app.config['MAIL_USE_TLS'] = TestingConfig.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = TestingConfig.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = TestingConfig.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = TestingConfig.MAIL_PASSWORD

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
