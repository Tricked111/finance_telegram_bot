from telebot import types
import my_parse


def command_start(bot):
    @bot.message_handler(commands=["start"])
    def start_command(message):
        bot.send_message(message.chat.id, "Hello!")
        starter(bot, message)


def starter(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_get_info = types.KeyboardButton("get info⁉")
    # item_get_screen =types.KeyboardButton('get screenshot📸')
    item_profit = types.KeyboardButton("calc profit💸")

    markup.add(item_get_info, item_profit)

    return bot.send_message(
        message.chat.id, "❗Select one of the commands❗", reply_markup=markup
    )


def command_info(bot, message):
    value_tinkoff = my_parse.parse_tinkoff()
    value_binance = my_parse.parse_binance()
    val = round(float(float(value_binance) / float(value_tinkoff) * 100 - 100), 2)
    # value_procent = round((val*100-100),2)
    bot.send_message(
        message.chat.id,
        f"Tinkoff USD:  {value_tinkoff}\nBinance SELL:  {value_binance} \nProfit: {val}%",
    )


def command_profit(bot, message):
    markup_profit = types.InlineKeyboardMarkup()
    markup_refresh = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item_get_10 = types.InlineKeyboardButton("30k", callback_data="active_1")
    item_get_20 = types.InlineKeyboardButton("50k", callback_data="active_2")
    item_get_30 = types.InlineKeyboardButton("100k", callback_data="active_3")
    # item_refresh = types.KeyboardButton('again')
    item_back = types.KeyboardButton("back")

    markup_refresh.add(item_back)
    markup_profit.add(item_get_10, item_get_20, item_get_30)
    bot.send_message(message.chat.id, "choose the amount", reply_markup=markup_profit)

    return bot.send_message(message.chat.id, "OR send ", reply_markup=markup_refresh)


def command_answer(bot, message):
    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        if call.data == "active_1":
            calc_profit(bot, float(30000.00), message)
        if call.data == "active_2":
            calc_profit(bot, float(50000.00), message)
        if call.data == "active_3":
            calc_profit(bot, float(100000.00), message)


def calc_profit(bot, val, message):
    value_tinkoff = my_parse.parse_tinkoff()
    value_binance = my_parse.parse_binance()
    profit = round(
        (float(val) / float(value_tinkoff) - 30.0) * 0.982 * float(value_binance), 2
    )

    rozdil = round((profit - val), 2)

    markup_refresh = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_refresh = types.KeyboardButton(str(profit))
    item_back = types.KeyboardButton("back")
    markup_refresh.add(item_refresh, item_back)

    return bot.send_message(
        message.chat.id, f"{profit}\n(+{rozdil})", reply_markup=markup_refresh
    )


def command_sorter(bot):
    @bot.message_handler(content_types=["text"])
    def sort_command(message):
        if message.text == "get info⁉":
            command_info(bot, message)
        elif message.text == "calc profit💸":
            msg = command_profit(bot, message)
            command_answer(bot, message)
            bot.register_next_step_handler(msg, test)
        elif message.text == "help":
            pass

    def test(message):
        try:
            float(message.text)
        except:
            if message.text != "back":
                msg = bot.send_message(message.chat.id, "Enter amount")
                bot.register_next_step_handler(msg, test)
            elif message.text == "back":
                msg = starter(bot, message)
                bot.register_next_step_handler(msg, sort_command)
        else:
            msg = calc_profit(bot, float(message.text), message)
            bot.register_next_step_handler(msg, test)
