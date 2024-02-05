import requests  # Импортируем модуль requests, который позволяет отправлять HTTP-запросы
import fake_useragent  # Импортируем модуль fake_useragent, который генерирует случайный user-agent
from bs4 import BeautifulSoup  # Импортируем класс BeautifulSoup из модуля bs4 для парсинга HTML и XML

user = fake_useragent.UserAgent().random  # Генерируем случайный user-agent
header = {'user-agent': user}  # Создаем заголовок запроса с использованием сгенерированного user-agent

link = "https://browser-info.info.ru"  # Указываем URL-адрес веб-страницы, с которой будем работать
response = requests.get(link, headers=header).text  # Отправляем GET-запрос на указанный URL-адрес с заданным заголовком и получаем текст ответа
soup = BeautifulSoup(response, 'xml')  # Создаем объект BeautifulSoup для парсинга полученного HTML-кода в формате XML
block = soup.find('div', id="tool_padding")  # Находим блок с идентификатором "tool_padding" на странице

check_js = block.find('div', id='javascript_check')  # Находим блок с информацией о JavaScript
status_js = check_js.find_all('span')[1].text  # Извлекаем статус JavaScript
result_js = f'javascript: {status_js}'  # Формируем строку с результатами проверки JavaScript

check_flash = block.find('div', id="flash version")  # Находим блок с информацией о Flash
status_flash = check_flash.find_all('span')[1].text  # Извлекаем статус Flash
result_flash = f'flash: {status_flash}'  # Формируем строку с результатами проверки Flash

check_user = block.find('div', id="user_agent").text  # Находим блок с информацией о User-Agent

print(result_js)  # Выводим результаты проверки JavaScript
print(result_flash)  # Выводим результаты проверки Flash
print(check_user)  # Выводим информацию о User-Agent