from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == '__main__':
    root = Tk()

    # => Basic Tkinter Setup
    root.wm_iconbitmap('notepad.ico')
    root.geometry("680x778")
    root.title("Untitled - Notepad")

    # => Text Area
    textArea = Text(root, font="comicsansms 14")
    file = None
    textArea.pack(expand=True, fill=BOTH)

    # => Creating Menubar
    MenuBar = Menu(root)
    root.config(menu=MenuBar)

# ====================================== Functions =================================================
    def NewFile():
        global file
        root.title('Untitled - Notepad')
        file = None
        textArea.delete(1.0, END)


    def OpenFile():
        global file
        file = askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file=None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            textArea.delete(1.0, END)
            f = open(file, 'r')
            textArea.insert(1.0, f.read())
            f.close()
            


    def SaveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if file == "":
                file = None

            else:
                f = open(file, 'w')
                f.write(textArea.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + " - Notepad")
        
        else:
            f = open(file, 'w')
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")


    def ExitFile():
        root.destroy()

    def cut():
        textArea.event_generate('<<Cut>>')

    def copy():
        textArea.event_generate('<<Copy>>')

    def paste():
        textArea.event_generate('<<Paste>>')

    def about():
        showinfo("About", "Notepad Made by Malhar")

# ==================================================================================================


# ====================================== FileMenu =================================================
    FileMenu = Menu(MenuBar, tearoff=0)
    # => To open new file
    FileMenu.add_command(label="New", command=NewFile)
    # => To open already existing file
    FileMenu.add_command(label="Open", command=OpenFile)
    # To save current File
    FileMenu.add_command(label="Save", command=SaveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=ExitFile)

    MenuBar.add_cascade(label="File", menu=FileMenu)
    
# ==================================================================================================


# ====================================== EditMenu ==================================================
    EditMenu = Menu(MenuBar, tearoff=0)

    # => To add cut, copy & paste command
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)
# ==================================================================================================


# ====================================== HelpMenu ==================================================
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)

# ==================================================================================================


# ====================================== Scroll Bar =================================================
    scrollbar = Scrollbar(textArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbar.set)

# ====================================================================================================
    root.mainloop()