 #!/usr/bin/env python
# coding=utf-8

from telebot import types


def contact_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))
    return keyboard


# def location_menu():
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     keyboard.add(types.KeyboardButton(text="Отправить свою локацию", request_location=True))
#     return keyboard


# def back_to_main_menu():
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     keyboard.add(types.KeyboardButton(text="В начало"))
#     return keyboard


# _________Инлайн_кнопки___________

# Main menu
def inline_main_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        # keyboard.add(types.InlineKeyboardButton(text="Заказать", callback_data="start: order_water"))
        keyboard.add(*[types.InlineKeyboardButton(text="Заказать", callback_data="start: order"),
                       types.InlineKeyboardButton(text="Заказы", callback_data="start: basket")])
                     # types.InlineKeyboardButton(text="Абонемент", callback_data="confirm: want_to_economize")])
        keyboard.add(*[types.InlineKeyboardButton(text="Новости", callback_data="start: news"),
                       types.InlineKeyboardButton(text="❓Помощь", callback_data="start: instruction")])
        return keyboard
    except Exception as e:
        print(e)
    return False



def inline_pre_order_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        # keyboard.add(types.InlineKeyboardButton(text="Заказать", callback_data="start: order_water"))
        keyboard.add(types.InlineKeyboardButton(text="Заказать воду", callback_data="start: order_water"))
        keyboard.add(types.InlineKeyboardButton(text="Повторить последний заказ", callback_data="basket: replay_order"))
        keyboard.add(types.InlineKeyboardButton(text="Абонемент", callback_data="start: subscription"))
        keyboard.add(types.InlineKeyboardButton(text="Магазин", callback_data="start: shop"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: back_to_main_menu_del"))
        return keyboard
    except Exception as e:
        print(e)
    return False


# Order water menu
def inline_order_water(type_of_order):
    try:
        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(*[types.InlineKeyboardButton(text='🔻', callback_data=type_of_order + ': minus'),
                       types.InlineKeyboardButton(text='Заказать', callback_data=type_of_order + ': select'),
                       types.InlineKeyboardButton(text='🔺', callback_data=type_of_order + ': plus')])
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu_del"))
        return keyboard
    except Exception as e:
        print(e)
    return False



# Order water menu
def inline_order_acsess(type_of_order):
    try:
        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(*[types.InlineKeyboardButton(text='🔻', callback_data=type_of_order + ': minus'),
                       types.InlineKeyboardButton(text='Заказать', callback_data=type_of_order + ': select'),
                       types.InlineKeyboardButton(text='🔺', callback_data=type_of_order + ': plus')])
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: {}".format(type_of_order)))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu_del"))
        return keyboard
    except Exception as e:
        print(e)
    return False



def inline_other_goods_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text="Помпа мех", callback_data="goods: pompa"),
                       types.InlineKeyboardButton(text="Помпа элек", callback_data="goods: pompaEL")])
        keyboard.add(types.InlineKeyboardButton(text="Кулер", callback_data="goods: culer"))
        keyboard.add(*[types.InlineKeyboardButton(text="Назад", callback_data="start: order_water"),
                       types.InlineKeyboardButton(text="Пропустить", callback_data="goods: skip")
                       ])
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        # keyboard.add(*[types.InlineKeyboardButton(text="Помпа мех", callback_data="goods: pompa"))
        # keyboard.add(types.InlineKeyboardButton(text="Помпа элек", callback_data="goods: pompaEL"))
        # keyboard.add(types.InlineKeyboardButton(text="Кулер 6990", callback_data="goods: culer"))
        # keyboard.add(types.InlineKeyboardButton(text="Пропустить", callback_data="goods: skip"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_pre_payment_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Банковской картой", callback_data="payment: yandex"))
        keyboard.add(types.InlineKeyboardButton(text="Наличными", callback_data="payment: wish"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_comment_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Пропустить", callback_data="payment: skip"))
        return keyboard
    except Exception as e:
        print(e)
    return False



def inline_location_menu(where):
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: {}".format(where)))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu_del"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_location_menu2(street, where):
    try:
        keyboard = types.InlineKeyboardMarkup()
        # keyboard.add(types.InlineKeyboardButton(text=street, callback_data="location: street {}".format(street)))
        keyboard.add(types.InlineKeyboardButton(text=street, callback_data="location: street"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: {}".format(where)))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu_del"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_sub_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="На 1 мес.", callback_data='subs: 1_month'))
        keyboard.add(types.InlineKeyboardButton(text="На 3 мес.", callback_data='subs: 3_months'))
        keyboard.add(types.InlineKeyboardButton(text="На 6 мес.", callback_data='subs: 6_months'))
        keyboard.add(types.InlineKeyboardButton(text="На 1 год.", callback_data='subs: 1_year'))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='start: order'))
        return keyboard
    except Exception as e:
        print(e)
    return False



def inline_cin_abone_menu(where):
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back: {}'.format(where)))
        return keyboard
    except Exception as e:
        print(e)
    return False



def inline_shop_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вода 19л", callback_data="shop: water"))
        keyboard.add(types.InlineKeyboardButton(text="Помпа мех", callback_data="shop: pompa"))
        keyboard.add(types.InlineKeyboardButton(text="Помпа элек", callback_data="shop: pompaEL"))
        keyboard.add(types.InlineKeyboardButton(text="Кулер", callback_data="shop: culer"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="start: order"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        # keyboard.add(*[types.InlineKeyboardButton(text="Помпа мех", callback_data="goods: pompa"))
        # keyboard.add(types.InlineKeyboardButton(text="Помпа элек", callback_data="goods: pompaEL"))
        # keyboard.add(types.InlineKeyboardButton(text="Кулер 6990", callback_data="goods: culer"))
        # keyboard.add(types.InlineKeyboardButton(text="Пропустить", callback_data="goods: skip"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_add_else_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text="Добавить", callback_data='shop: add'),
                       types.InlineKeyboardButton(text="Нет, пропустить", callback_data='shop: skip')])
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data='back: back_to_main_menu'))
        return keyboard
    except Exception as e:
        print(e)
    return False

#---------------------


def inline_basket_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Повторить последний заказ", callback_data="basket: replay_order"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False


# Help menu
def inline_instruction_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text="Написать нам", callback_data="instruction: write_to_us"),
                       types.InlineKeyboardButton(text="Контакты компании", callback_data="instruction: about_company")])
        # keyboard.add(types.InlineKeyboardButton(text="Вода", callback_data="instruction: about_company"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False



# def inline_back_menu(type_of_back):
#     try:
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text="Взять абонемент", callback_data='bottles: economize'))
#         keyboard.add(types.InlineKeyboardButton(text="Повторить последний заказ", callback_data="basket: replay_order"))
#         keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back: ' + type_of_back))
#         return keyboard
#     except Exception as e:
#         print(e)
#     return False





def inline_confirm_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Подтвердить", callback_data="confirm: confirm"))
        keyboard.add(types.InlineKeyboardButton(text="Изменить адрес", callback_data="confirm: change_adress"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_basket_empty_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Заказать", callback_data="start: order_water"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_write_question_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        # keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="start: basket"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_confirm_deliver_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        # keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="start: admin_panel"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False




def inline_pack_bottle_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(*[types.InlineKeyboardButton(text='➖', callback_data='package: minus_of_pack_bottle'),
                       types.InlineKeyboardButton(text='Заказать', callback_data='package: to_order_package'),
                       types.InlineKeyboardButton(text='➕', callback_data='package: plus_of_pack_bottle')])
        keyboard.add(types.InlineKeyboardButton(text="Отменить пакет", callback_data="package: back_to_confirm_order"))
        return keyboard
    except Exception as e:
        print(e)
    return False
# keyboard.add(types.InlineKeyboardButton(text="Ввести другое", callback_data="package: change_the_quantity"))

def inline_confirm_sub_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Подтвердить", callback_data="subs: confirm_sub"))
        keyboard.add(types.InlineKeyboardButton(text="Изменить адрес", callback_data="subs: change_adress"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_subor"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_replay_confirm():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Подтвердить", callback_data="replay: confirm"))
        # keyboard.add(types.InlineKeyboardButton(text="Изменить адрес", callback_data="replay: change_adress"))
        keyboard.add(types.InlineKeyboardButton(text="Отменить", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False


def inline_news_menu():
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Добавить новость", callback_data="news: add"))
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back: back_to_main_menu"))
        return keyboard
    except Exception as e:
        print(e)
    return False









#
# def inline_payment_menu():
#     try:
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text="Оплатить", callback_data="payment: pay_menu"))
#         return keyboard
#     except Exception as e:
#         print(e)
#     return False
