from app import bot, dp
from aiogram.types import Message
from config import  admin_id, todo, HELP
import time

command = 0
# 0 - пользователь ничего не выбрал
# 1 - ожидаем дату для добавления задачи
# 2 - ожидаем задачу для добавления в словарь

userDate, userTask = 0,0

async def send_to_admin(dp):
  await bot.send_message(chat_id=admin_id, text="Бот запущен")

  @dp.message_handler(commands = "start")
  async def echo(message:Message):
    await message.answer(text = "Работает")

  @dp.message_handler(commands = "add")
  async def add(message:Message):
    global command
    await message.answer(text = "Введите дату в форме дд.мм.гггг")
    command = 1

  @dp.message_handler(commands = "done")
  async def done(message:Message):
    await message.answer(text = "Работает")

  @dp.message_handler(commands = "help")
  async def help(message:Message):
    await message.answer(text = HELP)

  @dp.message_handler(commands = "show")
  async def show(message:Message):
    await message.answer(text = "Работает")

  @dp.message_handler()
  async def inputtext(message:Message):
    global userDate, userTask, command, todo
    if command == 1:
     #проверка корректноти ввода

     #запрос что нужно сделать 
     userDate = message.text
     await message.answer("Что нужно сделать?")
     command = 2
    elif command == 2:
       userTask = message.text
       if userDate in  todo:
         todo[userDate]=[userTask]
       else:
         todo[userDate]=[userTask]
       await message.answer(f"Добавлена,{userTask}, на {userDate}")
       command = 0       
