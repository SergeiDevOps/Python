# Импортируем модуль paramiko для установления защищенного соединения SSH
import paramiko

# Импортируем модуль socket для обмена командами и получения данных
import socket

import time

# Создаем функцию
def send_show_command(
        ip,
        username,
        password,
        enable,
        command,
        max_bytes=60000,
):
# Создаем клиента
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Прописываем политику
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,  # Отключение идентификации по ключам
        allow_agent=False,  # Отключение локального SSH агента
    )
# Создание удаленной программной оболочки invoke_shell и разрешения на доступ
# Установка интерактивной сессии SSH с сервером
    with cl.invoke_shell() as ssh:
        ssh.send("enable\n")  # Отправка данных в сессию
        ssh.send(f"{enable}\n")
        time.sleep(1)
        ssh.send("terminal length 0\n")
        time.sleep(1)
        ssh.recv(max_bytes)  # Получение данных от клиента по средствам модуля socket

        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(5)

            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result[command] = output

        return result
    
# Передача параметров
if __name__ == "__main__":
    devices = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    commands = ["sh clock", "sh arp"]
    result = send_show_command("192.168.100.1", "cisco", "cisco", "cisco", commands)
    print(result, width=120)

# Для записи информации в файл
l = "\n".join(result)
with open("router.csv", "w", encoding="utf-8") as file:
    file.write(l)
