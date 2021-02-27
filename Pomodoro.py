import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

T_MIN = 25
T_BREAK = 5
t_now = dt.datetime.now()
t_pom = T_MIN * 60
t_delta = dt.timedelta(0, t_pom)
t_fut = t_now + t_delta
delta_sec = 1
t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Pomodoro Started!", "\nTime Now: " + t_now.strftime("%H:%M:%S") +
                    "\nTimer will set for 25 mins...\nStart From Now!")

total_pomodoros = 0
breaks = 0

while True:
    if t_now < t_fut:
        print('First tnow < tfut')
    elif t_fut <= t_now <= t_fin:
        print('Hooray! It is Break Time Now!')
        if breaks == 0:
            print('if break')
            for i in range(T_BREAK):
                winsound.Beep((i+100), 700)
            print('Hooray! It is Break Time Now!')
            breaks += 1
    else:
        print('Third tnow > tfut - Finished')
        print('\a')
        breaks = 0
        for i in range(10):
            winsound.Beep((i + 100), 500)
        usr_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another pomodoro?")
        total_pomodoros += 1

        if usr_ans == True:
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)
            continue
        elif usr_ans == False:
            print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
            messagebox.showinfo("Pomodoro Finished!", "\nTime Now: " + t_now.strftime("%H:%M") +
                                "\nYou completed " + str(total_pomodoros) + " pomodoro today!")
            break

    print('Sleeping...')
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")