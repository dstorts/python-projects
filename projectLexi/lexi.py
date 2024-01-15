import os
from tkinter import *
from tkinter import ttk, filedialog

root = Tk() #the main window
root.title("Lexi the Namer")
root.geometry('800x500')
list_episode_names = [] #parallel list with episode_numbers to record intended episode file names
list_episode_numbers = [] #parallel list with episode_names to record intended episode number
list_episode_dirs = [] #parallel list with episode_currnames to record directories to every episode in the given directory
list_episode_currnames = [] #parallel list with episode_dirs to record current episode file names for easy display
list_episode_filetypes = [] #parrallel list with episode_currnames to record current episode file types to handle heterogenous selections

def clearNames():
    if lbox_names.size() > 0 and lbox_names.size() > 1:
        lbox_names.delete(0,lbox_names.size())
    elif lbox_names.size() > 0:
        lbox_names.delete(0)
    list_episode_names.clear()
    list_episode_numbers.clear()
    if len(entry_namefile_path.get()) > 0 and len(entry_namefile_path.get()) > 1:
        entry_namefile_path.delete(0,len(entry_namefile_path.get()))
    elif len(entry_namefile_path.get()) > 0:
        entry_namefile_path.delete(0)

def clearEpisodes():
    if lbox_episodes.size() > 0 and lbox_episodes.size() > 1:
        lbox_episodes.delete(0,lbox_episodes.size())
    elif lbox_episodes.size() > 0:
        lbox_episodes.delete(0)
    list_episode_dirs.clear()
    list_episode_currnames.clear()
    list_episode_filetypes.clear()
    if len(entry_series_path.get()) > 0 and len(entry_series_path.get()) > 1:
        entry_series_path.delete(0,len(entry_series_path.get()))
    elif len(entry_series_path.get()) > 0:
        entry_series_path.delete(0)

def browseForNameFile():
    #entry_namefile_path.delete(1,entry_namefile_path.size())
    namefiledir=open(filedialog.askopenfilename(initialdir = "/",
                                                             title = "Select Names file",
                                                             filetypes = (
                                                                 ("text files","*.txt"),
                                                                 ("all files","*.*")
                                                             )))
    entry_namefile_path.insert(0,namefiledir.name)
    nameslist=namefiledir.readlines() #get a list of each line in the text file

    #get rid of all lines that start with comment character '#' or are empty
    x = 0
    episode_count = 0
    line_count = len(nameslist)-1
    while line_count >= 0:
        comment_line = re.search("^#",nameslist[line_count])
        new_line = re.search("^\n",nameslist[line_count])
        if comment_line:
            print("%scomment line"%(line_count))
            nameslist.pop(line_count)
        elif new_line:
            print("%snew line"%(line_count))
            nameslist.pop(line_count)
        else:
            print("%svalid"%(line_count))
            episode_count += 1
        line_count -= 1
    episode_count += 1 #correct for starting at zero
    x = 0
    for n in nameslist:
        if n[len(n)-1] == '\n':
            nameslist[x] = n[0:len(n) - 1]  # get rid of the last character in this name, the newline character
        x+=1
    print(len(nameslist[0]))
    x = 0
    for n in nameslist:
        lbox_names.insert(x,n) #make list box reflect what is in nameslist in order
        list_episode_names.append(nameslist[x])
        if episode_count < 100:
            #here if episode count is double digits or single digits
            if x < 9:
                list_episode_numbers.append("0%s"%(x+1))
            else:
                list_episode_numbers.append("%s"%(x+1))
        elif episode_count > 99:
            #here if episode count is triple digits
            if x < 10:
                list_episode_numbers.append("00%s"%(x+1))
            elif x < 100:
                list_episode_numbers.append("0%s"%(x+1))
            else:
                list_episode_numbers.append("%s"%(x+1))
        x+=1
    print(episode_count)
    print(list_episode_numbers)
    namefiledir.close() #close the text file we read from

def seriesDirectory():
    clearEpisodes()
    path = ""
    filetypes = (("Mp4 files",".mp4"),("Mkv files",".mkv"),("All files","*.*"))
    first = TRUE
    i = 0
    index_path_tail = 0 #record index of directory in string
    index_fileext_begin = 0 #record index of the period for fileextension
    for filedir in filedialog.askopenfilenames(title='Open files',initialdir=path,filetypes=filetypes):
        if first:
            index_path_tail = filedir.rfind('/')
            entry_series_path.insert(0,filedir[0:index_path_tail+1])
            first = FALSE
        list_episode_dirs.append(filedir)
        index_fileext_begin = filedir.rfind('.') #use rfind to find last instance of a period, marks file extension
        list_episode_currnames.append(filedir[(index_path_tail+1):index_fileext_begin])
        list_episode_filetypes.append(filedir[index_fileext_begin:len(filedir)])
        lbox_episodes.insert(i,list_episode_currnames[i])
        i+=1

    print(list_episode_dirs)
    print(list_episode_currnames)
    print(list_episode_filetypes)

def renameMyFiles():
    if entry_series_path.get() != "" and lbox_names.size() > 0 and lbox_episodes.size() > 0:
        dest = ""
        episodes_path = entry_series_path.get()
        #find the name selected in the list, if any, to start new names from
        selection = lbox_names.curselection()
        index_name_start = 0
        if len(selection) != 0:
            if selection[0] >= 0:
                index_name_start = selection[0]
        e = 0
        for src in list_episode_dirs:
            if index_name_start+1 > len(list_episode_names):
                return #break out of loop if there are no more names since user can start at their selected name
            dest = episodes_path + list_episode_numbers[index_name_start] + " - " + list_episode_names[index_name_start] + list_episode_filetypes[e]
            os.rename(src, dest)
            e+=1
            index_name_start+=1

#GUI stuff
frame_series_input = Frame(root, bd=3, height=20, width=600)
frame_series_input.grid(row=1,column=0,padx=10,columnspan=3)

lbl_series_path = Label(frame_series_input, text="Series Directory:")
entry_series_path = Entry(frame_series_input, bd=3, width=55)
#entry_series_path.insert(0,"c:/videos/anime")
btn_series_path = Button(frame_series_input, text="Browse for Series Folder", command=seriesDirectory)
lbl_series_path.pack(side=LEFT)
entry_series_path.pack(side=LEFT)
btn_series_path.pack(side=LEFT)

frame_namefile_input = Frame(root, bd=3, height=20, width=600)
frame_namefile_input.grid(row=2, column=0,columnspan=3)

lbl_namefile_path = Label(frame_namefile_input, text="Name File Directory:")
entry_namefile_path = Entry(frame_namefile_input, bd=3, width=55)
#entry_namefile_path.insert(0,"c:/namefiles/anime")
btn_namefile_path = Button(frame_namefile_input, text="Browse for Name Files", command=browseForNameFile)
btn_clearnames = Button(frame_namefile_input, text="Clear Names List", command=clearNames)
lbl_namefile_path.pack(side=LEFT)
entry_namefile_path.pack(side=LEFT)
btn_namefile_path.pack(side=LEFT)
btn_clearnames.pack(side=LEFT,padx=5)

lbl_episodesfound = Label(root,text="List of Files Found in Series Directory:")
lbl_episodesfound.grid(row=3, column=0, pady=10)
lbox_episodes = Listbox(root, width=40, height=16)
lbox_episodes.grid(row=4,column=0)

lbl_namesfound = Label(root, text="List of Names found in Names File Directory")
lbl_namesfound.grid(row=3, column=1, pady=10)

lbox_names = Listbox(root, width=45, height=16,selectmode=SINGLE)
lbox_names.grid(row=4, column=1)

btn_doIt = Button(root, text="Rename the Files!", height=3,width=24,bg="green",fg="white",activebackground="yellow", command=renameMyFiles)
btn_doIt.grid(row=5, column=0, columnspan=2)

root.mainloop()