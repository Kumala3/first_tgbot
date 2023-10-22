from aiogram.utils.markdown import hbold


def user_info(user_id: int, username: str):
    user_profile = "\n".join(
        [
            f"{hbold(f'Приветсвую {username}!')}",
            f"{hbold(f'Твой id: {user_id}')}\n",

        ]
    )
    return user_profile
