# # # # akun_member = [
# # # #     {
# # # #         "id": "",
# # # #         "username": "a",
# # # #         "password": "b"
# # # #     },
# # # #     {
# # # #         "id": "1",
# # # #         "username": "user1",
# # # #         "password": "pass1"
# # # #     }
# # # # ]
# # # # print([i["username"]for i in akun_member])

# # # import tkinter as tk
# # # from tkinter import messagebox

# # # def login():
# # #     user = entry_user.get()
# # #     pw = entry_pw.get()
# # #     if user == "jovan" and pw == "123":
# # #         messagebox.showinfo("Login", "Berhasil!")
# # #     else:
# # #         messagebox.showerror("Login", "Username/Password salah.")

# # # root = tk.Tk()
# # # root.title("Login")

# # # tk.Label(root, text="Username").pack()
# # # entry_user = tk.Entry(root)
# # # entry_user.pack()

# # # tk.Label(root, text="Password").pack()
# # # entry_pw = tk.Entry(root, show="*")
# # # entry_pw.pack()

# # # tk.Button(root, text="Login", command=login).pack()
# # # root.mainloop()

# # import tkinter as tk
# # from tkinter import ttk
# # import time

# # # Splash screen
# # splash = tk.Tk()
# # splash.overrideredirect(True)  # hilangkan border
# # splash.geometry("400x200+500+300")
# # tk.Label(splash, text="GwehMauJalan", font=("Arial", 24)).pack(pady=40)
# # progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="determinate")
# # progress.pack(pady=20)

# # for i in range(101):
# #     progress['value'] = i
# #     splash.update()
# #     time.sleep(0.03)

# # splash.destroy()

# # # Main window
# # root = tk.Tk()
# # root.title("GwehMauJalan")
# # tk.Label(root, text="Selamat datang!", font=("Arial", 18)).pack(pady=50)
# # root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# def pilih_rute():
#     pilihan = listbox.get(listbox.curselection())
#     messagebox.showinfo("Pilihan Rute", f"Kamu memilih: {pilihan}")

# root = tk.Tk()
# root.title("Pilih Rute")

# tk.Label(root, text="Pilih rute perjalanan:").pack(pady=10)

# listbox = tk.Listbox(root)
# listbox.pack()
# for r in ["Balikpapan-Samarinda", "Samarinda-Bontang", "Balikpapan-Bontang"]:
#     listbox.insert(tk.END, r)

# tk.Button(root, text="Pilih", command=pilih_rute).pack(pady=10)

# root.mainloop()
