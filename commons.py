import datetime
from streamlit import session_state
from models import *


class Us:
    user: User = None


user_id = session_state.get("user_id")
Us.user = Users.get_child(user_id) if user_id else None

print(f"{user_id=}")


def get_ordinal_day(day):
    if 10 <= day % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"


def format_datetime(timestamp: int):
    dt = datetime.datetime.fromtimestamp(timestamp)
    day = get_ordinal_day(dt.day)
    return dt.strftime(f"%A {day} %B %I:%M%p")
