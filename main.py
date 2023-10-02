import customtkinter as tk
import telebot


tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

root = tk.CTk()
root.title("Отправка заявки ver 2.0")
root.geometry("600x400")
tip_var = tk.StringVar()
name_var = tk.StringVar()

def submit():
     tip = tip_var.get()
     name = name_var.get()

     if (tip == '' and name == '') or (tip =='') or (name==''):
          att =tk.CTk()
          att.title("Ошибка")
          att.geometry("600x200")
          atxt = tk.CTkLabel(att, text="Все поля должны быть заполнены")
          atxt.pack(anchor="center",expand=1)
          att.mainloop()
     else:
          total = 'Новый запрос:'
          bot = telebot.TeleBot("!BOT API!")
          chat_id = 'Your ID'
          bot.send_message(chat_id, total)
          bot.send_message(chat_id, tip)
          bot.send_message(chat_id, name)
          #
          tip_var.set("")
          name_var.set("")
          ###
          window = tk.CTk()
          window.title("Успешно")
          window.geometry("600x200")
          label = tk.CTkLabel(window, text="Отправлено! Спасибо за использование программы)")
          label.pack(anchor="center", expand=1)
          ###
          close_button = tk.CTkButton(window, text="Закрыть окно", command=lambda: window.destroy())
          close_button.pack(anchor="center", expand=1)
     window.mainloop()
tip_label = tk.CTkLabel(root, text='Сообщение:', font=('calibre', 18, 'bold'))

tip_entry = tk.CTkEntry(root, textvariable=tip_var, font=('calibre', 18, 'normal'))

##################################################################
name_label = tk.CTkLabel(root, text='Название ПО:', font=('calibre', 18, 'bold'))


name_entry = tk.CTkEntry(root, textvariable=name_var, font=('calibre', 18, 'normal'))

###################################################################
sub_btn = tk.CTkButton(root, text='Отправить', command=submit)


tip_label.grid(row=0, column=0)
tip_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()