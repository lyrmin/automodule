#!/home/sdtd/tmp/venv/bin/python3.11
# -*- coding: utf-8 -*-

import argparse
import codecs
import datetime
import errno
import os
import pickle
import re
import shutil
import stat
import subprocess
import sys
import json
from getpass import getpass
from html.parser import HTMLParser
from re import Match
from typing import List, Dict

import requests
from PIL import Image
# Внешние
from colorama import init, Fore


# Языковой класс
class Lang:
    ARGS_DESCRIPTION = ''
    ARGS_ACTION = ''
    ARGS_VERSION = ''
    ARGS_PATH = ''
    ARGS_DESCRIPTIONRU = ''
    ARGS_DESCRIPTIONEN = ''
    ARGS_USER = ''
    ARGS_PASSWORD = ''
    ARGS_FORCE = ''
    ARGS_LOG = ''
    ARGS_EMAIL = ''
    ARGS_NAME = ''
    ARGS_BASE = ''
    ARGS_RUSSIAN = ''
    ARGS_MODULE = ''
    INIT_MODULE_NAME_ERROR = ''
    MODULE_NEW = ''
    MODULE_DOWNLOADING = ''
    MODULE_NEW_REPLACE = ''
    MODULE_NEW_GIT_INIT = ''
    MODULE_ARCHIVE = ''
    MODULE_ARCHIVE_CONVERT_ENCODING = ''
    MODULE_PUSH = ''
    MODULE_PUSH_CODE_ERROR = ''
    MODULE_PUSH_MTYPE_ERROR = ''
    MODULE_PUSH_NAMERU_ERROR = ''
    MODULE_PUSH_DESCRIPTIONRU_ERROR = ''
    MODULE_PUSH_INSTALLRU_ERROR = ''
    MODULE_PUSH_IMAGE_ERROR = ''
    MODULE_PUSH_IMG_ERROR = ''
    MODULE_PUSH_CATEGORY_ERROR = ''
    MODULE_PUSH_LICENSES_ERROR = ''
    MODULE_PUSH_FREEMODULE_ERROR = ''
    MODULE_PUSH_SUCCESS = ''
    MODULE_PUSH_ARCHIVE_ERROR = ''
    MODULE_PUSH_IMAGE_TYPE_ERROR = ''
    MODULE_PUSH_IMAGE_EXT_ERROR = ''
    MODULE_PUSH_IMG_EXT_ERROR = ''
    MODULE_PUSH_CODE_EXIST = ''
    MODULE_PUSH_MODULE_FOUND = ''
    MODULE_PUSH_MODULE_NOT_FOUND = ''
    MODULE_PUSH_USE_FORCE_MODULE_ADD = ''
    MODULE_PUSH_MODULE_ADD = ''
    MODULE_PUSH_MODULE_ID = ''
    MODULE_PUSH_CLASS = ''
    UPDATE_ARCHIVE = ''
    UPDATE_ARCHIVE_GIT_NOT_EXIST = ''
    UPDATE_ARCHIVE_GIT_STATUS = ''
    UPDATE_ARCHIVE_NO_FILES = ''
    UPDATE_ARCHIVE_UPDATE_VERSION_FILE = ''
    UPDATE_ARCHIVE_CREATE_DESCRIPTION_FILE = ''
    UPDATE_ARCHIVE_DESCRIPTION_ERROR = ''
    UPDATE_ARCHIVE_DIRECTORY_READY = ''
    UPDATE_ARCHIVE_READY = ''
    UPDATE_PUSH = ''
    UPDATE_PUSH_ADD = ''
    UPDATE_PUSH_EDIT = ''
    UPDATE_PUSH_SUCCESSFUL = ''
    UPDATE_PUSH_ARCHIVE_NAME_ERROR = ''
    UPDATE_PUSH_ARCHIVE_CONTENTS_ERROR = ''
    UPDATE_PUSH_RU_DESCRIPTION_ERROR = ''
    DIRECTORY_ADD = ''
    DIRECTORY_DELETE = ''
    DIRECTORY_DELETE_ERROR = ''
    DIRECTORY_EXIST = ''
    DIRECTORY_NOT_EXIST = ''
    FILE_EXIST = ''
    FILE_NOT_EXIST = ''
    FILE_ADD = ''
    FILES_TO_COPY = ''
    FILES_TO_DELETE = ''
    GIT_INSTALLATION_ERROR = ''
    GIT_CLONE_ERROR = ''
    RENAME = ''
    COPY = ''
    ERROR = ''
    DONE = ''
    USE_FORCE = ''
    AUTH_SUCCESSFUL = ''
    AUTH_LOGIN_OR_PASSWORD_ERROR = ''
    AUTH_ERROR = ''
    AUTH_COOKIE_ERROR = ''
    USER = ''
    PASSWORD = ''
    VERSION_ERROR = ''
    CONFIG_PATH_ERROR = ''
    CONFIG_FILE_FORMAT_ERROR = ''
    CONFIG_PATH_NOT_EXIST_ERROR = ''

    forceEn = Fore.LIGHTYELLOW_EX + 'Use -f key to force replacement.' + Fore.RESET
    forceRu = Fore.LIGHTYELLOW_EX + 'Используйте параметр -f для принудительной замены.' + Fore.RESET
    errorEn = Fore.RED + 'Error' + Fore.RESET
    errorRu = Fore.RED + 'Ошибка' + Fore.RESET
    lang = {
        "ARGS_DESCRIPTION": {
            "en": Fore.LIGHTCYAN_EX + 'Automodule' + Fore.RESET + ' Creates the basis for the 1C-Bitrix module. And allow automatically create and update modules on marketplace.1c-bitrix.ru for more info: lyrmin.ru/automodule/.',
            "ru": Fore.LIGHTCYAN_EX + 'Automodule' + Fore.RESET + ' Создаёт основу для модулей на 1С-Битрикс. И позволяет в автоматическом режиме создавать и обновлять модули на marketplace.1c-bitrix.ru, подробнее здесь: lyrmin.ru/automodule/.'
        },
        "ARGS_ACTION": {
            "en": 'Choose action: n — Creating new module. m — Making module archive .last_version.zip. u — Making update archive X.X.X.zip. M — Pushing .last_version.zip to the marketplace. U — Pushing X.X.X.zip to the marketplace.',
            "ru": 'Выберите действие: n — Создание нового модуля. m — Создание архива модуля .last_version.zip. u — Создание архива версии X.X.X.zip. M — Отправка .last_version.zip на marketplace. U — Отправка X.X.X.zip на marketplace.'
        },
        "ARGS_VERSION": {
            "en": "Specify the version. Example 1.0.1. Update version.php file",
            "ru": "Указать версию. Пример 1.0.1. Обновит файл version.php"
        },
        "ARGS_PATH": {
            "en": 'Specify the path to the module\'s parent directory. Example: /var/www/local/modules',
            "ru": 'Указать путь к родительской директории модуля. Пример: /var/www/local/modules'
        },
        "ARGS_DESCRIPTIONRU": {
            "en": "Set text for description.ru update archive. EOL = #.",
            "ru": "Установить текст для архива версии description.ru. EOL = #."
        },
        "ARGS_DESCRIPTIONEN": {
            "en": "Set text for description.en update archive. EOL = #.",
            "ru": "Установить текст для архива версии description.en. EOL = #."
        },
        "ARGS_USER": {
            "en": "Your login to 1c-bitrix.ru account.",
            "ru": "Ваш логин в учетной записи на сайте 1c-bitrix.ru."
        },
        "ARGS_PASSWORD": {
            "en": "Your password to 1c-bitrix.ru account.",
            "ru": "Ваш пароль от учетной записи 1c-bitrix.ru."
        },
        "ARGS_FORCE": {
            "en": "Force action. Delete and replace existing module directories and files.",
            "ru": "Принудительное удаление и замена существующие каталоги и файлы модулей."
        },
        "ARGS_LOG": {
            "en": "Save log files: module-auth.html, module-result.html, result-error.html for -a M or -a U.",
            "ru": "Сохранение лог файлов: module-auth.html, module-result.html, result-error.html для операций -a M или -a U."
        },
        "ARGS_EMAIL": {
            "en": "Set email to your .git config file.",
            "ru": "Установите email в файл конфигурации .git."
        },
        "ARGS_NAME": {
            "en": "Set name to your .git config file.",
            "ru": "Установите ваше имя для файла конфигурации .git."
        },
        "ARGS_BASE": {
            "en": "Set base module name instead lyrmin.base. For example to rename your module to another.",
            "ru": "Установите имя базового модуля вместо lyrmin.base. Например переименовать свой модуль в другой."
        },
        "ARGS_RUSSIAN": {
            "en": "Set Russian Language.",
            "ru": "Установить Русский язык."
        },
        "ARGS_MODULE": {
            "en": "Module ID, example: " + Fore.LIGHTCYAN_EX + "lyrmin.test" + Fore.RESET + '.',
            "ru": "ID модуля, пример: " + Fore.LIGHTCYAN_EX + "lyrmin.test" + Fore.RESET + '.'
        },
        "INIT_MODULE_NAME_ERROR": {
            "en": "Module ID " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " is not valid.",
            "ru": "ID модуля " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " указано некорректно."
        },
        "MODULE_NEW": {
            "en": "Creating new module %s",
            "ru": "Создание нового модуля %s"
        },
        "MODULE_DOWNLOADING": {
            "en": "Downloading module from .git",
            "ru": "Загрузка модуля из .git"
        },
        "MODULE_NEW_REPLACE": {
            "en": "Replacing text in files.",
            "ru": "Замена текста в файлах."
        },
        "MODULE_NEW_GIT_INIT": {
            "en": "Creating .git repository for module.",
            "ru": "Создание .git репозитория для модуля."
        },
        "MODULE_ARCHIVE": {
            "en": "Making module archive " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET,
            "ru": "Создание архива модуля " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET
        },
        "MODULE_ARCHIVE_CONVERT_ENCODING": {
            "en": "Convert files to " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET,
            "ru": "Конвертация файлов в " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET
        },
        "MODULE_PUSH": {
            "en": "Pushing %s to the marketplace.",
            "ru": "Загрузка %s на marketplace."
        },
        "MODULE_PUSH_CODE_ERROR": {
            "en": "Module code is not specified in the \"code\" field.",
            "ru": "Не указан код решения в поле \"code\"."
        },
        "MODULE_PUSH_MTYPE_ERROR": {
            "en": "Specify what module includes. Fill in the \"mtype\" field.",
            "ru": "Укажите, что включает в себя решение. Заполните поле \"mtype\"."
        },
        "MODULE_PUSH_NAMERU_ERROR": {
            "en": "The legal name of module in the \"nameRU\" field must be more than 3 characters.",
            "ru": "Юридическое название продукта в поле \"nameRU\" должно быть больше 3 символов."
        },
        "MODULE_PUSH_DESCRIPTIONRU_ERROR": {
            "en": "The description of the module in the \"descriptionRU\" field must be at least 100 characters long.",
            "ru": "Описание решения в поле \"descriptionRU\" должно быть не менее 100 символов."
        },
        "MODULE_PUSH_INSTALLRU_ERROR": {
            "en": "The installation description in the \"INSTALLRU\" field must be at least 100 characters long.",
            "ru": "Описание установки в поле \"INSTALLRU\" должно быть не менее 100 символов."
        },
        "MODULE_PUSH_IMAGE_ERROR": {
            "en": "Required field \"Logo\" is not filled.",
            "ru": "Не заполнено обязательное поле \"Логотип\"."
        },
        "MODULE_PUSH_IMG_ERROR": {
            "en": "Required field \"Screenshots\" is not filled.",
            "ru": "Не заполнено обязательное поле \"Скриншоты\"."
        },
        "MODULE_PUSH_CATEGORY_ERROR": {
            "en": "Specify the categories to which your solution belongs. The \"category\" field is empty.",
            "ru": "Укажите категории, к которым относится ваше решение. Поле \"category\" не заполнено."
        },
        "MODULE_PUSH_LICENSES_ERROR": {
            "en": "Specify the editions that your solution is compatible with. The \"licenses\" field is empty.",
            "ru": "Укажите редакции, с которыми совместимо ваше решение. Поле \"licenses\" не заполнено."
        },
        "MODULE_PUSH_FREEMODULE_ERROR": {
            "en": "\"freeModule\" field not set - \"Free solution\".",
            "ru": "Не установлено поле \"freeModule\" - \"Бесплатное решение\"."
        },
        "MODULE_PUSH_SUCCESS": {
            "en": "Module changed successfully.",
            "ru": "Решение успешно изменено."
        },
        "MODULE_PUSH_ARCHIVE_ERROR": {
            "en": "Invalid contents of the archive with the module. The module must be in the .last_version folder.",
            "ru": "Неверное содержимое архива с модулем. Модуль должен лежать в папке .last_version."
        },
        "MODULE_PUSH_IMAGE_TYPE_ERROR": {
            "en": "Module image saving error: Wrong file type.",
            "ru": "Ошибка сохранения картинки модуля: Неверный тип файла."
        },
        "MODULE_PUSH_IMAGE_EXT_ERROR": {
            "en": "The logo file has the wrong extension.",
            "ru": "Файл с логотипом имеет неверное расширение."
        },
        "MODULE_PUSH_IMG_EXT_ERROR": {
            "en": "The file(s) in the \"Screenshots\" field has(are) the wrong extension.",
            "ru": "Файл(ы) в поле \"Скриншоты\" имеет(ют) неверное расширение."
        },
        "MODULE_PUSH_CODE_EXIST": {
            "en": "Module with this code already exists.",
            "ru": "Решение с таким кодом уже существует."
        },
        "MODULE_PUSH_MODULE_FOUND": {
            "en": "Module " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " found on marketplace.",
            "ru": "Модуль " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " найден на маркетплейс."
        },
        "MODULE_PUSH_MODULE_NOT_FOUND": {
            "en": "Module " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " not found on marketplace.",
            "ru": "Модуль " + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " не найден на маркетплейс."
        },
        "MODULE_PUSH_USE_FORCE_MODULE_ADD": {
            "en": Fore.LIGHTYELLOW_EX + "Use -f key to add new module " + Fore.LIGHTCYAN_EX + "%s" + Fore.LIGHTYELLOW_EX + " to marketplace." + Fore.RESET,
            "ru": Fore.LIGHTYELLOW_EX + "Используйте параметр -f для добавления нового модуля " + Fore.LIGHTCYAN_EX + "%s" + Fore.LIGHTYELLOW_EX + " на маркетплейс." + Fore.RESET
        },
        "MODULE_PUSH_MODULE_ADD": {
            "en": "Adding new module " + Fore.LIGHTCYAN_EX + "%s" + Fore.LIGHTYELLOW_EX + " to marketplace." + Fore.RESET,
            "ru": "Добавление нового модуля " + Fore.LIGHTCYAN_EX + "%s" + Fore.LIGHTYELLOW_EX + " на маркетплейс." + Fore.RESET
        },
        "MODULE_PUSH_MODULE_ID": {
            "en": "$MODULE_ID is incorrect in install/index.php file.",
            "ru": "В файле install/index.php не верно указан $MODULE_ID."
        },
        "MODULE_PUSH_CLASS": {
            "en": "The install/index.php file does not contain the correct class name.",
            "ru": "В файле install/index.php не верно указано имя класса."
        },
        "UPDATE_ARCHIVE": {
            "en": "Making update archive " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET,
            "ru": "Создание архива версии " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET
        },
        "UPDATE_ARCHIVE_GIT_NOT_EXIST": {
            "en": "It is not possible to create a update archive because it is generated automatically based on unstaged files. To view them use the command:" + Fore.LIGHTCYAN_EX + "git status" + Fore.RESET + ".",
            "ru": "Невозможно создать архив версии, т.к. он формируется автоматически на основании неустановленных файлов. Чтобы просмотреть их используйте команду: " + Fore.LIGHTCYAN_EX + "git status" + Fore.RESET + "."
        },
        "UPDATE_ARCHIVE_GIT_STATUS": {
            "en": Fore.LIGHTCYAN_EX + "git status" + Fore.RESET + ":",
            "ru": Fore.LIGHTCYAN_EX + "git status" + Fore.RESET + ":"
        },
        "UPDATE_ARCHIVE_NO_FILES": {
            "en": "There is no files to update.",
            "ru": "Нет файлов для обновления."
        },
        "UPDATE_ARCHIVE_UPDATE_VERSION_FILE": {
            "en": "Updating file install/version.php",
            "ru": "Обновление файла install/version.php"
        },
        "UPDATE_ARCHIVE_CREATE_DESCRIPTION_FILE": {
            "en": "Creating files description.ru and description.en",
            "ru": "Создание файлов description.ru и description.en"
        },
        "UPDATE_ARCHIVE_DESCRIPTION_ERROR": {
            "en": "Add the -d and -D switches and values to create the description.ru and description.en files, respectively.",
            "ru": "Добавьте ключи -d и -D и значения для создания файлов description.ru и description.en соответственно."
        },
        "UPDATE_ARCHIVE_DIRECTORY_READY": {
            "en": "Update directory " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET + " is ready",
            "ru": "Директория версии " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET + " готова"
        },
        "UPDATE_ARCHIVE_READY": {
            "en": "Update archive " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET + " is ready",
            "ru": "Архив версии " + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET + " готов"
        },
        "UPDATE_PUSH": {
            "en": "Pushing %s to the marketplace.",
            "ru": "Загрузка %s на marketplace."
        },
        "UPDATE_PUSH_ADD": {
            "en": "Adding new version.",
            "ru": "Добавление новой версии."
        },
        "UPDATE_PUSH_EDIT": {
            "en": "Edit version.",
            "ru": "Редактирование версии."
        },
        "UPDATE_PUSH_SUCCESSFUL": {
            "en": "The version has been successfully uploaded.",
            "ru": "Версия успешно загружена."
        },
        "UPDATE_PUSH_ARCHIVE_NAME_ERROR": {
            "en": "Invalid archive name.",
            "ru": "Неверное имя архива. "
        },
        "UPDATE_PUSH_ARCHIVE_CONTENTS_ERROR": {
            "en": "Invalid contents of the update archive.",
            "ru": "Неверное содержимое архива с обновлением."
        },
        "UPDATE_PUSH_RU_DESCRIPTION_ERROR": {
            "en": "The description of the update in Russian is not set.",
            "ru": "Не задано описание обновления на русском языке."
        },
        "DIRECTORY_ADD": {
            "en": 'Creating directory ' + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET,
            "ru": 'Создание директории ' + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET
        },
        "DIRECTORY_DELETE": {
            "en": 'Removing directory ' + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET,
            "ru": 'Удаление директории ' + Fore.LIGHTCYAN_EX + '%s' + Fore.RESET
        },
        "DIRECTORY_DELETE_ERROR": {
            "en": errorEn + ' deleting directory %s: %s. ' + forceEn,
            "ru": errorRu + ' при удалении директории %s: %s. ' + forceRu
        },
        "DIRECTORY_EXIST": {
            "en": errorEn + ' directory ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " exists. " + forceEn,
            "ru": errorRu + ' директория ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " существует. " + forceRu
        },
        "DIRECTORY_NOT_EXIST": {
            "en": errorEn + ' directory ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " not exists. ",
            "ru": errorRu + ' директория ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " не существует. "
        },
        "FILE_EXIST": {
            "en": errorEn + ' file ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " exists. " + forceEn,
            "ru": errorRu + ' файл ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " существует. " + forceRu
        },
        "FILE_NOT_EXIST": {
            "en": errorEn + ' file ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " not exists. ",
            "ru": errorRu + ' файл ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET + " не существует. "
        },
        "FILE_ADD": {
            "en": 'Creating file ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET,
            "ru": 'Создание файла ' + Fore.LIGHTCYAN_EX + "%s" + Fore.RESET
        },
        "FILES_TO_COPY": {
            "en": Fore.LIGHTYELLOW_EX + "Files to copy" + Fore.RESET,
            "ru": Fore.LIGHTYELLOW_EX + "Копируемые файлы" + Fore.RESET
        },
        "FILES_TO_DELETE": {
            "en": Fore.LIGHTYELLOW_EX + "Files to delete" + Fore.RESET,
            "ru": Fore.LIGHTYELLOW_EX + "Удаляемые файлы" + Fore.RESET
        },
        "GIT_INSTALLATION_ERROR": {
            "en": ".git is not installed",
            "ru": ".git не установлен"
        },
        "GIT_CLONE_ERROR": {
            "en": errorEn + " .git clone repository: %s",
            "ru": errorRu + " клонирования .git репозитория: %s"
        },
        "RENAME": {
            "en": 'Rename %s to %s',
            "ru": 'Переименование %s в %s'
        },
        "COPY": {
            "en": 'Copy %s to %s',
            "ru": 'Копирование %s в %s'
        },
        "ERROR": {
            "en": errorEn + " %s",
            "ru": errorRu + " %s"
        },
        "DONE": {
            "en": Fore.LIGHTGREEN_EX + "done" + Fore.RESET,
            "ru": Fore.LIGHTGREEN_EX + "готово" + Fore.RESET
        },
        "USE_FORCE": {
            "en": forceEn,
            "ru": forceRu
        },
        "AUTH_SUCCESSFUL": {
            "en": "Auth successful.",
            "ru": "Успешная авторизация."
        },
        "AUTH_LOGIN_OR_PASSWORD_ERROR": {
            "en": "Wrong login or password.",
            "ru": "Неверный логин или пароль."
        },
        "AUTH_ERROR": {
            "en": "The user is not authorized.",
            "ru": "Пользователь не авторизован."
        },
        "AUTH_COOKIE_ERROR": {
            "en": "Authorization is done via COOKIE.",
            "ru": "Авторизация через COOKIE не выполнена."
        },
        "USER": {
            "en": "User: ",
            "ru": "Пользователь: "
        },
        "PASSWORD": {
            "en": "Password: ",
            "ru": "Пароль: "
        },
        "VERSION_ERROR": {
            "en": "Update version not specified in X.X.X format. " + Fore.LIGHTCYAN_EX + "Use -v to specify the version." + Fore.RESET,
            "ru": "Не указана версия обновления в формате X.X.X. " + Fore.LIGHTCYAN_EX + "Используйте -v для указания версии." + Fore.RESET
        },
        "CONFIG_PATH_ERROR": {
            "en": errorEn + ' the path: %s is incorrect in the configuration',
            "ru": errorRu + ' в конфигурации не верно указан путь: %s'
        },
        "CONFIG_FILE_FORMAT_ERROR": {
            "en": errorEn + ' invalid configuration file format: %s',
            "ru": errorRu + ' не верный формат файла конфигурации: %s'
        },
        "CONFIG_PATH_NOT_EXIST_ERROR": {
            "en": errorEn + ' the path: %s is not exists',
            "ru": errorRu + ' путь: %s не существует.'
        },
    }

    def __init__(self) -> None:
        language = "en"
        if '-r' in sys.argv or '--russian' in sys.argv:
            language = "ru"
        for key, value in self.lang.items():
            self.__dict__[key] = value[language]


# Обработчик страниц маркетплейса
class BXMarketplacePageParser(HTMLParser):
    form: Dict[str, str] = {}
    list: List[dict] = []
    forms: List[dict] = []
    allowTags: List[str] = ['input', 'button', 'select', 'option', 'optgroup', 'textarea']
    result: List[tuple] = []

    def handle_starttag(self, tag: str, attrs: List) -> None:
        attrDict = {}
        for key, value in attrs:
            attrDict[key] = value

        self.getData(tag, attrDict)

    def handle_endtag(self, tag: str) -> None:
        if tag == 'form':
            self.forms.append({'attrs': self.form, 'list': self.list})
            self.form = {}
            self.list = []

    def getData(self, tag: str, attrs: Dict) -> None:
        if tag == 'form':
            self.form = attrs
            self.list = []
        elif self.form and (tag in self.allowTags):
            attrs['tag'] = tag
            self.list.append(attrs)

    # Получение формы по аттрибутам
    def getForm(self, selector: Dict) -> List:
        searchForm = {}
        name: str = ''

        for form in self.forms:
            if form['attrs']:
                for key in selector:
                    value = selector[key]
                    if (key in form['attrs']) and (form['attrs'][key] == value):
                        searchForm = form

        # Загрузка полей формы в словарь
        for field in searchForm['list']:
            tag = field['tag']

            if 'name' in field:
                name = field['name']

            if tag == 'optgroup':
                continue

            if tag == 'option' and 'selected' not in field:
                continue

            if 'disabled' in field:
                continue

            if 'type' in field and field['type'] == 'checkbox' and 'checked' not in field:
                continue

            if tag == 'select':
                continue

            if 'value' not in field:
                continue

            value = field['value']

            self.result.append(tuple((name, value)))

        return self.result

    # Получение данных для полей визуального редактора
    def getJSFields(self, html: str) -> List:
        fields = []
        jsFields = ['descriptionRU', 'INSTALLRU', 'SUPPORTRU', 'EULA_LINK']
        field = None
        regex = "(?:(?:var config.*)(descriptionRU)(?:.*?;$)(?:\W*\w*\W\w* = ')(.*?(?=';)))|(?:(?:var config.*)(INSTALLRU)(?:.*?;$)(?:\W*\w*\W\w* = ')(.*?(?=';)))|(?:(?:var config.*)(SUPPORTRU)(?:.*?;$)(?:\W*\w*\W\w* = ')(.*?(?=';)))|(?:(?:var config.*)(EULA_LINK)(?:.*?;$)(?:\W*\w*\W\w* = ')(.*?(?=';)))"
        matches = re.finditer(regex, html, re.MULTILINE | re.IGNORECASE)
        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                group = match.group(groupNum)
                if group in jsFields:
                    field = group
                elif field:
                    fields.append(tuple((field, re.sub(r'\\{1,}n', '\n', group))))
                    field = None

        return fields


# Основной класс: АВТОМОДУЛЬ
class AutoModule:
    base = "lyrmin.base"
    currentDir = os.path.abspath(os.path.dirname(__file__))
    encodeBase = 'utf-8'
    encode = 'cp1251'
    lastVersionDir = ".last_version"
    lastVersionFile = ".last_version.zip"
    updaterFile = "updater.php"
    versionDir = "1.0.1"
    versionFile = "1.0.1.zip"
    gitDir = '.git'
    cookieFile = 'cookie'
    session = None
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    resultCode = None
    resultValue = None
    resultText = None

    def __init__(self) -> None:
        self.lang = Lang()
        args = self.getArguments()

        tmp = args.module.split('.')
        self.module = args.module

        if not self.checkModuleName():
            print(self.lang.INIT_MODULE_NAME_ERROR % self.module)
            exit()

        self.partnerId = tmp[0]
        self.moduleId = tmp[1]
        del tmp

        self.action = args.action
        self.user = args.user
        self.password = args.password
        self.version = args.version
        if self.version:
            self.versionFile = self.version + ".zip"
            self.versionDir = self.version

        self.descriptionRu = args.descriptionru
        self.descriptionEn = args.descriptionen
        self.force = args.force
        self.log = args.log
        self.email = args.email
        self.name = args.name

        if args.base:
            self.base = args.base

        self.baseUnderscore = self.base.replace('.', '_')
        self.moduleUnderscore = self.module.replace('.', '_')
        self.baseLockPrefix = self.baseUnderscore.upper()
        self.moduleLockPrefix = self.moduleUnderscore.upper()
        self.baseNameSpace = self.base.title().replace('.', '\\')
        self.moduleNameSpace = self.module.title().replace('.', '\\')
        self.baseNameSpaceDouble = self.base.title().replace('.', '\\\\')
        self.moduleNameSpaceDouble = self.module.title().replace('.', '\\\\')

        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.getConfig(args)
        if not self.currentDir == os.path.abspath(os.path.dirname(__file__)):
            os.chdir(self.currentDir)

    def getConfig(self, args) -> None:
        configFile = 'config.json'
        configPath = os.path.join(self.currentDir, configFile)

        # Файл config.json не существует
        if not os.path.exists(configPath):
            config = {}
        else:
            with open(configFile, 'r', encoding=self.encodeBase) as f:
                try:
                    config = json.load(f)
                    if self.partnerId in config:
                        if self.moduleId in config[self.partnerId]:
                            if 'currentDir' in config[self.partnerId][self.moduleId]:
                                path = config[self.partnerId][self.moduleId]['currentDir']
                                if os.path.exists(path):
                                    self.currentDir = path
                                else:
                                    print(self.lang.CONFIG_PATH_ERROR % path)
                                    exit()
                except ValueError as error:
                    print(self.lang.CONFIG_FILE_FORMAT_ERROR % error)
                    exit()

        # Сохранение файла config.json
        if args.path:
            if os.path.exists(args.path):
                if self.partnerId not in config:
                    config[self.partnerId] = {self.moduleId: {'currentDir': args.path}}
                elif self.moduleId not in config[self.partnerId]:
                    config[self.partnerId][self.moduleId] = {'currentDir': args.path}

                if not self.currentDir == args.path:
                    config[self.partnerId][self.moduleId]['currentDir'] = args.path
                    with open(configFile, 'w', encoding=self.encodeBase) as f:
                        json.dump(config, f, ensure_ascii=False, indent=4)
                    self.currentDir = args.path
            else:
                print(self.lang.CONFIG_PATH_NOT_EXIST_ERROR % args.path)
                exit()

    # Выбирает действие на основании параметра action
    def doAction(self) -> None:
        if self.action == 'n':
            self.moduleNewAction()
        elif self.action == 'm':
            self.moduleArchiveAction()
        elif self.action == 'u':
            self.updateArchiveAction()
        elif self.action == 'M':
            self.modulePushAction()
        elif self.action == 'U':
            self.updatePushAction()

        print(self.lang.DONE)

    # Создаёт новый модуль
    def moduleNewAction(self) -> bool:
        print(self.lang.MODULE_NEW % self.module)

        # Удаление директории модуля
        if os.path.exists(self.module):
            if self.force:
                try:
                    shutil.rmtree(self.module, onerror=self.removeReadonly)
                except OSError as error:
                    print(self.lang.DIRECTORY_DELETE_ERROR % (self.module, error))
                    return False
            else:
                print(self.lang.DIRECTORY_EXIST % self.module)
                return False

        # Удаление ранее скачанной основы модуля
        if os.path.exists(self.base):
            try:
                shutil.rmtree(self.base, onerror=self.removeReadonly)
            except OSError as error:
                print(self.lang.DIRECTORY_DELETE_ERROR % (self.base, error))
                return False

        # Загрузка репозитория с основой модуля
        try:
            print(self.lang.MODULE_DOWNLOADING)
            subprocess.run(['git', 'clone', 'https://lyrmin@bitbucket.org/lyrmin/lyrmin.base.git'], check=True, shell=True)
        except subprocess.CalledProcessError as error:
            if (error.returncode == 1):
                print(self.lang.GIT_INSTALLATION_ERROR)
            else:
                print(self.lang.GIT_CLONE_ERROR % error)
            return False

        # Удаление репозитория
        gitPath = os.path.join(self.base, self.gitDir)
        try:
            shutil.rmtree(gitPath, onerror=self.removeReadonly)
        except OSError as error:
            print(self.lang.DIRECTORY_DELETE_ERROR % (gitPath, error))
            return False

        # Переименование рекурсивно директорий lyrmin.base в название нового модуля например lyrmin.test
        if os.path.exists(self.base):
            for root, dirs, files in os.walk(self.base):
                for dirName in dirs:
                    if dirName != self.base:
                        continue
                    oldPath = os.path.join(root, dirName)
                    newPath = os.path.join(root, dirName.replace(self.base, self.module))
                    print(self.lang.RENAME % (
                        re.sub(r'~^' + self.base + os.sep + '~', '', oldPath),
                        re.sub(r'~^' + self.base + os.sep + '~', '', newPath))
                          )
                    os.rename(oldPath, newPath)

            print(self.lang.RENAME % (self.base, self.module))
            os.rename(os.path.join(self.currentDir, self.base), os.path.join(self.currentDir, self.module))
        else:
            print(self.lang.DIRECTORY_NOT_EXIST % self.base)
            return False

        # Замена текста в файлах
        arFind = [self.base, self.baseUnderscore, self.baseLockPrefix, self.baseNameSpace, self.baseNameSpaceDouble]
        arReplace = [self.module, self.moduleUnderscore, self.moduleLockPrefix, self.moduleNameSpace,
                     self.moduleNameSpaceDouble]

        if not os.path.exists(self.module):
            print(self.lang.DIRECTORY_NOT_EXIST % self.module)
            return False
        print(self.lang.MODULE_NEW_REPLACE)
        for root, dirs, files in os.walk(self.module):
            for fileName in files:
                filePath = os.path.join(root, fileName)
                file = codecs.open(filePath, "rb", self.encodeBase)
                text = file.read()
                file.close()
                srcText = text
                for i in range(len(arFind)):
                    text = text.replace(arFind[i], arReplace[i])
                if srcText != text:
                    file = open(filePath, "wb")
                    file.write(text.encode())
                    file.close()

        # Создание репозитория в директории модуля
        try:
            print(self.lang.MODULE_NEW_GIT_INIT)
            os.chdir(self.module)
            if self.email:
                subprocess.run(['git', 'config', '--global', 'user.email', self.email])
            if self.name:
                subprocess.run(['git', 'config', '--global', 'user.name', self.name])
            subprocess.run(['git', 'init', '--quiet'])
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', '"init module"', '--quiet'])
        except subprocess.CalledProcessError as error:
            if error.returncode == 1:
                print(self.lang.GIT_INSTALLATION_ERROR)
            else:
                print(self.lang.ERROR + "%s" % error)

        return True

    # Создаёт архив: .last_version.zip
    def moduleArchiveAction(self):
        print(self.lang.MODULE_ARCHIVE % self.lastVersionFile)

        if not os.path.exists(self.module):
            print(self.lang.DIRECTORY_NOT_EXIST % self.module)
            return False

        if os.path.exists(self.lastVersionFile) and not self.force:
            print(self.lang.FILE_EXIST % self.lastVersionFile)
            return False

        if os.path.exists(self.lastVersionDir):
            if self.force:
                print(self.lang.DIRECTORY_DELETE % self.lastVersionDir)
                shutil.rmtree(self.lastVersionDir)
            else:
                print(self.lang.DIRECTORY_EXIST % self.lastVersionDir, end='')
                print(self.lang.USE_FORCE)
                return False

        # Создание директории .last_version
        print(self.lang.DIRECTORY_ADD % self.lastVersionDir)
        os.makedirs(self.lastVersionDir)

        # Конвертация файлов в кодировку cp1251
        print(self.lang.MODULE_ARCHIVE_CONVERT_ENCODING % self.encode)
        for root, dirs, files in os.walk(self.module):
            for fileName in files:
                fromFile = os.path.join(root, fileName)
                if fromFile.startswith(os.path.join(self.module, self.gitDir)):
                    continue

                rootLastVersion = os.path.join(self.lastVersionDir, root[len(self.module + '/'):])
                toFile = os.path.join(rootLastVersion, fileName)

                self.copyAndConvertFile(fromFile, toFile, self.encodeBase, self.encode)

        # Удаление файла .last_version/updater.php
        updaterPath = os.path.join(self.lastVersionDir, self.updaterFile)
        if os.path.exists(updaterPath):
            os.remove(updaterPath)

        # Архивация файлов
        print(self.lang.FILE_ADD % self.lastVersionFile)
        shutil.make_archive(self.lastVersionDir, 'zip', '.', self.lastVersionDir)

        # Удаление временной директории
        print(self.lang.DIRECTORY_DELETE % self.lastVersionDir)
        shutil.rmtree(self.lastVersionDir)

    # Проверяет модуль новый на маркетплейс или существует
    def moduleIsNew(self, formFields):
        for field, value in formFields:
            if field == 'ID':
                return value == ""

    def moduleUpdateField(self, formFields, fieldCheck, valueCheck, add=True):
        result = []

        for field, value in formFields:
            if fieldCheck == field:
                if not value:
                    value = valueCheck
                if add:
                    result.append(tuple((fieldCheck, value)))
                continue
            result.append(tuple((field, value)))

        return result

    # Загружает архив модуля .last_version.zip в marketplace
    def modulePushAction(self):
        print(self.lang.MODULE_PUSH % self.lastVersionFile)

        # Проверка наличия файла
        if not os.path.exists(self.lastVersionFile):
            print(self.lang.FILE_NOT_EXIST % self.lastVersionFile)
            return False

        # Авторизация через форму авторизации
        user = self.user
        password = self.password
        urlNew = 'https://partners.1c-bitrix.ru/personal/modules/edit.php'
        # urlNew = 'https://lyrmin.ru/test2/marketplace.php'
        url = urlNew + '?ID=' + self.module

        check = {
            'success': {
                'Маркетплейс 1С-Битрикс': self.lang.AUTH_SUCCESSFUL
            },
            'error': {
                'Неверный логин или пароль.': self.lang.AUTH_LOGIN_OR_PASSWORD_ERROR,
                'Войти на сайт': self.lang.AUTH_ERROR,
            }
        }

        if html := self.loginByForm(url, user, password, check):
            if self.log:
                file = codecs.open("module-auth.html", "w", self.encodeBase)
                file.write(html)
                file.close()

            print(self.resultText)

            if self.resultCode == "error":
                return False

            logoFile = 'logo.png'
            if not os.path.exists(logoFile):
                img = Image.new('RGB', (135, 135), (255, 255, 255))
                img.save(logoFile, "PNG")

            logo = open(logoFile, "rb")
            files = []
            errors = {
                'code': {
                    'error': 'Укажите код решения.',
                    'value': self.moduleId,
                    'text': self.lang.MODULE_PUSH_CODE_ERROR
                },
                'mtype[]': {
                    'error': 'Укажите, что включает в себя решение.',
                    'value': ['2'],
                    'text': self.lang.MODULE_PUSH_MTYPE_ERROR
                },
                'nameRU': {
                    'error': 'Юридическое название продукта должно быть больше 3 символов.',
                    'value': self.module,
                    'text': self.lang.MODULE_PUSH_NAMERU_ERROR
                },
                'descriptionRU': {
                    'error': 'Описание решения должно быть не менее 100 символов.',
                    'value': (self.module + '\n') * 20,
                    'text': self.lang.MODULE_PUSH_DESCRIPTIONRU_ERROR
                },
                'INSTALLRU': {
                    'error': 'Описание установки должно быть не менее 10 символов.',
                    'value': (self.module + '\n') * 20,
                    'text': self.lang.MODULE_PUSH_INSTALLRU_ERROR
                },
                'IMAGE': {
                    'error': 'Не заполнено обязательное поле "Логотип"',
                    'value': '',
                    'text': self.lang.MODULE_PUSH_IMAGE_ERROR
                },
                'IMG[]': {
                    'error': 'Не заполнено обязательное поле "Скриншоты"',
                    'value': '',
                    'text': self.lang.MODULE_PUSH_IMG_ERROR
                },
                'category[]': {
                    'error': 'Укажите категории, к которым относится ваше решение.',
                    'value': ['124'],
                    'text': self.lang.MODULE_PUSH_CATEGORY_ERROR
                },
                'licenses[]': {
                    'error': 'Укажите редакции, с которыми совместимо ваше решение.',
                    'value': ['45'],
                    'text': self.lang.MODULE_PUSH_IMG_ERROR
                },
                'freeModule': {
                    'error': 'Цена решения не может быть ниже 1000 рублей.',
                    'value': 'Y',
                    'text': self.lang.MODULE_PUSH_FREEMODULE_ERROR
                }
            }

            # Получение данных формы
            page = BXMarketplacePageParser()
            page.feed(html)
            formFields = page.getForm({'id': 'EDIT_MODULE'})
            formFields += page.getJSFields(html)
            formFields.append(tuple(('apply', 'Y')))

            isNew = self.moduleIsNew(formFields)

            if not isNew:
                print(self.lang.MODULE_PUSH_MODULE_FOUND % self.module)
            elif self.force:
                print(self.lang.MODULE_PUSH_MODULE_ADD % self.module)
                url = urlNew
            else:
                print(self.lang.ERROR % '', end='')
                print(self.lang.MODULE_PUSH_MODULE_NOT_FOUND % self.module)
                print(self.lang.MODULE_PUSH_USE_FORCE_MODULE_ADD % self.module)
                return False

            for field, data in errors.items():
                value = data["value"]

                if field in ["IMAGE", "IMG[]"]:
                    formFields = self.moduleUpdateField(formFields, field, "", False)
                else:
                    formFields = self.moduleUpdateField(formFields, field, value)

            if isNew:
                files.append(tuple(("IMAGE", (logoFile, logo, 'image/png'))))
                files.append(tuple(("IMG[]", (logoFile, logo, 'image/png'))))
            else:
                formFields = self.moduleUpdateField(formFields, "code", "", False)

            # Отправка данных формы
            check = {
                'success': {'Решение успешно изменено.': self.lang.MODULE_PUSH_SUCCESS},
                'error': {
                    'Неверное содержимое архива с модулем. Модуль должен лежать в папке .last_version.': self.lang.MODULE_PUSH_ARCHIVE_ERROR,
                    'Ошибка сохранения картинки модуля: Неверный тип файла': self.lang.MODULE_PUSH_IMAGE_TYPE_ERROR,
                    'Файл с логотипом имеет неверное расширение': self.lang.MODULE_PUSH_IMAGE_EXT_ERROR,
                    'Файл(ы) в поле "Скриншоты" имеет(ют) неверное расширение': self.lang.MODULE_PUSH_IMG_EXT_ERROR,
                    'Решение с таким кодом уже существует.': self.lang.MODULE_PUSH_CODE_EXIST,
                    'В файле install/index.php не верно указан $MODULE_ID': self.lang.MODULE_PUSH_MODULE_ID,
                    'В файле install/index.php не верно указано имя класса': self.lang.MODULE_PUSH_CLASS,
                    'Укажите, что включает в себя решение.': 'Укажите, что включает в себя решение.',
                    'Не заполнено обязательное поле "Скриншоты"': 'Не заполнено обязательное поле "Скриншоты"',
                    'Укажите категории, к которым относится ваше решение.': 'Укажите категории, к которым относится ваше решение.',
                    'Укажите редакции, с которыми совместимо ваше решение.': 'Укажите редакции, с которыми совместимо ваше решение.'
                }
            }
            files.append(tuple(("update", (self.lastVersionFile, open(self.lastVersionFile, "rb")))))

            html = self.sendForm(url, check, formFields, files)

            if self.log:
                file = codecs.open("module-upload.html", "w", self.encodeBase)
                file.write(html)
                file.close()

            if self.resultCode == 'error':
                if self.resultText:
                    print(self.lang.ERROR % '', end='')
                    print(self.resultText)

                for field, data in errors.items():
                    error = data['error']
                    errorText = data['text']
                    if error in html:
                        print(Fore.LIGHTRED_EX + 'Error field' + Fore.RESET + ':', field, errorText)
                return False
            else:
                print(self.resultText)
        return True

    # Создаёт архив версии X.X.X.zip
    # https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=101&LESSON_ID=3218
    # http://bxapi.ru/?module_id=main&class=CUpdater
    def updateArchiveAction(self):
        print(self.lang.UPDATE_ARCHIVE % self.versionFile)

        encoding = sys.getdefaultencoding()

        if not self.version:
            print(self.lang.ERROR % self.lang.VERSION_ERROR)
            return False

        # Удаление и создание директории X.X.X
        if os.path.exists(self.versionDir):
            if self.force:
                shutil.rmtree(self.versionDir)
            else:
                print(self.lang.DIRECTORY_EXIST % self.versionDir, end='')
                print(self.lang.USE_FORCE)
                return False

        os.chdir(self.module)

        # Проверка существования .git директории
        if not os.path.exists(self.gitDir):
            print(self.lang.DIRECTORY_NOT_EXIST % self.gitDir, end='')
            print(self.lang.UPDATE_ARCHIVE_GIT_NOT_EXIST)
            return False

        # Получение списка изменённых файлов
        try:
            updateFiles = subprocess.run(['git', 'ls-files', '-dmo'], capture_output=True, text=True).stdout.strip()
        except subprocess.CalledProcessError as error:
            if error.returncode == 1:
                print(self.lang.GIT_INSTALLATION_ERROR)
            else:
                print(self.lang.ERROR + " .git ls-files: %s" % error)
            return False

        if len(updateFiles) == 0:
            print(self.lang.UPDATE_ARCHIVE_NO_FILES)
            print(self.lang.UPDATE_ARCHIVE_GIT_STATUS)
            subprocess.run(['git', 'status'], check=True)
            return False

        os.chdir('..')
        os.makedirs(self.versionDir)

        # Обновление файла version.php
        print(self.lang.UPDATE_ARCHIVE_UPDATE_VERSION_FILE)
        self.makeVersionFile()

        # Создание файлов description.ru и description.en
        print(self.lang.UPDATE_ARCHIVE_CREATE_DESCRIPTION_FILE)
        if not self.makeDescriptionFiles():
            return False

        os.chdir(self.module)

        # Проверка на наличие изменённых файлов
        filesModified = subprocess.run(['git', 'ls-files', '-m'], capture_output=True, text=True).stdout.strip().replace('/', os.sep).split('\n')
        filesModified = list(filter(None, filesModified))
        filesAdded = subprocess.run(['git', 'ls-files', '-o'], capture_output=True, text=True).stdout.strip().replace('/', os.sep).split('\n')
        filesAdded = list(filter(None, filesAdded))
        filesDeleted = subprocess.run(['git', 'ls-files', '-d'], capture_output=True, text=True).stdout.strip().replace('/', os.sep).split('\n')
        filesDeleted = list(filter(None, filesDeleted))

        # Исключение из модифицированных файлов удалённые файлы
        filesModified = list(set(filesModified) - set(filesDeleted))

        copyFiles = filesModified + filesAdded
        copyFiles = list(dict.fromkeys(copyFiles))
        deleteFiles = filesDeleted

        os.chdir('..')

        if copyFiles:
            print(self.lang.FILES_TO_COPY)
            for filePath in copyFiles:
                fromFile = os.path.join(self.module, filePath)
                toFile = os.path.join(self.versionDir, filePath)
                print(self.lang.COPY % (fromFile, toFile))
                self.copyAndConvertFile(fromFile, toFile, self.encodeBase, self.encode)

        # Прописывает команды на удаление файлов в updater.php
        if deleteFiles:
            print(self.lang.FILES_TO_DELETE)
            textPostfix = ''
            for filePath in deleteFiles:
                print(filePath)
                textPostfix = textPostfix + 'unlink($_SERVER[\'DOCUMENT_ROOT\'] . BX_ROOT . DIRECTORY_SEPARATOR . \'modules\' . DIRECTORY_SEPARATOR . \'' + self.module + '\' . DIRECTORY_SEPARATOR . \'' + filePath + '\');\n'

            # Создать updater.php в случае отсутствия или дополнить файлами для удаления
            self.makeUpdater(textPostfix)

        print(self.lang.UPDATE_ARCHIVE_DIRECTORY_READY % self.versionDir)

        # Архивация обновления
        if os.path.exists(self.versionFile):
            if self.force:
                print(self.lang.UPDATE_ARCHIVE_READY % self.versionFile)
            else:
                print(self.lang.FILE_EXIST % self.versionFile, end='')
                print(self.lang.USE_FORCE)
                return False

        shutil.make_archive(self.versionDir, 'zip', '.', self.versionDir)

    # Загружает архив версии модуля X.X.X.zip в marketplace
    def updatePushAction(self):
        print(self.lang.UPDATE_PUSH % self.versionFile)

        if not self.version:
            print(self.lang.ERROR % self.lang.VERSION_ERROR)
            return False

        user = self.user
        password = self.password
        version = self.version

        urlNewVersion = 'https://partners.1c-bitrix.ru/personal/modules/deploy.php?ID=' + self.module
        urlEditVersion = urlNewVersion + '&ver=' + version

        # Проверка наличия файла
        if not os.path.exists(self.versionFile):
            print(self.lang.FILE_NOT_EXIST % self.versionFile)
            return False

        check = {
            'success': {
                'name="edit_update"': self.lang.AUTH_SUCCESSFUL,
                'Версия решения не найдена': self.lang.AUTH_SUCCESSFUL
            },
            'error': {
                'Неверный логин или пароль.': self.lang.AUTH_LOGIN_OR_PASSWORD_ERROR,
                'Войти на сайт': self.lang.AUTH_ERROR,
            }
        }

        if html := self.loginByForm(urlEditVersion, user, password, check):
            if self.log:
                file = codecs.open("update-auth.html", "w", self.encodeBase)
                file.write(html)
                file.close()

            if self.resultCode == "error":
                return False

            if self.resultValue == 'Версия решения не найдена':
                print(self.lang.UPDATE_PUSH_ADD)
                html = self.loginByForm(urlNewVersion, user, password, check)
                url = urlNewVersion
            else:
                print(self.lang.UPDATE_PUSH_EDIT)
                url = urlEditVersion

            # Получение данных формы
            page = BXMarketplacePageParser()
            page.feed(html)
            formFields = page.getForm({'name': 'edit_update'})
            formFields += page.getJSFields(html)
            formFields.append(tuple(('apply', 'Y')))
            formFields = self.moduleUpdateField(formFields, 'submit', '', False)

            files = []
            files.append(tuple(("update", (self.versionFile, open(self.versionFile, "rb")))))

            # Отправка данных формы
            check = {
                'success': {
                    'Обновление успешно изменено.': self.lang.UPDATE_PUSH_SUCCESSFUL
                },
                'error': {
                    'Неверное имя архива.': self.lang.UPDATE_PUSH_ARCHIVE_NAME_ERROR,
                    'Неверное содержимое архива с обновлением.': self.lang.UPDATE_PUSH_ARCHIVE_CONTENTS_ERROR,
                    'Не задано описание обновления на русском языке.': self.lang.UPDATE_PUSH_RU_DESCRIPTION_ERROR
                }
            }

            html = self.sendForm(url, check, formFields, files)
            if self.resultCode == 'success':
                print(self.resultText)
            else:
                print(self.lang.ERROR % '', end='')
                print(self.resultText)

            if self.log:
                file = codecs.open("update-result.html", "w", self.encodeBase)
                file.write(html)
                file.close()

            return self.resultCode == 'success'

    # Дополнительные методы

    # Обрабатывает аргументы
    def getArguments(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(prog='automodule', description=self.lang.ARGS_DESCRIPTION)
        # Действия
        parser.add_argument('-a', '--action', choices=['n', 'm', 'u', 'M', 'U'], help=self.lang.ARGS_ACTION)
        # Параметры
        parser.add_argument('-P', '--path', help=self.lang.ARGS_PATH)
        parser.add_argument('-v', '--version', help=self.lang.ARGS_VERSION)
        parser.add_argument('-d', '--descriptionru', help=self.lang.ARGS_DESCRIPTIONRU)
        parser.add_argument('-D', '--descriptionen', help=self.lang.ARGS_DESCRIPTIONEN)
        parser.add_argument('-u', '--user', help=self.lang.ARGS_USER)
        parser.add_argument('-p', '--password', help=self.lang.ARGS_PASSWORD)
        parser.add_argument('-f', '--force', action='store_true', help=self.lang.ARGS_FORCE)
        parser.add_argument('-l', '--log', action='store_true', help=self.lang.ARGS_LOG)
        parser.add_argument('-e', '--email', help=self.lang.ARGS_EMAIL)
        parser.add_argument('-n', '--name', help=self.lang.ARGS_NAME)
        parser.add_argument('-b', '--base', help=self.lang.ARGS_BASE)
        parser.add_argument('-r', '--russian', action='store_true', help=self.lang.ARGS_RUSSIAN)
        # Модуль для обработки
        parser.add_argument('module', help=self.lang.ARGS_MODULE)

        return parser.parse_args()

    # Проверяет название модуля на соответствие маски partner.module
    def checkModuleName(self) -> Match | None:
        return re.match(r'^[a-z]+\.[a-z]+$', self.module)

    # Удаление файлов доступных только для чтения
    def removeReadonly(self, func, path: str, excinfo) -> None:
        os.chmod(path, stat.S_IWRITE)
        func(path)

    # Конвертирование кодировки и копирование файла
    def copyAndConvertFile(self, fromFile: str, toFile: str, fromEncoding: str, toEncoding: str) -> None:
        BLOCKSIZE = 1048576

        # Создание директорий рекурсивно по пути к файлу
        toDir = os.path.dirname(toFile)
        if not os.path.exists(toDir):
            os.makedirs(toDir)

        # Конвертирование
        with codecs.open(fromFile, "r", fromEncoding) as sourceFile:
            with codecs.open(toFile, "w", toEncoding) as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)

    # Обновление файла version.php
    def makeVersionFile(self) -> bool:
        text = '<?php\n$arModuleVersion = [\'VERSION\' => \'' + self.version + '\', \'VERSION_DATE\' => \'' + self.date + '\'];\n\n'
        file = open(os.path.join(self.module, 'install', 'version.php'), 'wb')
        file.write(text.encode(self.encodeBase))
        file.close()

        return True

    # Создание файлов description.ru и description.en
    def makeDescriptionFiles(self) -> bool:
        if not self.descriptionRu or not self.descriptionEn:
            print(self.lang.ERROR % self.lang.UPDATE_ARCHIVE_DESCRIPTION_ERROR)
            return False

        file = codecs.open(os.path.join(self.version, 'description.ru'), "w", self.encode)
        file.write(self.descriptionRu.replace('#', "\n"))
        file.close()

        file = codecs.open(os.path.join(self.version, 'description.en'), "w", self.encode)
        file.write(self.descriptionEn.replace('#', "\n"))
        file.close()

        return True

    # Создаёт в случае необходимости файл updater.php
    def makeUpdater(self, postfixText: str) -> bool:
        updatePath = os.path.join(self.version, self.updaterFile)
        text = ''
        if not os.path.exists(updatePath):
            text = '<?php'

        text = text + '\n\n// Delete file list:\n' + postfixText
        # Дополнить кодом проверки и удаления пустых директорий
        file = open(updatePath, 'a+')
        file.write(text)
        file.close()

        return True

    # Авторизация пользователя через форму на сайте
    def sendForm(self, url: str, check: Dict, formData: List, files: List) -> str:
        self.openSession()
        response = self.session.post(url, data=formData, files=files, headers=self.header)
        self.checkResponse(response, check)
        self.saveCookie()

        return response.text

    # Авторизация пользователя через форму на сайте
    def loginByForm(self, url: str, user: str, password: str, check: Dict) -> str:
        self.openSession()
        response = self.session.get(url, headers=self.header)

        if not self.checkResponse(response, check):
            print(self.lang.AUTH_COOKIE_ERROR)
            formData = {
                'AUTH_FORM': 'Y',
                'TYPE': 'AUTH',
                'USER_LOGIN': user,
                'USER_PASSWORD': password,
                'USER_REMEMBER': 'Y',
                'Login': 'Войти'
            }
            if not user:
                user = input(self.lang.USER)
                formData["USER_LOGIN"] = user
                if not user:
                    return ""

            if not password:
                password = getpass(self.lang.PASSWORD)
                formData["USER_PASSWORD"] = password
                if not password:
                    return ""

            response = self.session.post(url, data=formData, headers=self.header)
            self.checkResponse(response, check)

        self.saveCookie()

        return response.text

    # Открытие сессии
    def openSession(self) -> bool:
        if self.session:
            return True

        self.session = requests.Session()

        try:
            with open(self.cookieFile, 'rb') as f:
                self.session.cookies.update(pickle.load(f))
        except IOError as e:
            # если файл с куками не найдет игнорируем ошибку
            if e.errno == errno.ENOENT:
                pass
            # в другом случае бросаем ошибку
            else:
                raise
        return True

    # Сохранение Cookie
    def saveCookie(self) -> None:
        if not self.session:
            return None

        with open(self.cookieFile, 'wb') as f:
            pickle.dump(self.session.cookies, f)

    # Проверка ответа
    def checkResponse(self, response: requests.Response, check: Dict) -> bool:
        self.resultCode = None
        self.resultValue = None
        self.resultText = None

        for code, valueList in check.items():
            for value, text in valueList.items():
                if value in response.text:
                    self.resultCode = code
                    self.resultValue = value
                    if text:
                        self.resultText = text
                    else:
                        self.resultText = value

                    return self.resultCode == "success"

        return False


if __name__ == '__main__':
    init(autoreset=True)
    module = AutoModule()
    module.doAction()
