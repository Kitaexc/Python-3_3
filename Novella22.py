import time
import json
import csv
import os
import pygame
from colorama import Fore, init

init(autoreset=True)

pygame.init()
audio_file_path = "C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\00218.mp3" #В папке есть файл со звуком, вставьте путь к файлу в данную строку, затем сохранить и наслождайтесь.
pygame.mixer.music.load(audio_file_path)

def clear_json_save(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('{}')  # Записываем пустой JSON объект
            print("Содержимое файла сохранения успешно очищено.")
    except Exception as e:
        print(f"Произошла ошибка при очистке файла: {e}")


user_data = {
    "username": "",
    "progress": 0,
    "choices": [],
    "volues" : "",
    "colors" : []
}

username = input("Введите свое имя: ")
user_data["username"] = username

громкости = { #Множество есть 
    "Тихо": 0.1,
    "Средне": 0.5,
    "Громко": 1.0
}

print("Выберите уровень громкости:")
for key, value in громкости.items():
    print(f"{key}. Громкость {value * 100}%")


выбор = input("Введите номер уровня громкости: ")

if выбор in громкости:
    уровень_громкости = громкости[выбор]
    pygame.mixer.music.set_volume(уровень_громкости)
    user_data["volues"] = уровень_громкости
else:
    print("Недопустимый выбор уровня громкости.")
    


def animate_text(text, speed = 0.000000005): #Функция со строками есть
    for char in text:
        print(Fore.WHITE + char, end='', flush=True)
        time.sleep(speed)
    print()

colors = [Fore.RED, Fore.MAGENTA, Fore.YELLOW] #Список есть

color_names = {  #Словарь есть
    1: "Красный",
    2: "Пурпурный",
    3: "Жёлтый"
}

print("Выберите цвет текста:")
for key, color in enumerate(colors, start=1):
    print(f"{key}. {color_names[key]}") #f-строка есть

col = input("Введите номер цвета: ")

user_data["colors"] = col

try:
    choice = int(col)
    text_color = colors[choice - 1] 
except (ValueError, IndexError):
    text_color = Fore.WHITE

a = 0

while a < 40:
    a += 1
    print ( )
    
pygame.mixer.music.play(-1)


print("1. Начать игру")
print("2. Очистить предыдущие сохранения")
choice = input("Выберите опцию: ")
if choice == "2":
    clear_json_save("C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\user_data.json")


print(text_color + "Добро пожаловать в Туман...")
print(text_color + "Чтобы начать играть, нажмите Enter")
input()
    
b = 0

while b < 40:
    b += 1
    print ( )    
pygame.mixer.music.play(-1)
print (text_color + "..........ГЛАВА №1..........")
print (text_color + "☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠")
print (text_color + "..........ВВЕДЕНИЕ..........")
print()
time.sleep(1)

text = "Снег жалобно скрипит под подошвами сапог, поблескивает изумрудным крошевом. Небо приобрело мертвенно-синюшный цвет."
animate_text(text)
print (text_color + "....................................................")
text = "Воздух звенит от мороза."
animate_text(text)
print (text_color + "....................................................")
text = "Вокруг, куда ни посмотри, простирается безжизненая белая пустыня, лишь вдали она бугрится холмами.\nНа их склонах искорёженные стволы мёртвых деревьев, чьи ветви похожи на руки мучеников."
animate_text(text)
print (text_color + "....................................................")

while True:
    print(text_color + "1. ⧼Поежиться⧽")
    print(text_color + "2. ⧼Оглядеться⧽")
    print(text_color + "3. ⧼Дыханием отогреть руки⧽")

    print(text_color + "...")
    answer = input()
    print()

    if answer not in ["1", "2", "3"]:
        print ("Вы не сделали выбор!")
    else:
        user_data["progress"] += 1
        user_data["choices"].append(answer)
        break

def answ_1():
    print (text_color + "....................................................")
    text = "Поежившись я иду по протоптанной \nдороге."
    animate_text(text)
    print (text_color + "....................................................")
def answ_2():
    print (text_color + "....................................................")
    text = "Оглядываясь по сторонам, я иду по протоптанной дороге."
    animate_text(text)
    print (text_color + "....................................................")
def answ_3():
    print (text_color + "....................................................")
    text = "Я снимаю перчатки, дышу на закоченевшие пальцы, чтобы их согреть. Помагает слабо."
    text += "Затем надеваю перчатки обратно и иду по протоптанной дороге."
    animate_text(text)
    print (text_color + "....................................................")

if answer == "1": 
    answ_1()
elif answer == "2":
    answ_2()
elif answer == "3":
    answ_3()
    

text = "На моем пути ни разу никто еще не \nпопался и иногда кажется, будто больше и \nнет никого на свете."
animate_text(text)
print (text_color + "....................................................")
text = "Лишь белая пустыня, черное небо и я."
animate_text(text)
print (text_color + "....................................................")
text = "Рано или поздно без воды и еды мои силы \nиссякнут, и явится смерть."
animate_text(text)
print (text_color + "....................................................")
text = "К тому же всё чаще налетает ледяной \nветер, от которого едва защищают плащ, \nнесколько свитеров и плотные штаны."
animate_text(text)
print (text_color + "....................................................")
text = "Холод медленно подбирается ко мне, \nпокусывает пальцы на ногах и руках…"
animate_text(text)
print (text_color + "....................................................")
text = "Я - мертвец."
animate_text(text)
print (text_color + "....................................................")
text = "Смутное чувство беспокойства преследует \nменя, не дает расслабиться ни на \nмгновение."
animate_text(text)
print (text_color + "....................................................")
text = "А иногда паника накатывает с такой \nсилой, что легкие обжигает огнем, а горло \nсдавливает."
animate_text(text)
print (text_color + "....................................................")
text = "Сердце начинает бешено колотиться, \nотдаваясь ударами в висках и в кончиках \nпальцев."
animate_text(text)
print (text_color + "....................................................")
text = "Я бегу на негнущихся от страха \nдеревянных ногах в надежде скрыться от \nсамого себя. Но уменя не выходит."
animate_text(text)
print (text_color + "....................................................")
text = "Конечно же, потом паника постепенно \nзатихает, а вот беспокойство - нет."
animate_text(text)
print (text_color + "....................................................")
text = "Когда вдали в ночной темноте \nугадываются очертания города, я \nвскрикиваю от радости."
animate_text(text)
print (text_color + "....................................................")
text = "Заставляю себя ускорить шаг."
animate_text(text)
print (text_color + "....................................................")
text = "Где-то глубоко внутри меня подленький \nголосок начинает шептать, что на самом \nделе впереди ничего нет, что это морок, \nиллюзия, что от холода брежу."
animate_text(text)
print (text_color + "....................................................")
text = "Но чем я ближе, тем отчетливее \nпроступают сторожевые башни, высокая \nстена, а за ними - силуэты домов."
animate_text(text)
print (text_color + "....................................................")
print()

while True:
    print(text_color + "1. ⧼Вспомнить, были ли здесь раньше⧽")
    print(text_color + "2. ⧼Спросить себя, кто вы⧽")
    print(text_color + "3. ⧼Задуматься, откуда вы пришли⧽")

    print(text_color + "...")
    answer = input()
    print()

    if answer not in ["1","2","3"]:
        print ("Вы не сделали выбор!")
    else:
        user_data["progress"] += 1
        user_data["choices"].append(answer)
        break
    
def answ_1():
    print (text_color + "....................................................")
    text = "Пытаюсь вспомнить, был ли здесь раньше."
    animate_text(text)
    print (text_color + "....................................................")    
    text = "Но моя память точно решето — ничего не \nвыцепить дельного."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Осколки прошлого воедино не собрать — \nтак, не значащие фрагменты."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Кто я?"
    animate_text(text)
    print (text_color + "....................................................")
    text = "Откуда я иду и куда?"
    animate_text(text)
    print (text_color + "....................................................")
def answ_2():
    print (text_color + "....................................................")
    text = "Моя память точно решето — ничего не \nвыцепить дельного."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Осколки прошлого воедино не собрать — \nтак, не значащие фрагменты."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Кто я?"
    animate_text(text)
    print (text_color + "....................................................")
    text = "Откуда я иду и куда?"
    animate_text(text)
    print (text_color + "....................................................")
def answ_3():
    print (text_color + "....................................................")
    text = "Моя память точно решето — ничего не \nвыцепить дельного."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Осколки прошлого воедино не собрать — \nтак, не значащие фрагменты."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Откуда я иду и куда?"
    animate_text(text)
    print (text_color + "....................................................")
    text = "Кто я?"
    animate_text(text)
    print (text_color + "....................................................")

if answer == "1": 
    answ_1()
elif answer == "2":
    answ_2()
elif answer == "3":
    answ_3()
    
text = "Как долго я вообще уже в пути?"
animate_text(text)
print (text_color + "....................................................")
text = "У меня нет сумки, нет запасов еды и воды. \nДа и одежда не для здешних холодов."
animate_text(text)
print (text_color + "....................................................")
text = "Что-то произошло? Напали бандиты?"
animate_text(text)
print (text_color + "....................................................")
text = "От бесчисленных вопросов сверлит в висках."
animate_text(text)
print (text_color + "....................................................")
print()

while True:
    print(text_color + "1. ⧼Понять все сейчас⧽")
    print(text_color + "2. ⧼Разобраться позже⧽")

    print(text_color + "...")
    answer = input()
    print()

    if answer not in ["1","2"]:
        print ("Вы не сделали выбор!")
    else:
        user_data["progress"] += 1
        user_data["choices"].append(answer)
        break

def answ_1():
    print (text_color + "....................................................")
    text = "Я. Должен. Понять. Всё. Сейчас."
    animate_text(text)
    print (text_color + "....................................................")
    text = "От этой неопределенности кружится \nголова, реальность кажется ненастоящей, \nвыдуманной."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Но чем сильнее я сосредотачиваюсь на \nпростых, казалось бы, вещах - есть ли у \nменя детство? как выглядели мои \nродители? где рос? - тем сильнее боль."
    animate_text(text)
    print (text_color + "....................................................")
    text = "К горлу подступает горький ком, мне \nприходится сосредоточиться на том, где \nнахожусь."
    animate_text(text)
    print (text_color + "....................................................")
def answ_2():
    print (text_color + "....................................................")
    text = "Раберусь позже."
    animate_text(text)
    print (text_color + "....................................................")
    
if answer == "1": 
    answ_1()
elif answer == "2":
    answ_2()

text = "Боковым зрением замечаю темный силуэт \nна поле по левую сторону от меня. \nПриглядевшись, вижу доходягу со \nспутанной бородой."
animate_text(text)
print (text_color + "....................................................")
text = "По колено утопая в снегу, он быстро \nудаляется от стены города, стонет, петляет \nзигзагами, но не выходит на широкую \nпротоптанную дорогу, по которой иду я."
animate_text(text)
print (text_color + "....................................................")
text = "Я хотел было поднять руку и \nпоприветствовать его, когда понимаю - \nчто-то здесь не так."
animate_text(text)
print (text_color + "....................................................")
text = "Доходяга полуголый!"
animate_text(text)
print (text_color + "....................................................")
text = "Из одежды на нем только порванные в \nлохмотья штаны!"
animate_text(text)
print (text_color + "....................................................")
text = "Посиневший от холода, грязный он то \nтеряет равновесие и падает в сугробы, то, \nпошатываясь и озираясь назад, \nподнимается, движется вперед."
animate_text(text)
print (text_color + "....................................................")
text = "Из тени стены возникает широкоплечий \nнезнакомец."
animate_text(text)
print (text_color + "....................................................")
print()

while True:
    print(text_color + "1. — Суровый мужик.")
    print(text_color + "2. — Надеюсь, меня не покалечит...")
    print(text_color + "3. — Надо скорее уходить.")

    print(text_color + "...")
    answer1 = input()
    print()

    if answer1 not in ["1","2","3"]:
        print ("Вы не сделали выбор!")
    else:
        user_data["progress"] += 1
        user_data["choices"].append(answer)
        break

def answ_11():
    print (text_color + "....................................................")
    text = "Его необычно длинный плащь, подбитый \nмехом, стелется за ним."
    animate_text(text)
    print (text_color + "....................................................")    
    text = "Накинутый на голову широкий капюшон \nскрывает лицо в чернильном мраке."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Незнакомец, не торопясь, \nостанавливается, неспешно отцепляет c \nпояса миниатюрный самострел."
    animate_text(text)
    print (text_color + "....................................................")
    text = "В ночи блестит острие взведенного \nарбалетного болта."
    animate_text(text)
    print (text_color + "....................................................")
    text = "До ушей доносится резкий свист."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Доходяга вздрагивает и валится в сугроб, \nточно подкошенный."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Страшный крик проносится по ледяной \nпустыне, эхом удаляясь к холмам и \nмертвомулесу."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Нервно сглатываю."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Между тем, незнакомец в плаще подходит \nк своей жертве и наблюдает за её \nстраданиями."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Мое сердце успевает ударить не меньше \nдвадцати раз прежде, чем он хватается за \nторчащий из-за спины костяной эфес меча \nи вынимает его."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Снег вокруг доходяги окрашивается в \nтемно-алый."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Содрогнувшись от отвращения, я ускоряю \nшаг и направляюсь к воротам города."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Стальные стены нависают надо мной, \nподавляют своими размерами."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Теперь отчетливо видно - они не \nиллюзорные, тут и там чернеют ржавые \nподтеки, на обшитых листах вмятины, \nточно от ударов молотом."
    animate_text(text)
    print (text_color + "....................................................")
    text = "По обе стороны от ворот торчат две \nмассивные сторожевые башни. В их окнах \nгорит, подрагивая, грязно-желтый свет."
    animate_text(text)
    print (text_color + "....................................................")
    text = "Интересно, меня истыкают стрелами, \nарбалетными болтами или просто \nзакидают камнями?"
    animate_text(text)
    print (text_color + "....................................................")
    print()
    
if answer1 == "1": 
    answ_11()
elif answer1 == "2":
    answ_11()
elif answer1 == "3":
    answ_11()

while True:
    print(text_color + "1. ⧼Позволить страху взять верх⧽")
    print(text_color + "2. ⧼Успокоиться⧽")


    print(text_color + "...")
    answer = input()
    print()

    if answer not in ["1","2"]:
        print ("Вы не сделали выбор!")
    else:
        user_data["progress"] += 1
        user_data["choices"].append(answer)
        break
    
def answ_1():
    print (text_color + "....................................................")
    text = "Ледяной страх разливается между лопаток, проникает по внутренности."
    animate_text(text)
    print (text_color + "....................................................")
def answ_2():
    print (text_color + "....................................................")
    text = "Так, надо дышать глубоко — вдох, выдох, вдох..."
    animate_text(text)
    print (text_color + "....................................................")
    
if answer == "1": 
    answ_1()
elif answer == "2":
    answ_2()
    
text = "Я всё время оглядываюсь, но не из-за незнакомца в плаще."
animate_text(text)
print (text_color + "....................................................")
text = "Не могу отделаться от ощущения, что за мной кто-то следит."
animate_text(text)
print (text_color + "....................................................")
text = "Кто-то там вдали за холмами - огромный, бесформенный, чужой."
animate_text(text)
print (text_color + "....................................................")
text = "Ждет, пока я сделаю первый шаг..."
animate_text(text)
print (text_color + "....................................................")
text = "Ладно, прочь дурные мысли."
animate_text(text)
print (text_color + "....................................................")
text = "Мне нужно войти в город!"
animate_text(text)
print (text_color + "....................................................")
print()
print (text_color + "☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠")
print (text_color + "......ВЫ УСПЕШНО ПРОШЛИ ВВЕДЕНИЕ......")

with open("C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\user_data.json", "a") as json_file:
    json.dump(user_data, json_file)

file_exists = os.path.isfile('C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\user_data.csv') and os.path.getsize('C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\user_data.csv') > 0

with open('C:\\Users\\ULNV_Developer\\Desktop\\Тех\\Python\\Novella\\user_data.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if not file_exists:
        headers = ['username', 'progress', 'choices', 'volues', 'colors']
        writer.writerow(headers)
    writer.writerow([user_data['username'], user_data['progress'], user_data['choices'], user_data['volues'], user_data['colors']])