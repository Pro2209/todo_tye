##импорт библеотека



TOCEN = ""

HELP = """
help - Вывод списка команд
add - добавление задачи
show - показать все задачи
done - задача выполнена
"""
todo = {}

print("Привет! Введите команду help для вывода списка команд")

while True:
  userAnswer = input("Введите команду:\n")
if userAnswer == "add" :
  userDate = input("Введите дату:\n")
  userTask = input("Что нужно сделать?")

  todo[ userDate ] = userTask
  print(f" На{userDate} число добавлена задача '{userTask}'")
  print("Работает")
elif userAnswer == "help" :
  print(HELP)
elif userAnswer == "show" :
 for date in todo.keys():
   print( f"[ {date} - {todo[date]} ]")
elif userAnswer == "done" :
  print("Работает") 
elif userAnswer == "exit" :
  print("Работает")   
else:
    print("Error,Нет такой команды")
    print("Введите help для вывода списка команд")