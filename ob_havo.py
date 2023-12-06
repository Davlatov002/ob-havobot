from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')
a = requests.get('https://sinoptik.ua/погода-андижан')
html_a = BS(a.content, 'html.parser')
c = requests.get('https://sinoptik.ua/погода-самарканд')
html_c = BS(c.content, 'html.parser')
n = requests.get('https://sinoptik.ua/погода-наманган')
html_n = BS(n.content, 'html.parser')
f = requests.get('https://sinoptik.ua/погода-фергана')
html_f = BS(f.content, 'html.parser')
j = requests.get('https://sinoptik.ua/погода-джизак')
html_j = BS(j.content, 'html.parser')
si = requests.get('https://sinoptik.ua/погода-гулистан')
html_si = BS(si.content, 'html.parser')
q = requests.get('https://sinoptik.ua/погода-карши')
html_q = BS(q.content, 'html.parser')
b = requests.get('https://sinoptik.ua/погода-бухара')
html_b = BS(b.content, 'html.parser')
su = requests.get('https://sinoptik.ua/погода-навои')
html_su = BS(su.content, 'html.parser')
x = requests.get('https://sinoptik.ua/погода-ургенч')
html_x = BS(x.content, 'html.parser')
qo = requests.get('https://sinoptik.ua/погода-нукус')
html_qo = BS(qo.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]

for el in html_a.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    a_min = min[4:]
    a_max = max[5:]
    
for el in html_c.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    c_min = min[4:]
    c_max = max[5:]

for el in html_n.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    n_min = min[4:]
    n_max = max[5:]

for el in html_f.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    f_min = min[4:]
    f_max = max[5:]

for el in html_j.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    j_min = min[4:]
    j_max = max[5:]

for el in html_si.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    si_min = min[4:]
    si_max = max[5:]

for el in html_q.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    q_min = min[4:]
    q_max = max[5:]

for el in html_b.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    b_min = min[4:]
    b_max = max[5:]

for el in html_su.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    su_min = min[4:]
    su_max = max[5:]

for el in html_x.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    x_min = min[4:]
    x_max = max[5:]

for el in html_qo.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    qo_min = min[4:]
    qo_max = max[5:]

def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01")],
        [InlineKeyboardButton("Andijon", callback_data=f"02")],
        [InlineKeyboardButton("Sanarqand", callback_data=f"03")],
        [InlineKeyboardButton("Jizzax", callback_data=f"04")],
        [InlineKeyboardButton("Sirdaryo", callback_data=f"05")],
        [InlineKeyboardButton("Xorazm", callback_data=f"06")],
        [InlineKeyboardButton("Qashqadaryo", callback_data=f"07")],
        [InlineKeyboardButton("Surxandaryo", callback_data=f"08")],
        [InlineKeyboardButton("Namangan", callback_data=f"09")],
        [InlineKeyboardButton("Farg'ona", callback_data=f"10")],
        [InlineKeyboardButton("Buxoro", callback_data=f"11")],
        [InlineKeyboardButton("Qoraqalpog'iston", callback_data=f"12")]
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    elif data[0] == "02":
        query.message.edit_text(f"Bugun Andijon viloyatida havo o`zgarib turadi\nmin {a_min}\nmax "
                                f"{a_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "03":
        query.message.edit_text(f"Bugun Samarqand viloyatida havo o`zgarib turadi\nmin {c_min}\nmax "
                                f"{c_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "04":
        query.message.edit_text(f"Bugun Jizzax viloyatida havo o`zgarib turadi\nmin {j_min}\nmax "
                                f"{j_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "05":
        query.message.edit_text(f"Bugun Sirdaryo viloyatida havo o`zgarib turadi\nmin {si_min}\nmax "
                                f"{si_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "06":
        query.message.edit_text(f"Bugun Xorazm viloyatida havo o`zgarib turadi\nmin {x_min}\nmax "
                                f"{x_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "07":
        query.message.edit_text(f"Bugun Qashqadaryo viloyatida havo o`zgarib turadi\nmin {q_min}\nmax "
                                f"{q_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "08":
        query.message.edit_text(f"Bugun Surxandaryo viloyatida havo o`zgarib turadi\nmin {su_min}\nmax "
                                f"{su_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "09":
        query.message.edit_text(f"Bugun Namangan viloyatida havo o`zgarib turadi\nmin {n_min}\nmax "
                                f"{n_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "10":
        query.message.edit_text(f"Bugun Farg'ona viloyatida havo o`zgarib turadi\nmin {f_min}\nmax "
                                f"{f_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "11":
        query.message.edit_text(f"Bugun Buxoro viloyatida havo o`zgarib turadi\nmin {b_min}\nmax "
                                f"{b_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    elif data[0] == "12":
        query.message.edit_text(f"Bugun Qoraqolpog'iston Respublikasida havo o`zgarib turadi\nmin {qo_min}\nmax "
                                f"{qo_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))




    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))



def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "5749829049:AAF5Dp3z_-KTkuwUgG-KDRARE-09qpvqtx0"
    updater = Updater(Token)
    print('salom')
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

