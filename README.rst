MyBot
=====

Это тестовый бот на котором я обкатываю разработку простых телеграм-ботов

Установка
---------
Создайте виртуальное окружение и активируйте его. 
Затем в виртуальном окружении выполните:
.. code-block:: text
    pip install -r requirements.txt

Положите картинки с котиками в папку images. Название файлов произвольное, формат любой

Настройка
---------

Создайте файл settings.py и укажите в нем следующие настройки
.. code-block:: python
    TOKEN = 'токен телеграм бота от BotFather'
    proxy_url = 'url прокси'
    username = 'логин для прокси'
    password = 'пароль для прокси'
    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']  #список emoji которые будут использоваться

Запуск
------
В активированном вирутальном окружении выполните команду 
.. code-block:: text
    python3 bot.py