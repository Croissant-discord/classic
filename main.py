from selenium import webdriver
from selenium.webdriver.common.by import By
import http.client
import json 
import sys
import os
import time
import art



def connection(method, url, token):
    conn = http.client.HTTPSConnection("discord.com")
    conn.request(method, url, headers={"Authorization": token, "Content-Type": "application/json"})
    return conn


def display_profile(user_data):
    print("\n==============================")
    print("|   Профиль пользователя     |")
    print("==============================")
    print("|  Имя пользователя:         |")
    print(f"|  {user_data['username']: <25} |")
    print("|----------------------------|")
    print("|  Глобальное имя:           |")
    print(f"|  {user_data['global_name']: <25} |")
    print("|----------------------------|")
    print("|  Локаль:                   |")
    print(f"|  {user_data['locale']: <25} |")
    print("|----------------------------|")
    print("|  Телефон:                  |")
    print(f"|  {user_data['phone'] if user_data['phone'] else 'Нет': <25} |")
    print("|----------------------------|")
    print("|  Электронная почта:        |")
    print(f"|  {user_data['email']: <25} |")
    print("==============================")


def checkprofile(token):
    conn = None
    conn = connection("GET", "/api/v9/users/@me", token)
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read().decode("utf-8"))

        required_keys = ["id", "username", "global_name", "locale", "phone", "email"]
        if all(key in data for key in required_keys):
            display_profile(data)  # assuming you have a display_profile function
            return data
    else:
        print(f"Error: {response.status} {response.reason}")
        return 

    conn.close()


def discord_token_login(token):
    conn = None
    conn = connection("GET", "/api/v9/users/@me", token)
    response = conn.getresponse()

    if response.status == 200:
        url = "https://discord.com/login"
        driver = webdriver.Chrome()
        driver.get(url)

        try:
            codexd = ('function login(token) {setInterval(() => {document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"${token}"`;}, 50);setTimeout(() => {location.reload();}, 2500);}' + " login('" + token + "')")

            driver.execute_script(codexd)

            input("\n[Press Enter To Exit Browser] = >")
            return
        except Exception as e:
            pass

        driver.quit()

    else:
        print(f"Error: {response.status} {response.reason}")
        return


def Boot():
    if len(sys.argv) < 2:
        print("Function name not provided.")
        return
        
    function_name = sys.argv[1]

    if function_name == "C":
        token = sys.argv[2] if len(sys.argv) > 2 else input("Enter Discord token: ")
        checkprofile(token)
        
    elif function_name == "L":
        token = sys.argv[2] if len(sys.argv) > 2 else input("Enter Discord token: ")
        discord_token_login(token)

    elif function_name == "V":
        print("Made By SanseL(.4462)")
        art.tprint("Croissant Modern 1.2")


if __name__ == "__main__":
    Boot()