from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.geometry("500x500")
root.title("Project 160")
root.configure( bg = "teal")

open1 = ImageTk.PhotoImage(Image.open("open.png"))
file1 = ImageTk.PhotoImage(Image.open("file.png"))
play1 = ImageTk.PhotoImage(Image.open("play.png"))
label_name = Label(root, text = "File Name : ")
label_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)
input1 = Entry(root)
input1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
text1 = Text(root, height = 5, width = 20, bg = "white", fg = "blue")
text1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
name = StringVar()

def openfile() :
    global name
    text1.delete(1.0,END)
    input1.delete(1.0,END)
    html_file = filedialog.askopenfilename(title = "Open HTML file", filetypes = (("HTML files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formattted_name = name.split('.')[0]
    input1.insert(END,formatted_name)
    root.title(formatted_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    text1.insert(END,paragraph)
    html_file.close()

open_btn = Button(root, image = open1, command = openfile)
play_btn = Button(root, image = play1)
file_btn = Button(root, image = file1)
open_btn.place(relx = 0.05, rely = 0.03, anchor = CENTER)
play_btn.place(relx = 0.07, rely = 0.05, anchor = CENTER)
file_btn.place(relx = 0.09, rely = 0.07, anchor = CENTER)
root.mainloop()