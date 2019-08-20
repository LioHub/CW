#!/usr/bin/env python
# coding=utf-8

from telebot import TeleBot, types

import core
import time

from core import news
from core import basket
from core import min_plu
from core import confirm
from core import main_menu
from core import instruction
from core import other_goods
from core import select_good
from core import check_answer
from core import take_contact
from core import subscription
from core import write_adress
from core import change_adress
from core import payment_success
from core import skip
from core import shop
from core import order
from core import set_street
from core import pay_menu
from core import take_sub
from core import confirm_menu
from core import leave_wishes
from core import cash_payment
from core import yandex_payment
from core import replay_order
from core import min_plu_of_sub
from core import confirm_sub
from core import add_n_skip
from core import show_contacts
from core import write_to_us
from core import add_news
from core import show_sub_water
from core import back_to_main_menu_del
from core import show_confirm_sub_water


token = ''
bot = TeleBot(token)

# WEBHOOK_HOST = ''
# WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
# LOCAL_PORT = 9001  #
# LOCAL_LISTEN = '127.0.0.1'
# WEBHOOK_LISTEN = ''
#
# # WEBHOOK_SSL_CERT = '/root/ssl/webhook_cert.pem'  # Путь к сертификату
# WEBHOOK_SSL_CERT = '/home/iman/ssl/webhook_pkey.pem'  # Путь к сертификату

#
# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# LOCAL_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, LOCAL_PORT)
# WEBHOOK_URL_PATH = "/%s/" % token

#
# bot = TeleBot(token)
#
# app = Flask(__name__)
#
#
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     update = types.Update.de_json(request.get_json(force=True))
#     bot.process_new_updates([update])
#     return ''



@bot.message_handler(commands=["start"])
def start_main_menu(message):
    main_menu(bot, message.chat.id, message.from_user.first_name)


# Ввод контактов
@bot.message_handler(content_types=["contact"])
def contact(message):
    print('Here1')
    take_contact(bot, message.chat.id, message.from_user.first_name, message.contact.phone_number)


user_time = {}


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        telegram = call.message.chat.id
        message_id = call.message.message_id
        # try:
        #     user_time[telegram].get('last_time')
        # except Exception as e:
        #     user_time.update({telegram: {'last_time': time.time(), 'first_time': True}})
        #     print(e)
        # if user_time[telegram].get('last_time') < (time.time() - 1) or user_time[telegram].get('first_time'):
        if call.message:
                user_time.update({telegram: {'last_time': time.time(), 'first_time': False}})
                # main menu
                print(call.data)
                if call.data[:7] == "start: ":
                    if call.data[7:] == 'order_water':
                        core.select_good(bot, telegram, 'water', 2)
                    elif call.data[7:] == 'order':
                        order(bot, telegram)
                    elif call.data[7:] == 'basket':
                        basket(bot, telegram, message_id)
                    elif call.data[7:] == 'subscription':
                        subscription(bot, telegram)
                    elif call.data[7:] == 'shop':
                        shop(bot, telegram)
                    elif call.data[7:] == 'news':
                        news(bot, telegram)
                    elif call.data[7:] == 'instruction':
                        instruction(bot, telegram)

                elif call.data[:8] == "basket: ":
                    if call.data[8:] == 'replay_order':
                        replay_order(bot, telegram)

                elif call.data[:13] == "order_water: ":
                    if call.data[13:] == 'minus':
                        min_plu(bot, telegram, 'water', '-', call.id, 2)
                    elif call.data[13:] == 'select':
                        other_goods(bot, telegram)
                    elif call.data[13:] == 'plus':
                        min_plu(bot, telegram, 'water', '+', call.id, 2)

                elif call.data[:7] == "goods: ":
                    if call.data[7:] == 'pompa':
                        select_good(bot, telegram, 'pompa', 3)
                    elif call.data[7:] == 'pompaEL':
                        select_good(bot, telegram, 'pompaEL', 4)
                    elif call.data[7:] == 'culer':
                        select_good(bot, telegram, 'culer', 5)
                    elif call.data[7:] == 'skip':
                        write_adress(bot, telegram, 'other_goods')

                elif call.data[:13] == "order_pompa: ":
                    if call.data[13:] == 'minus':
                        min_plu(bot, telegram, 'pompa', '-', call.id, 3)
                    elif call.data[13:] == 'select':
                        # other_goods(bot, telegram)
                        write_adress(bot, telegram, 'back_to_pompa')
                    elif call.data[13:] == 'plus':
                        min_plu(bot, telegram, 'pompa', '+', call.id, 3)


                elif call.data[:15] == "order_pompaEL: ":
                    if call.data[15:] == 'minus':
                        min_plu(bot, telegram, 'pompaEL', '-', call.id, 4)
                    elif call.data[15:] == 'select':
                        # other_goods(bot, telegram)
                        write_adress(bot, telegram, 'back_to_pompaEL')
                    elif call.data[15:] == 'plus':
                        min_plu(bot, telegram, 'pompaEL', '+', call.id, 4)

                elif call.data[:13] == "order_culer: ":
                    if call.data[13:] == 'minus':
                        min_plu(bot, telegram, 'culer', '-', call.id, 5)
                    elif call.data[13:] == 'select':
                        # other_goods(bot, telegram)
                        write_adress(bot, telegram, 'back_to_culer')
                    elif call.data[13:] == 'plus':
                        min_plu(bot, telegram, 'culer', '+', call.id, 5)

                elif call.data[:6] == "subs: ":
                    if call.data[6:] == "1_month":
                        take_sub(bot, telegram, "1_month", 14)
                    elif call.data[6:] == "3_months":
                        take_sub(bot, telegram, "3_months", 14)
                    elif call.data[6:] == "6_months":
                        take_sub(bot, telegram, "6_months", 14)
                    elif call.data[6:] == "1_year":
                        take_sub(bot, telegram, "1_year", 14)
                    elif call.data[6:] == "minus":
                        min_plu_of_sub(bot, telegram, "-", call.id)
                    elif call.data[6:] == "plus":
                        min_plu_of_sub(bot, telegram, "+", call.id)
                    elif call.data[6:] == "change_adress":
                        write_adress(bot, telegram, 'confirm_sub')
                    elif call.data[6:] == "select":
                        write_adress(bot, telegram, 'back_to_sub')
                    elif call.data[6:] == "confirm_sub":
                        confirm_sub(bot, telegram)

                elif call.data[:6] == "shop: ":
                    if call.data[6:] == 'water':
                        select_good(bot, telegram, 'water', 18)
                    elif call.data[6:] == 'pompa':
                        select_good(bot, telegram, 'pompa', 19)
                    elif call.data[6:] == 'pompaEL':
                        select_good(bot, telegram, 'pompaEL', 20)
                    elif call.data[6:] == 'culer':
                        select_good(bot, telegram, 'culer', 21)


                elif call.data[:14] == "shop_pompaEL: ":
                    if call.data[14:] == 'minus':
                        min_plu(bot, telegram, 'pompaEL', '-', call.id, 20)
                    elif call.data[14:] == 'select':
                        # other_goods(bot, telegram)
                        # add_n_skip(bot, telegram)
                        write_adress(bot, telegram, 'back_to_shop')
                    elif call.data[14:] == 'plus':
                        min_plu(bot, telegram, 'pompaEL', '+', call.id, 20)

                elif call.data[:12] == "shop_pompa: ":
                    if call.data[12:] == 'minus':
                        min_plu(bot, telegram, 'pompa', '-', call.id, 19)
                    elif call.data[12:] == 'select':
                        # other_goods(bot, telegram)

                        # add_n_skip(bot, telegram)
                        write_adress(bot, telegram, 'back_to_shop')
                    elif call.data[12:] == 'plus':
                        min_plu(bot, telegram, 'pompa', '+', call.id, 19)

                elif call.data[:12] == "shop_culer: ":
                    if call.data[12:] == 'minus':
                        min_plu(bot, telegram, 'culer', '-', call.id, 21)
                    elif call.data[12:] == 'select':
                        # other_goods(bot, telegram)

                        # add_n_skip(bot, telegram)
                        write_adress(bot, telegram, 'back_to_shop')
                    elif call.data[12:] == 'plus':
                        min_plu(bot, telegram, 'culer', '+', call.id, 21)

                elif call.data[:12] == "shop_water: ":
                    if call.data[12:] == 'minus':
                        min_plu(bot, telegram, 'water', '-', call.id, 18)
                    elif call.data[12:] == 'select':
                        # other_goods(bot, telegram)

                        # add_n_skip(bot, telegram)
                        write_adress(bot, telegram, 'back_to_shop')
                    elif call.data[12:] == 'plus':
                        min_plu(bot, telegram, 'water', '+', call.id, 18)

                elif call.data[:6] == "back: ":
                    if call.data[6:] == 'back_to_main_menu_del':
                        back_to_main_menu_del(bot, telegram)
                    if call.data[6:] == 'back_to_main_menu':
                        back_to_main_menu_del(bot, telegram)
                    if call.data[6:] == 'other_goods':
                        other_goods(bot, telegram)
                    if call.data[6:] == 'back_to_pompa':
                        select_good(bot, telegram, 'pompa', 3)
                    if call.data[6:] == 'back_to_pompaEL':
                        select_good(bot, telegram, 'pompaEL', 4)
                    if call.data[6:] == 'back_to_culer':
                        select_good(bot, telegram, 'culer', 5)
                    if call.data[6:] == 'back_to_confirm':
                        confirm_menu(bot, telegram)
                    if call.data[6:] == 'back_to_abonem':
                        subscription(bot, telegram)
                    if call.data[6:] == 'confirm_sub':
                        show_confirm_sub_water(bot, telegram)
                    if call.data[6:] == 'back_to_shop':
                        shop(bot, telegram)
                    if call.data[6:] == 'add_n_skip':
                        add_n_skip(bot, telegram)
                    if call.data[6:] == 'back_to_sub':
                        show_sub_water(bot, telegram)
                    elif call.data[6:] == 'order_pompaEL' or call.data[6:] == 'order_pompa' or \
                                    call.data[6:] == 'order_culer':
                        other_goods(bot, telegram)
                    elif call.data[6:] == 'shop_water' or call.data[6:] == 'shop_pompa' or \
                                    call.data[6:] == 'shop_pompaEL' or call.data[6:] == 'shop_culer':
                        shop(bot, telegram)

                elif call.data[:9] == "confirm: ":
                    if call.data[9:] == "confirm":
                        confirm(bot, telegram, call.id)
                    elif call.data[9:] == 'change_adress':
                        change_adress(bot, telegram, "show_confirm", 0)

                elif call.data[:10] == "location: ":
                    if call.data[10:16] == 'street':
                        print('before error', call.data)
                        set_street(bot, telegram)

                elif call.data[:9] == "payment: ":
                    if call.data[9:] == "pay_menu":
                        pay_menu(bot, telegram)
                    elif call.data[9:] == "yandex":
                        yandex_payment(bot, telegram)
                    elif call.data[9:] == "cash":
                        cash_payment(bot, telegram)
                    elif call.data[9:] == 'wish':
                        leave_wishes(bot, telegram)
                    elif call.data[9:] == 'skip':
                        skip(bot, telegram)

                elif call.data[:13] == "instruction: ":
                    if call.data[13:] == "write_to_us":
                        write_to_us(bot, telegram)
                    if call.data[13:] == "about_company":
                        show_contacts(bot, telegram)

                elif call.data[:6] == "news: ":
                    if call.data[6:] == "add":
                        add_news(bot, telegram)

    except Exception as e:
        print(e)


@bot.message_handler(content_types=["photo"])
def photos(message):
    try:
        print(message.photo[0].file_id)
    except Exception as e:
        print(e)
    # builder_menu(bot, message.chat.id)


# @bot.message_handler(content_types=['document', 'audio'])
# def audio(message):
#     print('audio')
#     builder_menu(bot, message.chat.id)



# Payment
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    summa = message.successful_payment.total_amount / 100
    payment_success(bot, message.chat.id, summa)


# text checker
@bot.message_handler(content_types=["text"])
def build_menu(message):
    try:
        check_answer(bot, message.chat.id, message.text)
    except Exception as e:
        print(e)

# bot.remove_webhook()

if __name__ == '__main__':
    bot.polling(none_stop=True)

#
#
#
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
#                 certificate=open(WEBHOOK_SSL_CERT, 'rb'))
#
# app.run(host=LOCAL_LISTEN, port=LOCAL_PORT, debug=True)