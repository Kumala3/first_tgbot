from aiogram.utils.markdown import hbold

file_send_rules_notifier = "\n".join(
    [
        f"{hbold('1) Отправляя файлы вы соглашаетесь с правилами использования бота')}",
        f"{hbold('2) Отправьте .zip или .rar файл до 20мб (Ограничение Телеграмма) или же отправьте ссылку на файл')}",


    ]
)
