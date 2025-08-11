from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# 🎬 Har bir bo‘lim uchun kinolar
# 🎬 Har bir bo‘lim uchun kinolar
sections = {
    "🎞 Taksi Film": [
        {"title": "1 qism", "url": "https://fayllar1.ru/1-s-x/Taksi%201%20HD%20O%27zbek%20tilida%20(asilmedia.net).mp4", "poster": "https://via.placeholder.com/150","description": "Kino 1 haqidab yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyz", "text1": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text2": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text3": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "2 qism", "url": "https://fayllar1.ru/1-s-x/Taksi%202%20HD%20O%27zbek%20tilida%20(asilmedia.net).mp4",  "poster": "https://via.placeholder.com/150", "description": "Kino 2 haqida", "text4": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text5": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text6": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "3 qism", "url": "https://fayllar1.ru/1-s-x/Taksi%203%20HD%20O%27zbek%20tilida%20(asilmedia.net).mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 3 haqida", "text7": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text8": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text9": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "4 qism", "url": "https://example.com/kino4.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 4 haqida", "text10": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text11": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text12": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "5 qism", "url": "https://example.com/kino4.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 4 haqida", "text13": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text14": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text15": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0}
    ],
    "🎞 Afsungar Film": [
        {"title": "Kino 5", "url": "https://example.com/kino5.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 5 haqida", "text16": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text2": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text3": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "Kino 6", "url": "https://example.com/kino6.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 6 haqida", "text19": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text20": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text21": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "Kino 7", "url": "https://example.com/kino7.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 7 haqida", "text22": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text23": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text24": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "Kino 8", "url": "https://example.com/kino8.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 8 haqida", "text25": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text26": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text27": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
    ],
    "🎞 Savdoyi posbon Film": [
        {"title": "Kino 9", "url": "https://example.com/kino9.mp4", "poster": "https://via.placeholder.com/150","description": "Kino 9 haqida", "text28": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text29": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text30": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "Kino 10", "url": "https://example.com/kino10.mp4","poster": "https://via.placeholder.com/150","description": "Kino 10 haqida", "text31": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text32": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text33": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
    ],
    "🎞 Terminator Film": [
        {"title": "Kino 11", "url": "https://example.com/kino11.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 11 haqida", "text34": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text35": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text36": "Kino 3 haqidab r4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
        {"title": "Kino 12", "url": "https://example.com/kino12.mp4",  "poster": "https://via.placeholder.com/150","description": "Kino 12 haqida", "text37": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","text38": "Kino 2 haqidab rrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy22","text39": "Kino 3 haqidab hr4rrrrrrrrrrrrryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","views": 0},
    ]
}
# 🌐 Til sozlamalari
translations = {
    "uz": {
        "films": "🎬 Filmlar",
        "stats": "📊 Statistika",
        "language": "📊 Til Tanlash",
        "about": "ℹ️ Biz haqimizda",
        "back": "⬅️ Orqaga",
        "welcome": "🎥 Xush kelibsiz! Quyidagilardan birini tanlang:",
        "choose_section": "🎞 Bo‘limni tanlang:",
        "choose_language": "🌐 Tilni tanlang:",
        "about_text": "📽 Bu bot orqali siz kinolarni tomosha qilishingiz mumkin.",
        "not_found": "❌ Kino topilmadi. Tugmalardan birini tanlang.",
        "stats_text": "📊 Statistika:\n",
        "changed_language": "✅ Til o‘zgartirildi: O‘zbekcha",
        "download": "📥 Yuklab olish"
    },
    "ru": {
        "films": "🎬 Фильмы",
        "stats": "📊 Статистика",
        "language": "📊 Выбрать язык",
        "about": "ℹ️ О нас",
        "back": "⬅️ Назад",
        "welcome": "🎥 Добро пожаловать! Выберите одно из следующих:",
        "choose_section": "🎞 Выберите раздел:",
        "choose_language": "🌐 Выберите язык:",
        "about_text": "📽 С помощью этого бота вы можете смотреть фильмы.",
        "not_found": "❌ Фильм не найден. Пожалуйста, выберите из кнопок.",
        "stats_text": "📊 Статистика:\n",
        "changed_language": "✅ Язык изменён: Русский",
        "download": "📥 Скачать"
    },
    "en": {
        "films": "🎬 Movies",
        "stats": "📊 Statistics",
        "language": "📊 Language",
        "about": "ℹ️ About us",
        "back": "⬅️ Back",
        "welcome": "🎥 Welcome! Choose one of the following:",
        "choose_section": "🎞 Choose a section:",
        "choose_language": "🌐 Choose a language:",
        "about_text": "📽 You can watch movies through this bot.",
        "not_found": "❌ Movie not found. Please choose from buttons.",
        "stats_text": "📊 Statistics:\n",
        "changed_language": "✅ Language changed: English",
        "download": "📥 Download"
    }
}

def get_translation(lang, key):
    return translations.get(lang, translations["uz"]).get(key)

def get_main_markup(lang="uz"):
    t = translations.get(lang, translations["uz"])
    buttons = [
        [KeyboardButton(t["films"])],
        [KeyboardButton(t["stats"])],
        [KeyboardButton(t["language"])],
        [KeyboardButton(t["about"])]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def get_language_buttons():
    buttons = [
        [KeyboardButton("🇺🇿 O‘zbekcha"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English")],
        [KeyboardButton("⬅️ Orqaga")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def get_section_buttons(lang="uz"):
    buttons = [[KeyboardButton(section)] for section in sections]
    buttons.append([KeyboardButton(get_translation(lang, "back"))])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def get_movies_buttons(section_name, lang="uz"):
    buttons = [[KeyboardButton(movie["title"])] for movie in sections[section_name]]
    buttons.append([KeyboardButton(get_translation(lang, "back"))])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "uz")
    await update.message.reply_text(get_translation(lang, "welcome"), reply_markup=get_main_markup(lang))

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    lang = context.user_data.get("language", "uz")
    t = translations.get(lang, translations["uz"])

    if text == "🇺🇿 O‘zbekcha":
        context.user_data["language"] = "uz"
        await update.message.reply_text(translations["uz"]["changed_language"], reply_markup=get_main_markup("uz"))
        return
    elif text == "🇷🇺 Русский":
        context.user_data["language"] = "ru"
        await update.message.reply_text(translations["ru"]["changed_language"], reply_markup=get_main_markup("ru"))
        return
    elif text == "🇬🇧 English":
        context.user_data["language"] = "en"
        await update.message.reply_text(translations["en"]["changed_language"], reply_markup=get_main_markup("en"))
        return

    lang = context.user_data.get("language", "uz")
    t = translations.get(lang, translations["uz"])

    if text == t["films"]:
        context.user_data["last_menu"] = "main"
        await update.message.reply_text(t["choose_section"], reply_markup=get_section_buttons(lang))
        return

    if text == t["stats"]:
        context.user_data["last_menu"] = "main"
        msg = t["stats_text"]
        for section in sections.values():
            for movie in section:
                msg += f"{movie['title']}: {movie['views']}x\n"
        await update.message.reply_text(msg)
        return

    if text == t["language"]:
        context.user_data["last_menu"] = "main"
        await update.message.reply_text(t["choose_language"], reply_markup=get_language_buttons())
        return

    if text == t["about"]:
        context.user_data["last_menu"] = "main"
        await update.message.reply_text(t["about_text"])
        return

    if text == t["back"]:
        last = context.user_data.get("last_menu")
        if last == "sections":
            await update.message.reply_text(t["choose_section"], reply_markup=get_section_buttons(lang))
        else:
            await update.message.reply_text(t["welcome"], reply_markup=get_main_markup(lang))
        context.user_data["last_menu"] = "main"
        return

    if text in sections:
        context.user_data["last_menu"] = "sections"
        context.user_data["current_section"] = text
        await update.message.reply_text(f"{text}:", reply_markup=get_movies_buttons(text, lang))
        return

    for section in sections.values():
        for movie in section:
            if movie["title"] == text:
                movie["views"] += 1
                caption = f"🎬 <b>{movie['title']}</b>\n📝 {movie['description']}"

                for i in range(1, 40):
                    key = f"text{i}"
                    if key in movie:
                        caption += f"\n\nℹ️ {movie[key]}"

                await update.message.reply_photo(photo=movie["poster"], caption=caption, parse_mode='HTML')

                await update.message.reply_text(f"{t['download']}: {movie['url']}")
                return

    await update.message.reply_text(t["not_found"])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token("8318054727:AAFVVX0EP2QRfk2lVhefH_bpQIGfZScZBX4").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    print("🤖 Bot ishga tushdi...")
    app.run_polling()
