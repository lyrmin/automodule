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
python automodule.py -a n lyrmin.test
start lyrmin.test
python automodule.py -a m lyrmin.test
python automodule.py -a M lyrmin.test
```
Перейдите в список модулей https://partners.1c-bitrix.ru/personal/modules/modules.php и откройте добавленный. Теперь вы можете прописать все необходимые вам настройки.

   [mbx]: <https://marketplace.1c-bitrix.ru>
   [la]: <https://lyrmin.ru/automodule>