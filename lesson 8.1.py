import re


def email_parse(a):
    if not a:  # проверяем, есть ли значение
        return "ValueError: no mail"
    else:
        b1 = re.findall(r"^\W", a)  # роверяем начало почты
        if len(b1) > 0:
            return "ValueError: wrong email: " + a
        else:
            b2 = re.findall(r"\w+@[a-z]+[.]com", a)
            if len(b2) == 0:
                b3 = re.findall(r"\w+@[a-z]+[.]ru", a)
                if len(b3) == 0:
                    return "ValueError: wrong email: " + a
                else:
                    username = a.split("@")[0]
                    domain = a.split("@")[1]
                    return {'username': username, 'domain': domain}
            else:
                username = a.split("@")[0]
                domain = a.split("@")[1]
                return {'username': username, 'domain': domain}


email_address = input("Введите почту:  ")
print(email_parse(email_address))
