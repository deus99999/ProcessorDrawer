# 🖼️ ProcessorDrawer Bot

Telegram-бот, который принимает изображение процессора и добавляет текст содержащий модель и название процессора для ноутбука. Идеально подходит для автоматической генерации подписей к изображениям процессоров

## 🚀 Возможности

- Принимает фото от пользователя через Telegram
- Автоматически обрезает изображение до квадратной формы
- Накладывает текст сверху и снизу изображения
- Возвращает обработанное изображение пользователю в чат

## 🧠 Используемые технологии

- Python 3
- [Pillow (PIL)](https://python-pillow.org/) — для обработки изображений
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) — для взаимодействия с Telegram API

## 📸 Пример использования

1. Отправьте фото процессора в боту
2. Добавьте подпись к изображению, например:  
   `Intel Pentium B960, SR07V`
3. Бот автоматически добавит надпись и вернёт обработанное изображение:

![image](https://github.com/user-attachments/assets/bff203e1-d9a5-4720-8d82-4f3057ae57b0)


## ⚙️ Установка и запуск

```bash
git clone https://github.com/deus99999/ProcessorDrawer.git
cd ProcessorDrawer
pip install -r requirements.txt
```

Создайте файл `config.py` и добавьте ваш Telegram Bot Token:

```python
TOKEN = "ваш_токен_бота"
```

Запустите:

```bash
python main.py
```

## 📁 Структура проекта

```
ProcessorDrawer/
├── config.py         # токен Telegram-бота
├── main.py           # основной код Telegram-бота
├── output.jpg        # обработанное изображение (пример)
├── requirements.txt  # зависимости
```

## 📝 Автор

- [@deus99999](https://github.com/deus99999)
