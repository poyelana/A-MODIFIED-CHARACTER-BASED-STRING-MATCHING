import tkinter
from jaro import *


def newjaro(s, t):
    '''NJaro distance between two strings.'''
    s_len = len(s)
    t_len = len(t)

    if s_len == 0 and t_len == 0:
        return 1

    match_distance = (max(s_len, t_len) // 2) - 1

    s_matches = [False] * s_len
    t_matches = [False] * t_len

    matches = 0
    transpositions = 0

    for i in range(s_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, t_len)

        for j in range(start, end):
            if t_matches[j]:
                continue
            if s[i] != t[j]:
                continue
            s_matches[i] = True
            t_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0

    k = 0
    for i in range(s_len):
        if not s_matches[i]:
            continue
        while not t_matches[k]:
            k += 1
        if s[i] != t[k]:
            transpositions += 1
        k += 1

    return ((matches / s_len) + (matches / t_len) + ((transpositions / 2) / matches)) / 2

#######

######





def show_entry_fields():
   str1 = str(e1.get())
   str2 = str(e2.get())
   str3.set(get_jaro_distance(str1,str2, winkler=False, scaling=0.1))
   str4.set(newjaro(str1,str2))
   str5.set(_get_matching_characters(str1, str2))

master = tkinter.Tk()
master.geometry('250x150')
master.resizable(0,0)
master.config(background="purple")
master.title('IMPROVED JARO-WINKLER ON STRING MATCHING')
tkinter.Label(master, text="String 1").grid(row=0)
tkinter.Label(master, text="String 2").grid(row=1)
tkinter.Label(master, text="Jaro").grid(row=2)
tkinter.Label(master, text="N Formula").grid(row=3)
tkinter.Label(master, text="Matching Characters").grid(row=4)


str1 = tkinter.StringVar()
str2 = tkinter.StringVar()
str3 = tkinter.StringVar()
str4 = tkinter.StringVar()
str5 = tkinter.StringVar()

##naming the entries
e1 = tkinter.Entry(master, textvariable=str1)
e2 = tkinter.Entry(master, textvariable=str2)
e3 = tkinter.Entry(master, textvariable=str3)
e4 = tkinter.Entry(master, textvariable=str4)
e5 = tkinter.Entry(master, textvariable=str5)

##packing entries

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

##EMPTY THE TEXT FIELD

e3.delete(0, tkinter.END)
e4.delete(0, tkinter.END)
e5.delete(0, tkinter.END)

##creating buttons

tkinter.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tkinter.W, pady=4)
tkinter.Button(master, text='Compare', command=show_entry_fields).grid(row=6, column=1, sticky=tkinter.W, pady=4)

master.mainloop()
