from tkinter import Tk, Label, Frame, Button, Entry, ttk, Listbox, END, StringVar, Toplevel, filedialog, Scrollbar, X
import json
from urllib.request import urlopen
from pygame import mixer #pip install pygame
import os
from mutagen.mp3 import MP3 #pip install mutagen

try:
    page = urlopen(url)
    weatherData = json.loads(page.read())
except:
    url = "https://api.openweathermap.org/data/2.5/forecast?q=Salt+Lake+City,us&units=imperial&appid=4d399dd2f89e04d7a461815f8f2d3f79"
    page = urlopen(url)
    weatherData = json.loads(page.read())

def readJSON(filename):
    file = open(filename, "r")
    existingData = json.loads(file.read())
    file.close()
    return existingData

def writeJSON(existingData, filename):
    file = open(filename, 'w')
    file.write(json.dumps(existingData))
    file.close()

def createJSON(filename):
    writeJSON([], filename)

def addNoteEntry():
    data = readJSON('toDo.json')
    newNote = tab1_entry_input.get()
    data.append(newNote)
    writeJSON(data, 'toDo.json')
    tab1_entry_input.delete(0, END)
    tab1_listbox_notes.delete(0, END)
    printNotes()

def editNoteEntry():
    data = readJSON('toDo.json')
    try:
        selectedIndex = tab1_listbox_notes.curselection()[0]
        editNote = tab1_entry_input.get()
        data.pop(selectedIndex)
        data.insert(selectedIndex,editNote)
        writeJSON(data, 'toDo.json')
        tab1_entry_input.delete(0, END)
        tab1_listbox_notes.delete(0, END)
        printNotes()
    except:
        return

def deleteNoteEntry():
    data = readJSON('toDo.json')
    try:
        selectedIndex = tab1_listbox_notes.curselection()[0]
        data.pop(selectedIndex)
        writeJSON(data, 'toDo.json')
        tab1_listbox_notes.delete(0, END)
        printNotes()
    except:
        return

def printNotes():
    data = readJSON('toDo.json')
    for i in data:
        tab1_listbox_notes.insert(END, i)

def listHelp():
    global helpWindow
    try:
        helpWindow.destroy()
    except:
        pass
    instructions = """Add: Insert text into textbox at top, then press Add to add it to the bottom of the list\n
        Edit: Insert text into textbox at top, then press Edit with the desired item selected to edit that item\n
            Delete: Selected desired item, then press Delete to delete that item from the list"""
    helpWindow = Toplevel()
    helpWindow.title("To-Do List Help")
    helpWindow_label_help = Label(helpWindow, text = instructions)
    helpWindow_label_help.pack(side = 'top')
    helpWindow_btn_destroy = Button(helpWindow, text = "Close", command = helpWindow.destroy)
    helpWindow_btn_destroy.pack(side = 'top')

def changeCity():
    global url
    newCity = tab2_entry_city.get()
    newCity = newCity.strip()
    cityUrl = newCity.replace(" ","+")
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + cityUrl + ",us&units=imperial&appid=4d399dd2f89e04d7a461815f8f2d3f79"
    try:
        page = urlopen(url)
        weatherData = json.loads(page.read())
        currentDate = weatherData['list'][0]['dt_txt']
        currentDateTemp = weatherData['list'][0]['main']['temp']
        currentDateDescription = weatherData['list'][0]['weather'][0]['description']
        datePlusOne = weatherData['list'][8]['dt_txt']
        datePlusOneTemp = weatherData['list'][8]['main']['temp']
        datePlusOneDescription = weatherData['list'][8]['weather'][0]['description']
        datePlusTwo = weatherData['list'][16]['dt_txt']
        datePlusTwoTemp = weatherData['list'][16]['main']['temp']
        datePlusTwoDescription = weatherData['list'][16]['weather'][0]['description']
        datePlusThree = weatherData['list'][24]['dt_txt']
        datePlusThreeTemp = weatherData['list'][24]['main']['temp']
        datePlusThreeDescription = weatherData['list'][24]['weather'][0]['description']
        datePlusFour = weatherData['list'][32]['dt_txt']
        datePlusFourTemp = weatherData['list'][32]['main']['temp']
        datePlusFourDescription = weatherData['list'][32]['weather'][0]['description']
        tab2_label_cityName.config(text=newCity)
        tab2_label_currentDate.config(text = f'{currentDate}: {currentDateTemp}°F - {currentDateDescription}')
        tab2_label_datePlusOne.config(text = f'{datePlusOne}: {datePlusOneTemp}°F - {datePlusOneDescription}')
        tab2_label_datePlusTwo.config(text = f'{datePlusTwo}: {datePlusTwoTemp}°F - {datePlusTwoDescription}')
        tab2_label_datePlusThree.config(text = f'{datePlusThree}: {datePlusThreeTemp}°F - {datePlusThreeDescription}')
        tab2_label_datePlusFour.config(text = f'{datePlusFour}: {datePlusFourTemp}°F - {datePlusFourDescription}')
    except:
        tab2_label_cityName.config(text="")
        tab2_label_currentDate.config(text="Unrecognized City. Please enter a valid US city.")
        tab2_label_datePlusOne.config(text="")
        tab2_label_datePlusTwo.config(text="")
        tab2_label_datePlusThree.config(text="")
        tab2_label_datePlusFour.config(text="")
    tab2_entry_city.delete(0, 'end')

def btnPressed(input):
    global math
    if problem == "Error" or problem == "Cannot divide by zero":
        math = ""
    math = math + input
    problem.set(math)

def solveProblem():
    global math
    try:
        solution = str(eval(math))
        problem.set(solution)
        math = solution
    except ZeroDivisionError:
        problem.set("Cannot divide by zero")
        math = ""
    except:
        problem.set("Error")
        math = ""

def clearProblem():
    global math
    math = ""
    problem.set("")

def addSongEntry(song):
    data = readJSON('songList.json')
    data.append(song)
    writeJSON(data, 'songList.json')
    tab4_listbox_music.delete(0, END)
    printSongs()

def deleteSong():
    data = readJSON('songList.json')
    try:
        selectedIndex = tab4_listbox_music.curselection()[0]
        data.pop(selectedIndex)
        writeJSON(data, 'songList.json')
        tab4_listbox_music.delete(0, END)
        printSongs()
    except:
        return

def printSongs():
    data = readJSON('songList.json')
    for i in data:
        tab4_listbox_music.insert(END, os.path.basename(i))

def addSong():
    song = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("MP3 files", "*.mp3"), ("WAV files", "*.wav")))
    addSongEntry(song)

def playSong():
    global isPaused
    global canPause
    mixer.init()
    if isPaused:
        mixer.music.unpause()
        isPaused = False
        canPause = True
    else:
        data = readJSON('songList.json')
        stopSong()
        try:
            songIndex = tab4_listbox_music.curselection()[0]
        except:
            return
        song = data[songIndex]
        mixer.music.load(song)
        mixer.music.play()

        fileType = os.path.splitext(song)
        fileType = fileType[1]
        if fileType == '.mp3':
            songAudio = MP3(song)
            song_length = songAudio.info.length
        else:
            songAudio = mixer.Sound(song) #mixer.Sound crashes when dealing w/ mp3 files
            song_length = songAudio.get_length()
        songMinute, songSecond = divmod(song_length, 60)
        songMinute = round(songMinute)
        songSecond = round(songSecond)
        if songSecond >= 60:
            songSecond -= 60
            songMinute += 1
        songLengthFormatted = '{:02d}:{:02d}'.format(songMinute, songSecond)
        tab4_label_length.config(text = f"Length: {songLengthFormatted}")
        canPause = True

def pauseSong():
    global isPaused
    global canPause
    if canPause:
        isPaused = True
        mixer.music.pause()
    else:
        return

def stopSong():
    global isPaused
    global canPause
    isPaused = False
    canPause = False
    mixer.music.stop()

def startTimer():
    global timerRunning, timerPrep, hour, minute, second
    if timerPrep:
        if timerRunning:
            timerRunning = False
            return
        hour = tab5_entry_hour.get()
        minute = tab5_entry_minute.get()
        second = tab5_entry_second.get()
        if len(hour) == 0:
            hour = 0
        if len(minute) == 0:
            minute = 0
        if len(second) == 0:
            second = 0
        try:
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            if hour < 0 or minute < 0 or second < 0:
                raise ValueError('All time values must be integers greater than or equal to 0')
        except:
            return
        timerRunning = True
        timerPrep = False
        tab5_btn_start.config(text = "Pause", command = pauseTimer)
    if timerRunning:
        while second >= 60:
            second -= 60
            minute += 1
        while minute >= 60:
            minute -= 60
            hour += 1

        tab5_label_timer.config(text = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second))

        hour = int(hour)
        minute = int(minute)
        second = int(second)

        if second > 0:
            second -= 1
        elif second == 0:
            if minute == 0 and hour == 0:
                playTimerSound()
            else:
                second = 59
                if minute > 0:
                    minute -= 1
                elif minute == 0:
                    if hour > 0:
                        minute = 59
                        hour -= 1

        if timerRunning:
            tab5.after(1000, startTimer)
    
def cancelTimer():
    global timerPrep
    timerPrep = True
    tab5_label_timer.config(text = '00:00:00')
    tab5_btn_start.config(text = "Start", command = startTimer)

def pauseTimer():
    global timerRunning, timerPrep
    timerRunning = False
    tab5_btn_start.config(text = "Resume", command = resumeTimer)

def resumeTimer():
    global timerRunning, timerPrep
    timerRunning = True
    startTimer()
    tab5_btn_start.config(text = "Pause", command = pauseTimer)

def playTimerSound():
    global timerRunning, timerPrep
    timerRunning = False
    timerPrep = True
    tab5_btn_start.config(text = "Start", command = startTimer)
    filename = 'Timer Sounds\\radar_-_ios_7.mp3'
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

try:
    file = open("toDo.json", "r")
    file.close()
except FileNotFoundError:
    createJSON('toDo.json')
try:
    file = open("songList.json", "r")
    file.close()
except FileNotFoundError:
    createJSON('songList.json')

root = Tk()
root.title('3rd Party Frameworks Final')
root.resizable(False, False)
tabs = ttk.Notebook(root)

tab1 = ttk.Frame(tabs)
tabs.add(tab1, text = 'To-Do List')

tab2 = ttk.Frame(tabs)
tabs.add(tab2, text = 'Weather Forecast')

tab3 = ttk.Frame(tabs)
tabs.add(tab3, text = 'Calculator')

tab4 = ttk.Frame(tabs)
tabs.add(tab4, text = 'Music Player')

tab5 = ttk.Frame(tabs)
tabs.add(tab5, text = 'Timer')

tabs.pack(side = 'top')

#To-Do List Tab------------------------------

tab1_frame_top = Frame(tab1)
tab1_frame_bottom = Frame(tab1)
tab1_frame_top.pack(side = 'top')
tab1_frame_bottom.pack(side = 'top')

tab1_entry_input = Entry(tab1_frame_top, width = 50)
tab1_btn_add = Button(tab1_frame_top, text = 'Add', command = addNoteEntry)
tab1_btn_edit = Button(tab1_frame_top, text = 'Edit', command = editNoteEntry)
tab1_btn_delete = Button(tab1_frame_top, text = 'Delete', command = deleteNoteEntry)
tab1_btn_help = Button(tab1_frame_top, text = 'Help', command = listHelp)
tab1_entry_input.pack(side = "top")
tab1_btn_add.pack(side = 'left')
tab1_btn_edit.pack(side = "left")
tab1_btn_delete.pack(side = "left")
tab1_btn_help.pack(side = "left")

tab1_scrollbar_toDo = Scrollbar(tab1_frame_bottom, orient = 'horizontal')
tab1_listbox_notes = Listbox(tab1_frame_bottom, width = 50, xscrollcommand = tab1_scrollbar_toDo.set)
tab1_scrollbar_toDo.config(command=tab1_listbox_notes.xview)
tab1_listbox_notes.pack(side = "top")
tab1_scrollbar_toDo.pack(side='top', fill=X)

printNotes()

#Weather Forecast Tab------------------------

currentDate = weatherData['list'][0]['dt_txt']
currentDateTemp = weatherData['list'][0]['main']['temp']
currentDateDescription = weatherData['list'][0]['weather'][0]['description']

datePlusOne = weatherData['list'][8]['dt_txt']
datePlusOneTemp = weatherData['list'][8]['main']['temp']
datePlusOneDescription = weatherData['list'][8]['weather'][0]['description']

datePlusTwo = weatherData['list'][16]['dt_txt']
datePlusTwoTemp = weatherData['list'][16]['main']['temp']
datePlusTwoDescription = weatherData['list'][16]['weather'][0]['description']

datePlusThree = weatherData['list'][24]['dt_txt']
datePlusThreeTemp = weatherData['list'][24]['main']['temp']
datePlusThreeDescription = weatherData['list'][24]['weather'][0]['description']

datePlusFour = weatherData['list'][32]['dt_txt']
datePlusFourTemp = weatherData['list'][32]['main']['temp']
datePlusFourDescription = weatherData['list'][32]['weather'][0]['description']

tab2_frame_top = Frame(tab2)
tab2_frame_bottom = Frame(tab2)
tab2_frame_top.pack(side = 'top')
tab2_frame_bottom.pack(side = 'top')

tab2_label_cityEntry = Label(tab2_frame_top, text = "Enter US City: ")
tab2_label_cityEntry.pack(side = 'left')
tab2_entry_city = Entry(tab2_frame_top)
tab2_entry_city.pack(side = 'left')
tab2_btn_submit = Button(tab2_frame_top, text = 'Submit', command = changeCity)
tab2_btn_submit.pack(side = 'left')

tab2_label_cityName = Label(tab2_frame_bottom,
    text = weatherData['city']['name']
)
tab2_label_currentDate = Label(tab2_frame_bottom,
    text = f'{currentDate}: {currentDateTemp}°F - {currentDateDescription}'
)
tab2_label_datePlusOne = Label(tab2_frame_bottom,
    text = f'{datePlusOne}: {datePlusOneTemp}°F - {datePlusOneDescription}'
)
tab2_label_datePlusTwo = Label(tab2_frame_bottom,
    text = f'{datePlusTwo}: {datePlusTwoTemp}°F - {datePlusTwoDescription}'
)
tab2_label_datePlusThree = Label(tab2_frame_bottom,
    text = f'{datePlusThree}: {datePlusThreeTemp}°F - {datePlusThreeDescription}'
)
tab2_label_datePlusFour = Label(tab2_frame_bottom,
    text = f'{datePlusFour}: {datePlusFourTemp}°F - {datePlusFourDescription}'
)

tab2_label_cityName.pack(side = 'top')
tab2_label_currentDate.pack(side = 'top')
tab2_label_datePlusOne.pack(side = 'top')
tab2_label_datePlusTwo.pack(side = 'top')
tab2_label_datePlusThree.pack(side = 'top')
tab2_label_datePlusFour.pack(side = 'top')

#Calculator Tab------------------------------

math = ""
problem = StringVar()

tab3_frame_top = Frame(tab3)
tab3_frame_bottom = Frame(tab3)
tab3_frame_top.pack(side = 'top')
tab3_frame_bottom.pack(side = 'top')

tab3_entry_equation = Entry(tab3_frame_top, width = 37, state = 'readonly', textvariable = problem)
tab3_btn_9 = Button(tab3_frame_bottom, text = '9', height = 3, width = 5, command = lambda: btnPressed('9'))
tab3_btn_8 = Button(tab3_frame_bottom, text = '8', height = 3, width = 5, command = lambda: btnPressed('8'))
tab3_btn_7 = Button(tab3_frame_bottom, text = '7', height = 3, width = 5, command = lambda: btnPressed('7'))
tab3_btn_6 = Button(tab3_frame_bottom, text = '6', height = 3, width = 5, command = lambda: btnPressed('6'))
tab3_btn_5 = Button(tab3_frame_bottom, text = '5', height = 3, width = 5, command = lambda: btnPressed('5'))
tab3_btn_4 = Button(tab3_frame_bottom, text = '4', height = 3, width = 5, command = lambda: btnPressed('4'))
tab3_btn_3 = Button(tab3_frame_bottom, text = '3', height = 3, width = 5, command = lambda: btnPressed('3'))
tab3_btn_2 = Button(tab3_frame_bottom, text = '2', height = 3, width = 5, command = lambda: btnPressed('2'))
tab3_btn_1 = Button(tab3_frame_bottom, text = '1', height = 3, width = 5, command = lambda: btnPressed('1'))
tab3_btn_0 = Button(tab3_frame_bottom, text = '0', height = 3, width = 5, command = lambda: btnPressed('0'))
tab3_btn_add = Button(tab3_frame_bottom, text = '+', height = 3, width = 5, command = lambda: btnPressed('+'))
tab3_btn_subtract = Button(tab3_frame_bottom, text = '-', height = 3, width = 5, command = lambda: btnPressed('-'))
tab3_btn_multiply = Button(tab3_frame_bottom, text = '*', height = 3, width = 5, command = lambda: btnPressed('*'))
tab3_btn_divide = Button(tab3_frame_bottom, text = '/', height = 3, width = 5, command = lambda: btnPressed('/'))
tab3_btn_equals = Button(tab3_frame_bottom, text = '=', height = 3, width = 5, command = solveProblem)
tab3_btn_clear = Button(tab3_frame_bottom, text = 'C', height = 3, width = 5, command = clearProblem)
tab3_btn_lParantheses = Button(tab3_frame_bottom, text = '(', height = 3, width = 5, command = lambda: btnPressed('('))
tab3_btn_rParantheses = Button(tab3_frame_bottom, text = ')', height = 3, width = 5, command = lambda: btnPressed(')'))
tab3_btn_decimal = Button(tab3_frame_bottom, text = '.', height = 3, width = 5, command = lambda: btnPressed('.'))
tab3_btn_mod = Button(tab3_frame_bottom, text = 'mod', height = 3, width = 5, command = lambda: btnPressed('%'))

tab3_entry_equation.pack(side = 'top')
tab3_btn_7.grid(column=0,row=0)
tab3_btn_8.grid(column=1,row=0)
tab3_btn_9.grid(column=2,row=0)
tab3_btn_add.grid(column=3,row=0)
tab3_btn_lParantheses.grid(column=4,row=0)
tab3_btn_4.grid(column=0,row=1)
tab3_btn_5.grid(column=1,row=1)
tab3_btn_6.grid(column=2,row=1)
tab3_btn_subtract.grid(column=3,row=1)
tab3_btn_rParantheses.grid(column=4,row=1)
tab3_btn_1.grid(column=0,row=2)
tab3_btn_2.grid(column=1,row=2)
tab3_btn_3.grid(column=2,row=2)
tab3_btn_multiply.grid(column=3,row=2)
tab3_btn_decimal.grid(column=4,row=2)
tab3_btn_clear.grid(column=0,row=3)
tab3_btn_0.grid(column=1,row=3)
tab3_btn_equals.grid(column=2,row=3)
tab3_btn_divide.grid(column=3,row=3)
tab3_btn_mod.grid(column=4,row=3)

#Music Player Tab----------------------------

isPaused = False
canPause = False

tab4_frame_left = Frame(tab4, padx = 20)
tab4_frame_right = Frame(tab4, padx = 40)
tab4_frame_left.pack(side = 'left')
tab4_frame_right.pack(side = 'left')

tab4_scrollbar_music = Scrollbar(tab4_frame_left, orient = 'horizontal')
tab4_listbox_music = Listbox(tab4_frame_left, width = 50, xscrollcommand = tab4_scrollbar_music.set)
tab4_scrollbar_music.config(command=tab4_listbox_music.xview)
tab4_btn_add = Button(tab4_frame_left, text = 'Add', command = addSong)
tab4_btn_delete = Button(tab4_frame_left, text = 'Delete', command = deleteSong)
tab4_label_length = Label(tab4_frame_right, text = "Length: --:--")
tab4_btn_play = Button(tab4_frame_right, text = 'Play', command = playSong)
tab4_btn_pause = Button(tab4_frame_right, text = 'Pause', command = pauseSong)
tab4_btn_stop = Button(tab4_frame_right, text = 'Stop', command = stopSong)

tab4_listbox_music.pack(side = 'top')
tab4_scrollbar_music.pack(side='top', fill=X)
tab4_btn_add.pack(side = 'top')
tab4_btn_delete.pack(side = 'top')
tab4_label_length.pack(side = 'top')
tab4_btn_play.pack(side = 'top')
tab4_btn_pause.pack(side = 'top')
tab4_btn_stop.pack(side = 'top')

printSongs()

#Timer Tab-----------------------------------

timerRunning = False
timerPrep = True

tab5_frame_top = Frame(tab5)
tab5_frame_middle = Frame(tab5)
tab5_frame_bottom = Frame(tab5)
tab5_frame_top.pack(side = 'top')
tab5_frame_middle.pack(side = 'top')
tab5_frame_bottom.pack(side = 'top')

tab5_label_timer = Label(tab5_frame_top, text = "00:00:00")
tab5_label_timer.config(font = ('Verdana 30 bold'))
tab5_label_hour = Label(tab5_frame_middle, text = "Hour: ")
tab5_entry_hour = Entry(tab5_frame_middle)
tab5_label_minute = Label(tab5_frame_middle, text = "Minute: ")
tab5_entry_minute = Entry(tab5_frame_middle)
tab5_label_second = Label(tab5_frame_middle, text = "Second: ")
tab5_entry_second = Entry(tab5_frame_middle)
tab5_btn_start = Button(tab5_frame_bottom, text = "Start", command = startTimer)
tab5_btn_reset = Button(tab5_frame_bottom, text = 'Cancel', command = cancelTimer)

tab5_label_timer.pack(side = 'top')
tab5_label_hour.pack(side = 'left')
tab5_entry_hour.pack(side = 'left')
tab5_label_minute.pack(side = 'left')
tab5_entry_minute.pack(side = 'left')
tab5_label_second.pack(side = 'left')
tab5_entry_second.pack(side = 'left')
tab5_btn_start.pack(side = 'left')
tab5_btn_reset.pack(side = 'left')

root.mainloop()
