import io

from PIL import Image, ImageDraw, ImageFont
from config import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def add_text_to_image(file_path, text: str, output_path):
    """ Get image as a bytes array and returns image with text """

    # Открыть изображение
    image = Image.open(io.BytesIO(file_path))

    # Настройка шрифта
    try:
        font_size = max(50, image.size[0] // 8)
        font = ImageFont.truetype("arial.ttf", size=font_size)  # Использование шрифта Arial
    except IOError as e:
        print(e)
        font = ImageFont.load_default()

    # Размер изображения
    width, height = image.size

    # Вычисляем отступы сверху и снизу, чтобы обрезать по центру
    top = (height - width) // 2
    bottom = (height + width) // 2

    img = image.crop((0, top, width, bottom))

    draw = ImageDraw.Draw(img)

    # Обновляем высоту после обрезки
    new_height = img.size[1]   # height

    # Добавление текста на изображение
    text = text.replace(',', '').split()
    #
    # for letter in text:
    #     if letter == ',':
    #         text.replace(',', '')
    print("text: ", text)

    top_text, bottom_text = text[-1], text[:3]

    print(top_text, bottom_text)
    draw.text((width / 2, new_height / 6), top_text, anchor="ms", font=font, fill="Black")

    bottom_text = [word for word in bottom_text]

    draw.text((width / 2, new_height / 1.25), bottom_text[0] + " " + bottom_text[1], anchor="ms", font=font,
              fill="Black")
    draw.text((width / 2, new_height / 1.05), bottom_text[2], anchor="ms", font=font, fill="Black")

    # Сохранение результата
    img.save(output_path)

    return img


def start(update):
    update.message.reply_text('Привет! Отправь мне фото процессора, и я добавлю на него текст.')


# # Функция для обработки изображений
def handle_image(update, context):
    photo_file = update.message.photo[-1].get_file()  # Получаем изображение
    file_path = photo_file.download_as_bytearray()

    # Добавляем текст к изображению

    text_from_user = update.message.caption  # Получаем подпись к фото, если она есть

    if text_from_user is None:
        update.message.reply_text('no processor info')

    image = add_text_to_image(file_path, text_from_user, "output.jpg")

    # Открытие изображения через буфер памяти (io.BytesIO)
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    image_buffer.seek(0)  # Сброс указателя в начало файла

    # Отправляем обратно изображение с текстом
    context.bot.send_photo(chat_id=update.message.chat_id, photo=image_buffer)


# Основная функция для запуска бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_image))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
