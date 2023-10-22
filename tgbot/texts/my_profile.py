from aiogram.utils.markdown import hbold


def show_start_text(username: str):
    start_text = "\n".join(
        [
            f"{hbold(f'Добро пожаловать {username} !')}",
        ]
    )
    return start_text
