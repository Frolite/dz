
dot_list = ["com", "ru", "net"]

def check_recipient(recipient: str) -> bool:
    if len(recipient.split("@")) > 1:
        for i in dot_list:
            if i in recipient.split("."):
                return True
    return False


def check_sender(sender: str) -> bool:
    if len(sender.split("@")) > 1:
        for i in dot_list:
            if i in sender.split("."):
                return True
    return False
 

def send_email(message: str, recipient: str,* ,sender = "university.help@gmail.com"):
        recipient_ = check_recipient(recipient)
        sender_ = check_sender(sender)
        if recipient_ == True and sender_ == True:
            if sender == recipient:
                print("Нельзя отправить письмо самому себе!\n")
            elif sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}\n")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}\n")
        else:
            print("ERROR\n")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')