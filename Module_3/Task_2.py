


def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not is_email(recipient) or not is_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return -1

    if recipient == sender:
        print("Нельзя отправить письмо самому себе")
        return -1

    original_sender = "university.help@gmail.com"

    if not original_sender == sender:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса {sender} на адрес {recipient}')
        return 0

    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    return 0


def is_email(email: str):
    if not "@" in email:
        return False

    if not is_domen(email):
        return False

    return True


def is_domen(email : str, substr_list= ('.net', '.com', '.ru')):
    for substr in substr_list:
        check_email = email.find(substr, -len(substr))
        if not check_email == -1:
            return True

    return False


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')