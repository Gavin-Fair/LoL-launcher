from tkinter import *
import os
import smtplib
import time


window = Tk()

window.geometry("840x840")

window.title("Sus Launcher")

window.resizable(width=False, height=False)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

message = f"""From: Sus Launcher
to: YOU!
subject: Welcome to Sus Launcher\n
Hello,\n
You are reciveing this email as you have recently signed up for our newsletter.\n
Every so often you will get emails like these with news about the launcher and upcoming sales\n
Thankyou for choosing Sus Launcher and as always, stay sussy\n
\n
    Best regards\n
        -Gavin Fair (creator of Sus Launcher)
"""

# fucntions

def sus():
    os.startfile(r"C:\Riot Games\League of Legends\LeagueClient.exe")
    time.sleep(2)
    window.destroy()

def email():
    old_emails = entry.get()
    server.login("EMAIL", "PASWORD")
    server.sendmail("EMAIL",
                    old_emails,
                    message)
    server.quit

# Background, title, and icon

icon = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\GUI\among.png")
window.iconphoto(True, icon)
window.config(background="#FF503C")

# Label

photo = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\GUI\this.png")
label = Label(window,
              text="!!You are about to be sus!!",
              font=("Arial", 40, "bold"),
              fg="black",
              bg="#FF503C",
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()

# Button

button = Button (window,
                text="Click to be sus",
                fg="black",
                bg="#FF503C",
                font=("Comic Sans", 30),
                command=sus,
                activeforeground="black",
                activebackground="#FF503C")

button.pack()

# email label

label2 = Label(window,
          text="Put your email to sign up for our newsletter",
          font=("Ariel", 10),
          fg="Black",
          bg="#FF503C")

label2.pack()

# email

entry = Entry(window,
              font=("Arial",20))
entry.pack()

# enter button

enter = Button(window,
               text="Enter",
               pady=6.7,
               padx=10,
               bg="#FF503C",
               activeforeground="black",
               activebackground="#FF503C",
               command=email)
enter.place(x=580, y=759)

window.mainloop()
