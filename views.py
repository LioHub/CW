#!/usr/bin/env python
# coding=utf-8

from db import connect_mysql
from dictionary import menu, provider_token, prices
from words import *
import button
# import bitrix24
import time


# Check user exist
def check_user(telegram):
    check_connect()
    where = 'telegram = %s' % telegram
    return connect_mysql.select('users', where, *['telegram'])


# Check bd connection
def check_connect():
    try:
        where = 'telegram = %s' % 12345
        menu = connect_mysql.select('users', where, *['telegram'])
    except Exception as e:
        print('e', e)
        connect_mysql.open()
    return True



def select_menu(telegram):
    check_connect()
    where = 'telegram = %s' % telegram
    return connect_mysql.select('menu', where, *['telegram', 'message_id', 'text', 'index'])


def insert_menu(telegram):
    check_connect()
    connect_mysql.insert('menu', **{'telegram': telegram})


# Удалить меню
def del_menu(bot, chat_id, message_id):
    return bot.delete_message(chat_id=chat_id, message_id=message_id)


# Показ результата в виде окошки
def alert(bot, call_id, text):
    bot.answer_callback_query(call_id, show_alert=True, text=text)


# Отправить меню
def send_menu(bot, chat_id, text, index):
    check_connect()
    message_id = bot.send_message(chat_id, text, reply_markup=menu[index].get('button'), parse_mode='HTML')
    where = 'telegram = %s' % chat_id
    connect_mysql.update('menu', where, **{'message_id': message_id.message_id, 'text': text, 'index': index})


# Отправить меню
def send_photo(bot, telegram, photo, text, index):
    check_connect()
    message_id = bot.send_photo(telegram, photo, text, reply_markup=menu[index].get('button'))
    where = 'telegram = %s' % telegram
    connect_mysql.update('menu', where, **{'message_id': message_id.message_id, 'text': text, 'index': index})


def select_user(telegram):
    check_connect()
    where = 'telegram = %s' % telegram
    return connect_mysql.select('users', where, *['telegram', 'name', 'phone'])


def select_list_of_users():
    check_connect()
    return connect_mysql.select_all_for_count_row('users', *['id', 'telegram'])


def update_menu(telegram, message_id, text, index):
    check_connect()
    where = 'telegram = %s' % telegram
    connect_mysql.update('menu', where, **{'message_id': message_id,
                                           'text': text, 'index': index})


def edit_caption_of_photo(bot, caption, telegram, message_id, index):
    bot.edit_message_caption(caption, telegram, message_id, reply_markup=menu[index].get('button'))


def select_last_street(telegram):
    check_connect()
    water = "'water'"
    where = 'telegram = %s and goods = %s ORDER BY order_number DESC LIMIT 1;' % (telegram, water)
    return connect_mysql.select('orders', where, *['order_number', 'telegram', 'name', 'phone', 'goods',
                                                   'amount', 'sum', 'street'])


def for_street_menu(bot, telegram, street, where, index):
    check_connect()
    print('street %s ' % street)
    if street == []:
        message_id = bot.send_message(telegram, LOCATION, reply_markup=button.inline_location_menu(where),
                                      parse_mode='HTML')
    else:
        message_id = bot.send_message(telegram, LOCATION, reply_markup=
        button.inline_location_menu2(street.get('street'), where), parse_mode='HTML')

    where = 'telegram = %s' % telegram
    connect_mysql.update('menu', where, **{'message_id': message_id.message_id, 'text': LOCATION, 'index': index})


# Обновление кнопок
def reply_message(bot, telegram, message_id, text, index):
    bot.edit_message_text(chat_id=telegram, message_id=message_id, text=text,
                          reply_markup=menu[index].get('button'), parse_mode='HTML')
    check_connect()
    where = 'telegram = %s' % telegram
    connect_mysql.update('menu', where, **{'message_id': message_id,
                                           'text': text, 'index': index})


def insert_order(**kwargs):
    check_connect()
    connect_mysql.insert('orders', **kwargs)


def invoice(bot, telegram):
    price = prices[telegram]
    bot.send_invoice(telegram, title='SV',
                     description=PAYMENT_WARRING,
                     provider_token=provider_token,
                     currency='RUB',
                     # photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
                     # photo_height=512,  # !=0/None or picture won't be shown
                     # photo_width=512,
                     # photo_size=512,
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     prices=price,
                     start_parameter='time-machine-example',
                     invoice_payload='HAPPY FRIDAYS COUPON')



def just_send_mes(bot, telegram, text):
    bot.send_message(telegram, text, parse_mode='HTML')


def add_sub(**kwargs):
    check_connect()
    return connect_mysql.insert('subscription', **kwargs)


def select_all_orders():
    return connect_mysql.select_all('orders', *['', 'order_number', 'telegram', 'name', 'phone', 'goods',
                                                'amount', 'sum', 'street'])


def select_orders(telegram):
    check_connect()
    where = 'telegram = %s ORDER BY order_number DESC LIMIT 10;' % (telegram)
    return connect_mysql.select_all('orders', where, *['order_number', 'telegram', 'name', 'phone', 'goods',
                                                       'amount', 'sum', 'deal_id', 'status', 'street', 'added'])


def select_news():
    return connect_mysql.select_all('news', *['', 'new', 'added'])


def insert_news(telegram, new):
    check_connect()
    connect_mysql.insert('news', **{'telegram': telegram, 'new': new})


def select_all_users():
    check_connect()
    return connect_mysql.select_all('users', *['id', 'telegram'])