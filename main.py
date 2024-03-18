import tkinter
from pytube import YouTube
import customtkinter

def startdownload():
    try:
        ytLink = url_var.get()
        ytObject = YouTube(
            ytLink
        )
        video = ytObject.streams.get_highest_resolution()
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except Exception as e:
        print("Error", e)
        finishLabel.configure(text="Error", text_color="red")

def startdownloadmp4():
    try:
        ytLink = url_var_mp4.get()
        ytObject = YouTube(ytLink)
        audio = ytObject.streams.filter(only_audio=True).first()
        audio.download()
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

#download video interface
title = customtkinter.CTkLabel(app, text="Video Link", **title_style) 
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_var, **entry_style)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="", **label_style)
finishLabel.pack()

download = customtkinter.CTkButton(app, text="Download", command=startdownload, **button_style)
download.pack(padx=20, pady=20)

#download audio interface
title = customtkinter.CTkLabel(app, text="Audio Link", **title_style)
title.pack(padx = 10, pady = 10)

url_var_mp4 = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_var_mp4, **entry_style)
link.pack()

finishLabel_2 = customtkinter.CTkLabel(app, text="", **label_style)
finishLabel_2.pack()

download = customtkinter.CTkButton(app, text="Download", command=startdownloadmp4, **button_style)
download.pack(padx=20, pady=20)

app.mainloop()