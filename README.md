cd ~
# Создаем виртуальное окружение
virtualenv venv
# Активируем виртуальное окружение
source venv/scripts/activate
# Клонируем проект
git clone https://github.com/AlexanderVorobei/pyMessenger.git
# Ставим необходимые модули
pip install -r requirements.txt
# Запускаем сервер
python server.py
# Запускаем клиент
python messenger.py