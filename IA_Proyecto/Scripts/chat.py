import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import google.generativeai as genai

genai.configure(api_key="AIzaSyAX4nYQR3NLW0ORVTzN6uM-K_GckI50zLI")
model = genai.GenerativeModel('gemini-pro')
history = []


class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot - Bellow")

        self.chat_window = scrolledtext.ScrolledText(master, state='disabled', wrap='word', height=20)
        self.chat_window.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.input_frame = tk.Frame(master)
        self.input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.input_entry = tk.Entry(self.input_frame, width=50, font=("Arial", 12))
        self.input_entry.pack(side=tk.LEFT)
        self.input_entry.bind("<Return>", self.send_message)


        arrow_icon = Image.open("flecha_icon.png").resize((16, 16))
        arrow_icon = ImageTk.PhotoImage(arrow_icon)

        self.send_button = tk.Button(self.input_frame, image=arrow_icon, command=self.send_message,
                                     bg=master.cget("bg"), bd=0)
        self.send_button.image = arrow_icon
        self.send_button.pack(side=tk.RIGHT, padx=5)

        self.model = genai.GenerativeModel('gemini-pro')
        self.history = []


        self.user_icon = Image.open("1.png").resize((40, 40))
        self.user_icon = ImageTk.PhotoImage(self.user_icon)
        self.assistant_icon = Image.open("2.png").resize((40, 40))
        self.assistant_icon = ImageTk.PhotoImage(self.assistant_icon)

    def send_message(self, event=None):
        message = self.input_entry.get().strip()
        if message:
            self.display_message("Tu: " + message, 'user')
            if message.lower() == "salir":
                self.master.quit()
            else:
                response = self.model.generate_content(message)
                self.display_message("Bot: " + response.text, 'assistant')
        self.input_entry.delete(0, 'end')

    def display_message(self, message, role):
        self.chat_window.configure(state='normal')
        icon = self.user_icon if role == 'user' else self.assistant_icon
        icon_label = tk.Label(self.chat_window, image=icon)
        icon_label.image = icon
        self.chat_window.window_create(tk.END, window=icon_label)
        self.chat_window.insert(tk.END, ' ' + message + '\n')
        self.chat_window.see(tk.END)
        self.chat_window.configure(state='disabled')


def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
