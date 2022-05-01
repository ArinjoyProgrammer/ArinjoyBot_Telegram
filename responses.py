from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()


    if user_message in ("hi", "hello", "sup"):
        return "Hello there!"

    if user_message in ("who are you", "who are you?"):
        return "I am Arinjoy Bot"

    if user_message in ("time?", "time", "what is the time?", "what is the time", "what is the time now", "what is the time now?"):
        now = datetime.now()
        date_time = now.strftime("Time - %H : %M : %S\nDate - %d / %m / %y")

        return str(date_time)


    return "I can't recognize your message!"