import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import YouTube
import customtkinter

def startdownload():
    try:
        ytLink = url_var.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        save_path = filedialog.askdirectory()  
        if save_path:
            video.download(save_path)
        finishLabel.configure(text="Downloaded", text_color="green")
    except Exception as e:
        print("Error", e)
        finishLabel.configure(text="Error", text_color="red")

def startdownloadmp4():
    try:
        ytLink = url_var_mp4.get()
        ytObject = YouTube(ytLink)
        audio = ytObject.streams.filter(only_audio=True).first()
        save_path = filedialog.askdirectory()  
        if save_path:  
            audio.download(save_path)
        finishLabel_2.configure(text="Downloaded", text_color="green")
    except Exception as e:
        print("Error", e)
        finishLabel_2.configure(text="Error", text_color="red")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Downloader")

title_style = {"font": ("Arial", 18, "bold")}
entry_style = {"width": 350, "height": 40, "font": ("Arial", 12)}
button_style = {"font": ("Arial", 12, "bold"), "width": 150, "height": 30}
label_style = {"font": ("Arial", 14)}

download_icon = Image.open("icon/download_icon.png")
download_icon = download_icon.resize((20, 20))
download_icon = ImageTk.PhotoImage(download_icon)


#download video interface
title = customtkinter.CTkLabel(app, text="Video Link", **title_style) 
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_var, **entry_style)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="", **label_style)
finishLabel.pack()

download = customtkinter.CTkButton(app, text="Download", image=download_icon, command=startdownload, **button_style)
download.pack(padx=20, pady=20)


#download audio interface
title = customtkinter.CTkLabel(app, text="Audio Link", **title_style)
title.pack(padx = 10, pady = 10)

url_var_mp4 = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_var_mp4, **entry_style)
link.pack()

finishLabel_2 = customtkinter.CTkLabel(app, text="", **label_style)
finishLabel_2.pack()

download = customtkinter.CTkButton(app, text="Download", image=download_icon, command=startdownloadmp4, **button_style)
download.pack(padx=20, pady=20)

app.mainloop()