import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("☕ Cozy Pomo")
app.geometry("900x600")

label = ctk.CTkLabel(app, text="Welcome to Cozy Pomo!", font=("Courier", 24))
label.pack(pady=40)

app.mainloop()
