# -*- coding: utf-8 -*-
import numpy
import telebot
import datetime
import time
import threading
import json
import os

chatid = 0
bot = telebot.TeleBot('988714903:AAFU2FccliDpkE5_6anNWiDMr8WZkhqpNpY')

dir_videos = os.listdir("video/hb")
dir_videos.sort()
videousDictionary = {}

print(str(dir_videos))

#время начала тайм-чека бота
#нужный час - 3
t = (2020, 5, 28, 7, 40, 0, 0, 0, 0)
init_time = int(time.mktime(t))

lessons_times = [(2020, 5, 28, 9, 43, 0, 0, 0, 0), (2020, 5, 28, 10, 43, 0, 0, 0, 0), (2020, 5, 28, 11, 43, 0, 0, 0, 0), (2020, 5, 28, 12, 43, 0, 0, 0, 0), (2020, 5, 28, 13, 43, 0, 0, 0, 0), (2020, 5, 28, 14, 43, 0, 0, 0, 0)]

print('init_time = '+str(init_time))
print('time.time = '+str(int(time.time())))
session_length_time = 10*60*60
video_hb_timeout = int(session_length_time/len(dir_videos))
video_messages = ['Приём-приём', 'Есть к тебе пара слов...', 'Хочется сказать', 'Итак, время поздравлений!', 'Вот, смотри, что нашёл', 'Кажется, это тебе?', 'Так-так-тааак, у кого у нас сегодня день рождения?']

print('video_hb_timeout ===> ')
print(video_hb_timeout/60)


noise_message = ['*Пшш-ш-ш*','*Пииип*','*...Пкшс*','*пк*','*пиии-и-ик*','*Пшш--Пшшшшшш*','*ПЩК*','*дзынь*','*пииип*','*...ик*']
drunk_message = ['Ну, выпьем?','Будем!','Ну, за любовь!','За ПЗД!','Чин-чин','Поехали','Na zdorovie!','Надо бы выпить...']


i=0
while i<len(dir_videos):
    videoTimestamp = init_time+video_hb_timeout*i+10
    print('videoTimestamp ==== '+dir_videos[i])
    print(time.ctime(videoTimestamp+60*60*3))
    videousDictionary[str(videoTimestamp)] = dir_videos[i]
    i+=1
    
#print('videousDictionary =======> ')
#print(str(videousDictionary))

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '21285':
        sendMessageToAll('И это правильный ответ!')
        sendMessageToAll('Что, сам решил? Ещё и в уме небось?')
        showPic('pics/respect.jpg')
        sendMessageToAll('Ну, за это надо выпить')
        
        showDrink()

    elif message.text == '20045':
        sendMessageToAll('Не то! Придётся выпить!\nЗа связь без бpака!\n псс - ну, ты понял, я же робот ;)')
        showDrink()
    elif message.text == '35924':
        sendMessageToAll('Неа... Опять пить?\nСамый короткий тост: Enter!!!')
        showDrink()
    elif message.text == '48762':
        sendMessageToAll('И это... не правильный ответ!\nРаньше человек 10 должны были работать неделю, чтобы сделать столько же ошибок, сколько делает компьютер секунд за 10. Так выпьем же за постоянное увеличение скорости компьютеров!')
        showDrink()
    elif message.text == '12345':
        sendMessageToAll('Не повезло! Зато нет повода не выпить!\nПьянству бой!\nТак выпьем же, друзья перед боем!')
        showDrink()
    elif message.text == '11111':
        sendMessageToAll('Не правильно! Теперь надо выпить на удачу!\nНе пьянки ради - здоровья для!')
        showDrink()
    elif message.text == '00000':
        bot.send_message(message.chat.id, '*Пириветик!')

@bot.message_handler(commands=['start'])
def start_message(message):
    f = open('chatid.txt', 'r')

    chatsStr = f.read()
    print('--------->>>>  chatsStr = '+chatsStr)
    chats = chatsStr.split(",")
    print('--------->>>>  chats = '+str(chats))
    hasId = 0
    
    if chats[0] == '':
        chats = []
    
    i = 0
    while i<len(chats):
        if int(chats[i]) == message.chat.id:
            hasId = 1
        i+=1
            
    if hasId == 0:
        chats.append(message.chat.id)
        print('--------->>>>  chats 2 = '+str(chats))
        
    f = open('chatid.txt', 'w')

    i=0;
    while i<len(chats):
        a = str(chats[i])
        chats[i] = a
        i+=1

    f.write(','.join(chats))
    
    bot.send_message(message.chat.id, '*Пии-и-и-ип* День Рожденческий робот помощник приветсвует тебя!')
    bot.send_message(message.chat.id, '*Пшк* Следи за этим чатом. Следуй моим указаниям и я приведу тебя заветной цели, которую эти кожаные мешки хорошенько запрятали!')
    bot.send_message(message.chat.id, '*ик* Удачи!')

def ShowVideoToAll(videoPath):
    f = open('chatid.txt', 'r')
    chats = f.read().split(',')
    for id in chats:
        print('seding videoto '+str(id))
        bot.send_message(id, numpy.random.choice(noise_message, len(noise_message)))
        bot.send_message(id, numpy.random.choice(video_messages, len(video_messages)))
        video = open(videoPath, 'rb')
        bot.send_video(id, video)
            
    showDrink()

def checkVideoHb():
    now = int(time.time())
    now_video = videousDictionary.get(str(now))
    if now_video:
        videoPath = 'video/hb/'+now_video
        print('send video '+videoPath)
        
        ShowVideoToAll(videoPath)
        
def checkVideoAddition(now, showTime, vName):
    if now != showTime:
        return
    
    videoPath = 'video/'+vName
    print('send video '+videoPath)
    
    ShowVideoToAll(videoPath)

            
def checkQustion1(now, lessTime):
    if (now == lessTime):
        showLessPic(1)
        sendMessageToAll('Поздравляем! Ты родился!\nДавай проверим, как ты сохранился ;)\nЯ буду присылать тебе простейшие задачки про МОДУЛИ.\nда-да! Именно модули! А ты будешь присылать ответ. Время для ответа - 10 секунд. Проверь себя?')
        showPic('pics/supermozg.jpg')
        
    if(now == lessTime+1):
        sendMessageToAll('Ты готов?')
    if(now == lessTime+2):
        sendMessageToAll('3...')
    if(now == lessTime+3):
        sendMessageToAll('2...')
    if(now == lessTime+4):
        sendMessageToAll('1...')
    if(now == lessTime+5):
        sendMessageToAll('Поехали!')
        
    if(now == lessTime+5):
        showPic('less/less1/1q.png')
        
    if(now == lessTime+6):
        showPic('less/less1/1.png')
    if(now == lessTime+16):
        showPic('less/less1/1a.png')
        showPic('less/less1/2.png')
    if(now == lessTime+26):
        showPic('less/less1/2a.png')
        showPic('less/less1/3.png')
    if(now == lessTime+36):
        showPic('less/less1/3a.png')
        showPic('less/less1/4.png')
    if(now == lessTime+46):
        showPic('less/less1/4a.png')
        
    if(now == lessTime+47):    
        showPic('less/less1/2q.png')
    if(now == lessTime+48):    
        showPic('less/less1/5.png')
    if(now == lessTime+58):   
        showPic('less/less1/5a.png')
        showPic('less/less1/6.png')
    if(now == lessTime+68):   
        showPic('less/less1/6a.png')
        showPic('less/less1/7.png')
    if(now == lessTime+78):   
        showPic('less/less1/7a.png')
        showPic('less/less1/8.png')
    if(now == lessTime+88):   
        showPic('less/less1/8a.png')

    if(now == lessTime+89):   
        showPic('less/less1/2q.png')
    if(now == lessTime+100):   
        showPic('less/less1/9.png')
    if(now == lessTime+110):    
        showPic('less/less1/9a.png')
        showPic('less/less1/10.png')
    if(now == lessTime+120):   
        showPic('less/less1/10a.png')
        showPic('less/less1/11.png')
    if(now == lessTime+130):   
        showPic('less/less1/11a.png')
        showPic('less/less1/12.png')
    if(now == lessTime+140):   
        showPic('less/less1/12a.png')
        
    if(now == lessTime+141):
        sendMessageToAll('Ну что, размялся мозжечок? Заработал процессор?')
        sendMessageToAll('Так выпьем же за это!')
        showDrink()
        
def CheckQuestion2(now, lessTime):
    if now != lessTime:
        return
        
    showLessPic(2)
    showPic('pics/geo.jpg')
    sendMessageToAll('Натренировался ты, дружок!\nПопробуй ка ещё разок:\nНачерталку вспоминай\nИ загадку разгадай!')
    sendMessageToAll('Подойди к Ване, чтобы получить Путевой лист')
    showDrink()

def CheckQuest3(now, lessTime):
    if now != lessTime:
        return
        
    showLessPic(3)
    showPic('pics/wife.jpg')
    sendMessageToAll('Дальше двигайся теперь\nОткрывай скорее дверь\nЧто же делать, угадай?\nУ жены своей узнай!')
    showDrink()

def CheckQuest4(now, lessTime):
    if now != lessTime:
        return
        
    showLessPic(4)
    showPic('pics/sniper.jpg')
    sendMessageToAll('Чтобы разгадать зашифрованный пятизначный код - тебе понадобится оружие!')
    sendMessageToAll('Спроси-ка на всякий случай у Виктора - он сумеет тебе помочь!')
    showDrink()
    
def CheckQuest5(now, lessTime):
    if now != lessTime:
        return
        
    showLessPic(5)
    showPic('pics/maxresdefault.jpg')
    sendMessageToAll('Пора бы уже сдать на права! Причём - на двухколёсном транспорте!')
    sendMessageToAll('Найди себе мотоинструктора, одежду и мотоцикл')   
    showDrink()
    
def CheckQuest6(now, lessTime):
    if now != lessTime:
        return

    showLessPic(6)
    sendMessageToAll('Найди тайное послание.\nТолько для тебя...\nИщи в морских просторах.\nНаградой тебе станут - настоящие сокровища!')
    showPic('pics/map.jpg')
    showDrink()


def showDrink():
    showPic('pics/drink4.jpg')
    sendMessageToAll(numpy.random.choice(drunk_message, len(drunk_message)))
    
def sendMessageToAll(message):
    f = open('chatid.txt', 'r')
    chats = f.read().split(',')
    for id in chats:
        bot.send_message(id, numpy.random.choice(noise_message, len(noise_message)))
        bot.send_message(id, message)

def showPic(path):
    f = open('chatid.txt', 'r')
    chats = f.read().split(',')
    for id in chats:
        photo = open(path, 'rb')
        bot.send_photo(id, photo)

def showLessPic(num):
    f = open('chatid.txt', 'r')
    chats = f.read().split(',')
    for id in chats:
        photo = open('less/pics/'+str(num)+'.png', 'rb')
        bot.send_photo(id, photo)
    
def checkEnd(now, lessTime):
    if now != lessTime:
        return
        
    print('checkEnd');

    showPic('pics/ava.jpg')
    sendMessageToAll('Всем спасибо за внимание! Пора отключаться... ')
    sendMessageToAll('Мой код здесь:\n https://github.com/ZergMaster/pyHappyMarvin.git')
    sendMessageToAll('Да, я знаю, что он ужасен и написан на коленке за 12 часов, но несмотря на это - он позволил мне Жить!\nИ вместе с этим - поздравить тебя, Витя, с Днём Рождения!\nЯ очень рад возможности пусть и не долго, но Существовать, чтобы поздравить тебя. Желаю, чтобы твой кожаный мешок был крепок, как мой стальной корпус и не поддавался ржавчине. Чтобы твой процессор всегда работал на полную мощь, а стремление получать новый удивительный опыт никогда не иссякало.\nОтсутсвия багов тебе и своевременных апдейтов!\nНу всё.. я на покой.')
    showDrink()

def checkTime():
    threading.Timer(1.0, checkTime).start()  # Перезапуск через 1 секуду
    now = int(time.time())
    if (now-init_time)%60 == 0:
        print(now-init_time)
        
    checkVideoHb()
    checkVideoAddition(now, int(time.mktime((2020, 5, 28, 13, 50, 0, 0, 0, 0))), 'hbVitka.mp4')
    checkEnd(now, int(time.mktime((2020, 5, 28, 17, 40, 0, 0, 0, 0))))
    checkQustion1(now, int(time.mktime(lessons_times[0])))
    CheckQuestion2(now, int(time.mktime(lessons_times[1])))
    CheckQuest3(now, int(time.mktime(lessons_times[2])))
    CheckQuest4(now, int(time.mktime(lessons_times[3])))
    CheckQuest5(now, int(time.mktime(lessons_times[4])))
    CheckQuest6(now, int(time.mktime(lessons_times[5])))
    #*** more check...

checkTime()

bot.polling()