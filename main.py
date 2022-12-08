import playsound
import random
import time
import speech_recognition as sr

hello = ["привет", "здравствуйте", "здравия желаю", "приветствую", "доброго времни суток", "добрый день"]
bye = ["пока", "до свидания", "всего доброго", "пошёл нахуй", "прощай"]
how = ["как ваши дела", "как у вас дела", "как сам", "как дела", "что нового", "как жизнь"]
who = ["кто ваш любимый студент", "кто лучший", "кто"]
node = ["напугали", "напугали", "поставили два", "поставили три", "зачем", "почему"]
youare = ["вы тупой", "ты тупой", "тупой"]
no = ["нет", "никак нет", "не буду", "никогда"]
history = ["история", "историю", "расскажите историю", "расскажи историю", "смысл жизни", "как правильно жить", "правильно жить"]
bred = ["ссс", "ррр"]
ptr = 0

print('\n')
print("Привет, друг!")
print('\n')
time.sleep(3)
print("Ты запустил голосвого ассистента Артемьева. К сожалению, он немного тупой \n(не потому, что его делал рукожопый программист с третьего курса) \nпоэтому вот список вопросов, на которые он может ответить:")
time.sleep(10)
print("-В чём смысл жизни?")
time.sleep(2)
print("-Зачем он ставит нам двойки?")
time.sleep(2)
print("-Кто его любимый студент? (Это очень хороший вопрос)")
time.sleep(3)
print("-Также он может отреагировать, если назвать его тупым")
time.sleep(3)
print("\nНачинаем!")
time.sleep(1)
time.sleep(1)

def play1():
    playsound.playsound('1.mp3')

def play2():
    playsound.playsound('2.mp3')

def play3():
    playsound.playsound('3.mp3')

def play5():
    playsound.playsound('5.mp3')

def play6():
    playsound.playsound('6.mp3')

def play7():
    playsound.playsound('7.mp3')

def play8():
    playsound.playsound('8.mp3')

def play9():
    playsound.playsound('9.mp3')

def play10():
    playsound.playsound('10.mp3')

def play11():
    playsound.playsound('11.mp3')

def play12():
    playsound.playsound('12.mp3')

def play13():
    playsound.playsound('13.mp3')


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n')
        print("Скажите команду: ")
        audio = r.listen(source)
    try:
        print("Вы сказали: ", r.recognize_google(audio, language="ru"))
        return r.recognize_google(audio, language="ru")
    except sr.UnknownValueError:
        return "Error"
    except sr.RequestError:
        return "Error"


def say(text):
    if text == "Hello":
        play2()
    elif text == "Bye":
        a = random.randint(1, 3)
        if a == 1:
            play9()
            finish()
        else:
            play10()
            finish()
    elif text == "How":
        play3()
    elif text == "Volk":
        play5()
    elif text == "Node":
        play11()
    elif text == "You":
        play7()
    elif text == "History":
        play12()
    elif text == "No":
        play6()
    elif text == "I don't understand":
        print("Артемьев вас не понял. Сейчас будет сказана стандартная фраза.")
        ptr = 0
        b = random.randint(0, 4)
        if b < 2:
            play1()
        elif b == 2:
            play8()
        else:
            play13()


def handle_message(message):
    global ptr
    message = message.lower()
    for i in range(0, len(hello)):
        if hello[i] in message:
            ptr = 0
            say("Hello")
            return
        else:
            ptr = 1
    for i in range(0, len(bye)):
        if bye[i] in message:
            ptr = 0
            say("Bye")
            return
        else:
            ptr = 2
    for i in range(0, len(how)):
        if how[i] in message:
            ptr = 0
            say("How")
            return
        else:
            ptr = 3
    for i in range(0, len(who)):
        if who[i] in message:
            ptr = 0
            say("Volk")
            return
        else:
            ptr = 4
    for i in range(0, len(node)):
        if node[i] in message:
            ptr = 0
            say("Node")
            return
        else:
            ptr = 5
    for i in range(0, len(youare)):
        if youare[i] in message:
            ptr = 0
            say("You")
            return
        else:
            ptr = 6
    for i in range(0, len(history)):
        if history[i] in message:
            ptr = 0
            say("History")
            return
        else:
            ptr = 7
    for i in range(0, len(no)):
        if no[i] in message:
            ptr = 0
            say("No")
            return
        else:
            ptr = 8
    if ptr != 0:
        say("I don't understand")


def finish():
    print('\n')
    print("____________*_____*\n"
          "___________*_*****_*\n"
          "__________*_(O)_(O)_*\n"
          "_________**____V____**\n"
          "_________**_________**\n"
          "_________**_________**\n"
          "__________*_________*\n"
          "___________***___***\n")
    time.sleep(2)
    exit()

if __name__ == '__main__':
    while True:
        time.sleep(1)
        command = listen()
        handle_message(command)