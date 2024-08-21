# Проверка маски поля ввода почты @gmail.

def valid_mail(str):
    return "@gmail.com" in str

def test_1():
    assert valid_mail("pytest@gmail.com")  # PASS

def test_2():
    assert valid_mail("pytest@gmail,com")  # FAILL