# pyHappyMarvin

запуск скрипта *фоновым процессом на **VPS - 

    nohup python script.py &

логи будут писаться в файле **nohup.out

Чтобы сразу писалось в лог можно **sys.stdout.flush() в коде ставить после print

***
**Либо в начале программы можно прописать

    if os.fork(): sys.exit()
    os.setsid()
    sys.stdin.close()
    sys.stdout.close()
    sys.stderr.close()
    fd = open("log/debug.log", "a", 1)
    sys.stdout = fd
    sys.stderr = fd

Потом можно запускать скрипт обычным образом

а лучше выделить всё это в отдельный модуль и импортировать его в те проекты, где он нужен. Тольок import должен быть первой строкой



