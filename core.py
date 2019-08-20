#!/usr/bin/env python
# coding=utf-8

from views import check_user
from words import *
from button import contact_menu
from dictionary import users, menu, product_price, product_name, prices, sub_price
from dictionary import sub_price2
from views import select_menu
from views import insert_menu
from views import del_menu
from views import send_photo
from views import check_connect
from views import select_user
from views import alert
from views import insert_order
from views import select_list_of_users
from views import edit_caption_of_photo
from views import update_menu
from views import for_street_menu
from views import select_last_street
from views import reply_message
from views import send_menu
from views import invoice
from views import just_send_mes
from views import add_sub
from views import select_orders
from views import select_news
from views import insert_news
from views import select_all_users
from send_orders import report_about_paid, edit_report
from send_orders import report
from db import connect_mysql
from telebot.types import LabeledPrice


# проверка вводов
def check_answer(bot, telegram, text):
    if check_user(telegram) == []:
        message_id = bot.send_message(telegram, NEED_PHONE_NUMBER,
                                      reply_markup=contact_menu())
        users.update({telegram: {'mess_id': message_id.message_id}})
        return True
    users_menu = select_menu(telegram)

    if users_menu.get('index') == 0:
        try:
            try:
                users[telegram].update(street=text)
            except Exception as e:
                return back_to_main_menu_del(bot, telegram)
            if users[telegram].get('min_sub'):
                show_confirm_sub_water(bot, telegram)
            if users[telegram].get('water'):
                confirm_menu(bot, telegram)
        except Exception as e:
            print('error', e)
    elif users_menu.get('index') == 10:
        try:
            users[telegram].update(comment=text)
            edit_report(users[telegram].get('report') + COMMENT.format(text))
            skip(bot, telegram)
        except Exception as e:
            return back_to_main_menu_del(bot, telegram)

    elif users_menu.get('index') == 14:
        try:
            text = int(text)

            try:

                if users[telegram].get('min_sub') <= text:
                    users[telegram].update(how_much_sub=text)
                    show_sub_water(bot, telegram)
                else:
                    text_send = 'Мало бутылок, <b>в абонементе %s</b> минимальное количество бутылей равно <b>%s</b>' % \
                                (users[telegram].get('term'), users[telegram].get('min_sub'))
                    just_send_mes(bot, telegram, text_send)
                    print('not enough water')
            except Exception as e:
                print(e)
                return back_to_main_menu_del(bot, telegram)
        except Exception as e:
            print('error', e)
            message_id = select_menu(telegram).get('message_id')
            try:
                send_menu(bot, telegram, CIN_PACK_WATER.format(users[telegram].get('price'),
                                                               users[telegram].get('min_sub'),
                                                               users[telegram].get('term')), 14)
            except Exception as e:
                return back_to_main_menu_del(bot, telegram)
            try:
                del_menu(bot, telegram, message_id)
            except Exception as e:
                print('error', e)
    elif users_menu.get('index') == 24:
        look_up_question(bot, telegram, text)
    elif users_menu.get('index') == 25:
        insert_news(telegram, text)
        back_to_main_menu_del(bot, telegram)

        all_users = select_all_users()
        print('all_users', all_users)
        print('text', text)
        for user in all_users:
            print('user', user)
            just_send_mes(bot, user.get('telegram'), 'Новости\n{}'.format(text))
    elif users_menu.get('index') == 1:
        back_to_main_menu_del(bot, telegram)



# start menu
def main_menu(bot, telegram, first_name):
    if check_user(telegram) == []:
        message_id = bot.send_message(telegram, NEED_PHONE_NUMBER, reply_markup=contact_menu())
        users.update({telegram: {'mess_id': message_id.message_id}})
        return True
    else:
        user_menu = select_menu(telegram)
        if user_menu == []:
            insert_menu(telegram)
        else:
            try:
                del_menu(bot, user_menu.get('telegram'),
                         user_menu.get('message_id'))
            except Exception as e:
                print('error', e)
    try:
        send_photo(bot, telegram, WATER_PHOTO, GREETINS.format(first_name), 1)
    except Exception as e:
        print('error', e)


# save phone_number
def take_contact(bot, telegram, first_name, phone_number):
    # send_menu
    text = GREETINS.format(first_name)

    message_id = bot.send_photo(telegram, WATER_PHOTO, text, reply_markup=menu[1].get('button'))

    try:
        del_menu(bot, telegram, users[telegram].get('mess_id'))
    except Exception as e:
        print('error', e)
        message_id = bot.send_message(telegram, NEED_PHONE_NUMBER, reply_markup=contact_menu())
        del_menu(bot, telegram, message_id.message_id)


    # adding user to users
    check_connect()
    user = select_user(telegram)
    if user == []:
        print(phone_number)
        if phone_number[0] == '+':
            phone_number = phone_number[1::]
        connect_mysql.insert('users', **{'telegram': telegram, 'name': first_name,
                                         'phone': phone_number})
        all_rows = select_list_of_users()
        report(NEW_USER.format(first_name, phone_number, all_rows))

    # adding user to menu
    user_menu = select_menu(telegram)
    if user_menu == []:
        connect_mysql.insert('menu', **{'telegram': telegram, 'message_id': message_id.message_id,
                                        'text': text.encode('utf-8'), 'index': 1})
    else:
        update_menu(telegram, message_id.message_id, text, 1)

#
# def select_bottles(bot, telegram):
#     user = select_user(telegram)
#     try:
#         users.update({telegram: {'index': 2, 'name': user.get('name'),
#                                  'phone': user.get('phone'), 'water': 1}})
#         # users[telegram].update(bottles=amount)
#     except Exception as e:
#         return back_to_main_menu_del(bot, telegram)
#     show_selected_bottles(bot, telegram, )


# the way to main menu
def back_to_main_menu_del(bot, telegram):
    try:
        if users.get(telegram):
            users.pop(telegram)
    except Exception as e:
        print(e)

    message_id = select_menu(telegram).get('message_id')
    try:
        users.pop(telegram)
    except Exception as e:
        print('error', e)
    send_photo(bot, telegram, WATER_PHOTO, MAIN_MENU, 1)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)


def show_selected_bottles(bot, telegram, product, index):
    message_id = select_menu(telegram).get('message_id')
    print('here')
    try:
        send_photo(bot, telegram, WATER_PHOTO, NAME_OF_GOOD.format(product_name.get(product)) +
                   GOOD.format(users[telegram].get(product),
                               product_price.get(product),
                               (users[telegram].get(product) *
                                int(product_price.get(product)))), index)
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)

    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    return True


# the operation plus or minus
def min_plu(bot, telegram, product, act, call_id, index):
    try:
        if act == '+':
            users[telegram][product] += 1
        else:
            if users[telegram][product] == 1:
                users[telegram][product] = 1
                alert(bot, call_id, 'Извиняй, половинку не продаем')
            else:
                users[telegram][product] -= 1
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)
    users_menu = select_menu(telegram)
    try:
        edit_caption_of_photo(bot, NAME_OF_GOOD.format(product_name.get(product)) +
                              GOOD.format(users[telegram][product],
                                          product_price.get(product),
                                          (users[telegram][product] * int(product_price.get(product)))),
                              telegram, users_menu.get('message_id'), index)
    except Exception as e:
        print('error', e)


def other_goods(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    # last_order = select_last_street(telegram)
    try:
        send_photo(bot, telegram, POMPA_PHOTO, OTHER_GOODS, 6)
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    if users[telegram].get('pompa'):
        users[telegram].pop('pompa')
    if users[telegram].get('pompaEL'):
        users[telegram].pop('pompaEL')
    if users[telegram].get('culer'):
        users[telegram].pop('culer')


def select_good(bot, telegram, product, index):
    user = select_user(telegram)
    try:
        if not users.get(telegram):
            users.update({telegram: {'name': user.get('name'),
                                     'phone': user.get('phone')
                                     }})
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)

    try:
        users[telegram].update({product: 1})
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)

    show_selected_bottles(bot, telegram, product, index)


def write_adress(bot, telegram, menu):
    message_id = select_menu(telegram).get('message_id')
    for_street_menu(bot, telegram, select_last_street(telegram), menu, 0)
    # send_menu(bot, telegram, LOCATION, 7)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    # for_street_menu(bot, telegram, select_last_street(telegram), 'show_pompa', 0)


def confirm_menu(bot, telegram):
    try:
        text_for_confirm = DATES_FOR_CONFIRM.format(users[telegram].get('name'),
                                                    users[telegram].get('phone'),
                                                    users[telegram].get('street'))
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)
    total = 1

    prices_productes = []

    if users[telegram].get('water'):
        text_for_confirm += BOTTLE_FOR_CONFIRM.format(users[telegram].get('water'),
                                                      product_price.get('water'),
                                                      (users[telegram].get('water') *
                                                       int(product_price.get('water'))))
        total = users[telegram].get('water') * int(product_price.get('water'))
        prices_productes.append(LabeledPrice(label='water',
                                             amount=int(users[telegram].get('water')) *
                                                    int(product_price.get('water'))  * 100))
    if users[telegram].get('pompa'):
        text_for_confirm += POMPA_FOR_CONFIRM.format(users[telegram].get('pompa'),
                                                     product_price.get('pompa'),
                                                     (users[telegram].get('pompa') *
                                                      int(product_price.get('pompa'))))
        total += users[telegram].get('pompa') * int(product_price.get('pompa'))
        prices_productes.append(LabeledPrice(label='pompa',
                                             amount=int(users[telegram].get('pompa')) *
                                                    int(product_price.get('pompa')) * 100))

    if users[telegram].get('pompaEL'):
        text_for_confirm += POMPA_FOR_CONFIRM.format(users[telegram].get('pompaEL'),
                                                     product_price.get('pompaEL'),
                                                     (users[telegram].get('pompaEL') *
                                                      int(product_price.get('pompaEL'))))
        total += users[telegram].get('pompaEL') * int(product_price.get('pompaEL'))
        prices_productes.append(LabeledPrice(label='pompaEL',
                                             amount=int(users[telegram].get('pompaEL')) *
                                                    int(product_price.get('pompaEL')) * 100))

    if users[telegram].get('culer'):
        text_for_confirm += CULER_FOR_CONFIRM.format(users[telegram].get('culer'),
                                                     product_price.get('culer'),
                                                     (users[telegram].get('culer') *
                                                      int(product_price.get('culer'))))
        total += users[telegram].get('culer') * int(product_price.get('culer'))
        prices_productes.append(LabeledPrice(label='culer',
                                             amount=int(users[telegram].get('culer')) *
                                                    int(product_price.get('culer')) * 100))

    prices.update({telegram: prices_productes})
    text_for_confirm += ITOG_CONFIRM.format(total)
    # if first:


    try:
        del_menu(bot, telegram, select_menu(telegram).get('message_id'))
    except Exception as e:
        print(e)

    send_menu(bot, telegram, text_for_confirm, 8)


def confirm(bot, telegram, call_id):
    pay_menu(bot, telegram)

    text = ''
    price_water = []
    print('here')
    text = FOR_SEND_ORDER_TO_OTHER_BOT2.format(telegram, users[telegram].get('name'),
                                               users[telegram].get('phone'),
                                               users[telegram].get('street'))
    if users[telegram].get('water'):
        try:
            if users[telegram].get('water'):
                insert_order(**{'telegram': telegram, 'name': users[telegram].get('name'),
                                'phone': users[telegram].get('phone'), 'goods': 'water',
                                'amount': users[telegram].get('water'),
                                'sum': (users[telegram].get('water') * product_price.get('water')),
                                'street': users[telegram].get('street')})

                summa = users[telegram].get('water') * product_price.get('water') * 100
                price_water.append(LabeledPrice(label='water19',
                                                amount=summa))
                prices.update({telegram:
                                   [LabeledPrice(label='water19',
                                                 amount=int(users[telegram].get('water')) *
                                                        int(product_price.get('water')))]})
                try:
                    text += FOR_SEND_BOTTLE_TO_OTHER_BOT.format('вода', users[telegram].get('water'),
                                                                (users[telegram].get('water') *
                                                                 int(product_price.get('water'))))
                except Exception as e:
                    print('error', e)
        except Exception as e:
            return back_to_main_menu_del(bot, telegram)
    if users[telegram].get('pompa'):
        insert_order(**{'telegram': telegram, 'name': users[telegram].get('name'),
                        'phone': users[telegram].get('phone'), 'goods': 'pompa',
                        'amount': users[telegram].get('pompa'),
                        'sum': (users[telegram].get('pompa') * product_price.get('pompa')),
                        'street': users[telegram].get('street')})

        try:
            text += FOR_SEND_POMPA_TO_OTHER_BOT.format('помпа', users[telegram].get('pompa'),
                                                        (users[telegram].get('pompa') *
                                                         product_price.get('pompa')))
            summa = int(users[telegram].get('pompa')) * int(product_price.get('pompa')) * 100

            price_water.append(LabeledPrice(label='pompa',
                                            amount=summa))
            if prices.get(telegram):
                prices[telegram].append(LabeledPrice(label='pompa',
                                                 amount=users[telegram].get('pompa') *
                                                        product_price.get('pompa')))
            else:
                prices.update({telegram:
                                   [LabeledPrice(label='pompa',
                                                 amount=int(users[telegram].get('pompa')) *
                                                        int(product_price.get('pompa')))]})

        except Exception as e:
            print('error pompa', e)

    if users[telegram].get('pompaEL'):
        insert_order(**{'telegram': telegram, 'name': users[telegram].get('name'),
                        'phone': users[telegram].get('phone'), 'goods': 'pompaEL',
                        'amount': users[telegram].get('pompaEL'),
                        'sum': (users[telegram].get('pompaEL') * product_price.get('pompaEL')),
                        'street': users[telegram].get('street')})

        summa = int(users[telegram].get('pompaEL')) * int(product_price.get('pompaEL')) * 100
        price_water.append(LabeledPrice(label='pompaEL',
                                        amount=summa))
        if prices.get(telegram):
            prices[telegram].append(LabeledPrice(label='pompaEL',
                                                 amount=users[telegram].get('pompaEL') *
                                                        product_price.get('pompaEL')))
        else:
            prices.update({telegram:
                               [LabeledPrice(label='pompaEL',
                                             amount=int(users[telegram].get('pompaEL')) *
                                                    int(product_price.get('pompaEL')))]})

        try:
            text += FOR_SEND_POMPA_TO_OTHER_BOT.format('помпа электрическа',
                                                       users[telegram].get('pompaEL'),
                                                       (users[telegram].get('pompaEL') *
                                                        product_price.get('pompaEL')))
        except Exception as e:
            print('error pompaEL', e)
    print('here')
    if users[telegram].get('culer'):
        insert_order(**{'telegram': telegram, 'name': users[telegram].get('name'),
                        'phone': users[telegram].get('phone'), 'goods': 'culer',
                        'amount': users[telegram].get('culer'),
                        'sum': (users[telegram].get('culer') * product_price.get('culer')),
                        'street': users[telegram].get('street')})

        summa = int(users[telegram].get('culer')) * int(product_price.get('culer')) * 100
        price_water.append(LabeledPrice(label='culer',
                                        amount=summa))

        if prices.get(telegram):
            prices[telegram].append(LabeledPrice(label='culer',
                                                 amount=users[telegram].get('culer') *
                                                        product_price.get('culer')))
        else:
            prices.update({telegram:
                               [LabeledPrice(label='culer',
                                             amount=int(users[telegram].get('culer')) *
                                                    int(product_price.get('culer')))]})
        try:
            text += FOR_SEND_POMPA_TO_OTHER_BOT.format('кулер', users[telegram].get('culer'),
                                                        (users[telegram].get('culer') *
                                                         product_price.get('culer')))
        except Exception as e:
            print('error pompa', e)
    print('here')
    users[telegram].update(report=text)
    print('here')
    report(text)
    try:
        users.pop(telegram)
    except Exception as e:
        print(e)

# Ввод/изменение адреса
def change_adress(bot, telegram, where, index):
    write_adress(bot, telegram, 'back_to_confirm')



# Функция вывода меню для выбора метода оплаты
def pay_menu(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, PAYMENT_METHOD, 9)


# Функция для яндекс оплаты
def yandex_payment(bot, telegram):
    invoice(bot, telegram)

# Функция для комментов
def leave_wishes(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, WISHES, 10)

# Функция оплаты наличными
def cash_payment(bot, telegram):
    return back_to_main_menu_del(bot, telegram)


def payment_success(bot, telegram, summa):
    message_id = select_menu(telegram).get('message_id')
    send_menu(bot, telegram, WISHES, 10)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print(e)
    user = select_user(telegram)
    report_about_paid(USER_PAID.format(user.get('name'), summa,
                                       user.get('telegram'), user.get('phone')))


# Пропустить
def skip(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    send_menu(bot, telegram, THANKS_FOR_ORDER_OUT + '\n' + MAIN_MENU, 1)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)


# Заказать
def order(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    send_menu(bot, telegram, CHOOSE_GOOD, 11)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print(e)


# Установить адрес
def set_street(bot, telegram):
    if select_menu(telegram).get('index') == 0:
        try:
            users[telegram].update(street=select_last_street(telegram).get('street'))
        except Exception as e:
            print('error', e)
            return back_to_main_menu_del(bot, telegram)
        if users[telegram].get('min_sub'):
            show_confirm_sub_water(bot, telegram)
            # if users[telegram].get('water'):
        else:
            confirm_menu(bot, telegram)

    # if select_menu(telegram).get('index') == 26:
    #     try:
    #         users[telegram].update(pack_street=select_last_street(telegram).get('street'))
    #     except Exception as e:
    #         print('error', e)
    #         return back_to_main_menu_del(bot, telegram)
    #     show_confirm_pack_bottle(bot, telegram)


# Повторить последний заказ
def replay_order(bot, telegram):
    last_order = select_last_street(telegram)
    last_order.pop('order_number')
    users.update({last_order.get('telegram'): last_order})
    users[telegram].update(water=last_order.get('amount'))
    text_for_confirm = DATES_FOR_CONFIRM.format(users[telegram].get('name'), users[telegram].get('phone'),
                                                                                   users[telegram].get('street'))
    total = 1
    if users[telegram].get('water'):
        text_for_confirm += BOTTLE_FOR_CONFIRM.format(users[telegram].get('water'), product_price.get('water'),
                                                       (users[telegram].get('water') * int(product_price.get('water'))))
        total = users[telegram].get('water') * int(product_price.get('water'))
    text_for_confirm += ITOG_CONFIRM.format(total)
    reply_message(bot, telegram, select_menu(telegram).get('message_id'), text_for_confirm, 8)


def subscription(bot, telegram):
    return reply_message(bot, telegram, select_menu(telegram).get('message_id'), ALL_SUBSCRIPTION, 12)


def take_sub(bot, telegram, sub, index):
    user = select_user(telegram)
    try:
        users.update({telegram: {'index': index, 'name': user.get('name'),
                                 'phone': user.get('phone')}})
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)

    try:
        users[telegram].update(sub_price2.get(sub))
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)


    reply_message(bot, telegram, select_menu(telegram).get('message_id'),
                  CIN_PACK_WATER.format(sub_price2.get(sub).get('price'),
                                        sub_price2.get(sub).get('min_sub'),
                                        sub_price2.get(sub).get('term')), index)


def min_plu_of_sub(bot, telegram, act, call_id):
    try:
        if act == '-':
            if users[telegram]['how_much_sub'] <= users[telegram]['min_sub']:
                users[telegram]['how_much_sub'] = users[telegram]['min_sub']
                alert(bot, call_id, 'Извиняй, {}бут это минимально возможное количество на {}'.
                      format(users[telegram]['min_sub'], users[telegram]['term']))
            else:
                users[telegram]['how_much_sub'] -= 1
        else:
            try:
                users[telegram]['how_much_sub'] += 1
            except Exception as e:
                return back_to_main_menu_del(bot, telegram)
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)

    users_menu = select_menu(telegram)
    try:
        edit_caption_of_photo(bot, SHOW_SUB.format(
            users[telegram]['price'], users[telegram]['term'],
            users[telegram]['how_much_sub'],
            (users[telegram]['how_much_sub'] * int(users[telegram]['price'])),
            (users[telegram]['how_much_sub'] * (int(product_price.get('water')) -
                                                int(users[telegram]['price'])))),
            telegram, users_menu.get('message_id'), 13)
    except Exception as e:
        print('error', e)




def show_sub_water(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    try:
        send_photo(bot, telegram, WATER_PHOTO, SHOW_SUB.
                   format(users[telegram]['price'], users[telegram]['term'],
                          users[telegram]['how_much_sub'],
                          (users[telegram]['how_much_sub'] * int(users[telegram]['price'])),
                          (users[telegram]['how_much_sub'] * (150 - int(users[telegram]['price'])))), 13)
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)


def show_confirm_sub_water(bot, telegram, where=True):
    text = ''
    message_id = select_menu(telegram).get('message_id')
    try:
        text = SHOW_SUB_FOR_CONFIRM.format(
            users[telegram].get('price'), users[telegram].get('term'),
            users[telegram].get('how_much_sub'), users[telegram].get('street'),
            (int(users[telegram].get('how_much_sub')) * int(users[telegram].get('price'))),
            (int(product_price.get('water')) - int(users[telegram].get('price'))) *
            int(users[telegram].get('how_much_sub')))
    except Exception as e:
        return back_to_main_menu_del(bot, telegram)
    try:
        return reply_message(bot, telegram, message_id, text, 15)
    except Exception as e:
        print('error', e)
    return




def confirm_sub(bot, telegram):
    # statTime = time.strftime("%y%m")
    # statTime += '01'

    try:
        price_water = []
        add_sub(**{'telegram': telegram, 'name': users[telegram].get('name'),
                       'phone': users[telegram].get('phone'), 'price': users[telegram]['price'],
                       'term': users[telegram]['term'], 'quantity': users[telegram]['how_much_sub'],
                       'sum': (int(users[telegram]['price']) * int(users[telegram]['how_much_sub'])),
                       'econom': (int(users[telegram].get('how_much_sub')) *
                                  (int(product_price.get('water')) - int(users[telegram]['price']))),
                       'street': users[telegram].get('street')})
        summa = int(users[telegram]['price']) * int(users[telegram]['how_much_sub']) * 100
        price_water.append(LabeledPrice(label=users[telegram]['term'],
                                        amount=summa))
        prices.update({telegram: price_water})
    except Exception as e:
        print('e', e)
        return back_to_main_menu_del(bot, telegram)
    try:
        text = FOR_SEND_SUB_TO_OTHER_BOT.format(telegram, users[telegram].get('name'),
                                             users[telegram].get('phone'), users[telegram]['term'],
                                             users[telegram]['price'], users[telegram]['how_much_sub'],
                                             (int(users[telegram]['price']) * int(users[telegram]['how_much_sub'])),
                                             (int(users[telegram].get('how_much_sub')) * (int(product_price.get('water'))
                                                                                    - int(users[telegram]['price']))),
                                             users[telegram].get('street'))
    except Exception as e:
        print(e)
        return back_to_main_menu_del(bot, telegram)
    report(text)
    try:
        users[telegram].update(report=text)
    except Exception as e:
        back_to_main_menu_del(bot, telegram)
    pay_menu(bot, telegram)




def shop(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    # reply_message(bot, telegram, message_id, SELECT_PRODUCT, 16)
    send_menu(bot, telegram, SELECT_PRODUCT, 16)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    if users.get(telegram):
        users.pop(telegram)


def add_n_skip(bot, telegram):
    message_id = select_menu(telegram).get('message_id')

    send_menu(bot, telegram, ADD_GOOD, 22)

    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print(e)
        back_to_main_menu_del(bot, telegram)


def basket(bot, telegram, message_id):
    orders = select_orders(telegram)
    message_id = select_menu(telegram).get('message_id')
    if orders == []:
        send_menu(bot, telegram, BAKEST_EMPTY, 11)
        try:
            del_menu(bot, telegram, message_id)
        except Exception as e:
            print('error', e)
    else:
        text = build_orders(orders[::-1])
        # 'Корзина'
        send_menu(bot, telegram, text, 1)
        try:
            del_menu(bot, telegram, message_id)
        except Exception as e:
            print('error', e)
    return


def build_orders(orders):
    text = ''
    max_orders = 10
    for order in orders:
        text += ORDER_NUMBER % order.get('order_number') + \
                DATES_FOR_CONFIRM.format(order.get('name'), order.get('phone'), order.get('street')) + \
                BASKET_ORDERS.format(order.get('goods'), str(order.get('amount')),
                                     product_price.get(order.get('goods')), str(order.get('sum')), order.get('added'))

        if max_orders == 0:
            break
        max_orders -= 1
    return text



def news(bot, telegram):
    all_news = select_news()
    message_id = select_menu(telegram).get('message_id')
    if all_news == []:
        if telegram == 226665834:
            send_menu(bot, telegram, NEWS_EMPTY, 26)
        else:
            send_menu(bot, telegram, NEWS_EMPTY, 1)
        # reply_message(bot, telegram, message_id, NEWS_EMPTY, 1)
    else:
        new_text = ''
        all_news = all_news[::-1]
        last_news = []
        total = 10
        for new in all_news:
            last_news.append(new)
            total -= 1
            if total == 0:
                break

        last_news = last_news[::-1]

        for new in last_news:
            new_text += NEW.format(new.get('new'), new.get('added'))
        if telegram == 226665834:
            send_menu(bot, telegram, new_text, 26)
        else:
            send_menu(bot, telegram, new_text, 1)

    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    return


def add_news(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, WRITE_NEW, 25)


def instruction(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    send_menu(bot, telegram, NEED_HELP, 23)
    try:
        del_menu(bot, telegram, message_id)
    except Exception as e:
        print('error', e)
    return


def show_contacts(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, ABOUT_COMPANY, 1)
    return True


def write_to_us(bot, telegram):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, WRITE_QUESTION, 24)
    return True


def look_up_question(bot, telegram, text):
    message_id = select_menu(telegram).get('message_id')
    reply_message(bot, telegram, message_id, THANKS_FOR_QUESTION, 1)
    user = select_user(telegram)
    msg = USER_QUESTION.format(user.get('name'), user.get('phone'), text)
    report(msg)
    return True