# [Автомодуль][la]: для 1С-Битрикс Управление сайтом...

АвтоМодуль - это незаменимый инструмент разработчика 1С-Битрикс, который экономит десятки часов рутинных действий при создании своих модулей.

Создайте и разместите свой модуль в [marketplace.1c-bitrix.ru][mbx] за 1 минуту.

Приложение позволяет создать и размещестить в [marketplace.1c-bitrix.ru][mbx], свой модуль из консоли без необходимости загружать файлы вручную и использовать веб-интерфейс.

## Возможности
- Создание основы модуля. Дальше вы можете писать логику вашего модуля не тратя время на рутину.
- Создание архива модуля .last_version.zip с автоковертацией кодировки файлов в CP1251.
- Загрузка архива модуля в [marketplace.1c-bitrix.ru][mbx], с автоматическим заполнением необходимых полей.
- Создание архива версии модуля. Создаётся на основании изменений файлов отслеживаемых git status.
- Загрузка архива версии в [marketplace.1c-bitrix.ru][mbx].

## Быстрый старт
### Установка Python
https://www.python.org/downloads/

Windows: Установите в начале галочки - установка под админом и добавить python в PATH.

*nix https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart#step-4-install-additional-tools

### Установка git
https://git-scm.com/downloads

### Запуск скрипта
Рекомендуется скрипт использовать на персональном компьютере, а не на хостинге для простоты установки и настройки ПО.

Важно: Замените lyrmin.test на ваш id модуля.

Для windows выполните команды в консоли
```cmd
cd C:\
git clone https://github.com/lyrmin/automodule.git
cd automodule
git config --global core.autocrlf false
python -m venv venv
python -m pip install -r requirements.txt
python automodule.py -h -r
python automodule.py lyrmin.test -a n
start lyrmin.test
python automodule.py lyrmin.test -a m
python automodule.py lyrmin.test -a M
```
Перейдите в список модулей https://partners.1c-bitrix.ru/personal/modules/modules.php и откройте добавленный. Теперь вы можете прописать все необходимые вам настройки.

Перечень параметров выполнения приложения
```shell
Обяательный аргумент:
  module                ID модуля, пример: lyrmin.test.

Параметры:
  -h, --help            вывести страницу помощи
  -a {n,m,u,M,U}, --action {n,m,u,M,U}
         Выберите действие:
            n — Создание нового модуля.
            m — Создание архива модуля .last_version.zip.
            u — Создание архива версии X.X.X.zip.
            M — Отправка .last_version.zip на marketplace.
            U — Отправка X.X.X.zip на marketplace.
  -P PATH, --path PATH  Указать путь к родительской директории модуля. Пример: /var/www/local/modules
  -v VERSION, --version VERSION
        Указать версию. Пример 1.0.1. Обновит файл version.php
  -d DESCRIPTIONRU, --descriptionru DESCRIPTIONRU
        Установить текст для архива версии description.ru. EOL = #.
  -D DESCRIPTIONEN, --descriptionen DESCRIPTIONEN
        Установить текст для архива версии description.en. EOL = #.
  -u USER, --user USER  Ваш логин в учетной записи на сайте 1c-bitrix.ru.
  -p PASSWORD, --password PASSWORD
        Ваш пароль от учетной записи 1c-bitrix.ru.
  -f, --force
        Принудительное удаление и замена существующие каталоги и файлы модулей.
  -l, --log
        Сохранение лог файлов: module-auth.html, module-result.html, result-error.html для операций -a M или -a U.
  -e EMAIL, --email EMAIL
        Установите email в файл конфигурации .git. Только в момент создания нового модуля.
  -n NAME, --name NAME
        Установите ваше имя для файла конфигурации .git.
  -b BASE, --base BASE
        Установите имя базового модуля вместо lyrmin.base. Например переименовать свой модуль в другой.
  -r, --russian
        Установить Русский язык.
```
Стандартный набор команд:
```shell
python automodule.py lyrmin.news -r -a n -e "myemail@email.ru" -n "Aleksandr Lyrmin"
python automodule.py lyrmin.news -r -a m
python automodule.py lyrmin.news -r -a M -l 
python automodule.py lyrmin.news -a u -r -v1.0.1 -d "Описание версии на русском.#Новая строка." -D "Version description on english.#New line."
python automodule.py lyrmin.news -a U -r -v1.0.1 -l
```

   [mbx]: <https://marketplace.1c-bitrix.ru>
   [la]: <https://lyrmin.ru/automodule>