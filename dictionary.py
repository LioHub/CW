#!/usr/bin/env python
# coding=utf-8

from button import inline_main_menu
from button import inline_order_water
from button import inline_confirm_menu
from button import inline_location_menu
from button import inline_comment_menu
from button import inline_pre_order_menu
from button import inline_other_goods_menu
from button import inline_pre_payment_menu
from button import inline_order_acsess
from button import inline_sub_menu
from button import inline_cin_abone_menu
from button import inline_confirm_sub_menu
from button import inline_shop_menu
from button import inline_add_else_menu
from button import inline_instruction_menu
from button import inline_write_question_menu
from button import inline_news_menu

provider_token = ''  # - origin
users = {}
prices = {0: []}

menu = {
    1: {'button': inline_main_menu(), 'index': 1},
    2: {'button': inline_order_water('order_water'), 'index': 2},
    3: {'button': inline_order_acsess('order_pompa'), 'index': 3},
    4: {'button': inline_order_acsess('order_pompaEL'), 'index': 4},
    5: {'button': inline_order_acsess('order_culer'), 'index': 5},
    6: {'button': inline_other_goods_menu(), 'index': 6},
    7: {'button': inline_location_menu('d'), 'index': 7},
    8: {'button': inline_confirm_menu(), 'index': 8},
    9: {'button': inline_pre_payment_menu(), 'index': 9},
    10: {'button': inline_comment_menu(), 'index': 10},
    11: {'button': inline_pre_order_menu(), 'index': 11},
    12: {'button': inline_sub_menu(), 'index': 12},
    13: {'button': inline_order_water('subs'), 'index': 13},
    14: {'button': inline_cin_abone_menu('back_to_abonem'), 'index': 14},
    15: {'button': inline_confirm_sub_menu(), 'index': 15},
    16: {'button': inline_shop_menu(), 'index': 16},
    17: {'button': inline_order_acsess('shop'), 'index': 17},
    18: {'button': inline_order_acsess('shop_water'), 'index': 18},
    19: {'button': inline_order_acsess('shop_pompa'), 'index': 19},
    20: {'button': inline_order_acsess('shop_pompaEL'), 'index': 20},
    21: {'button': inline_order_acsess('shop_culer'), 'index': 21},
    22: {'button': inline_add_else_menu(), 'index': 22},
    23: {'button': inline_instruction_menu(), 'index': 23},
    24: {'button': inline_write_question_menu(), 'index': 24},
    25: {'button': inline_write_question_menu(), 'index': 25},
    26: {'button': inline_news_menu(), 'index': 26}
}

product_price = {
    'water': 150,
    'pompa': 450,
    'pompaEL': 1150,
    'culer': 6990

}


product_name = {
    'water': 'Вода 19л',
    'pompa': 'Помпа',
    'pompaEL': 'Помпа электрическая',
    'culer': 'Кулер'
}




sub_price2 = {
    '1_month': {'min_sub': 7, 'term': '1 месяц', 'price': 145},
    '3_months': {'min_sub': 21, 'term': '3 месяц', 'price': 140},
    '6_months': {'min_sub': 42, 'term': '6 месяц', 'price': 130},
    '1_year': {'min_sub': 84, 'term': '1 год', 'price': 120}
}