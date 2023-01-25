from tkinter import *
from chat import get_response, bot_name

BLUE1 = "#4A6274"
BLUE2 = "#1f2933"
PEACH = "#de9e97"
PINK = "#b1838e"
TEXT_COLOR = "#dbd5d5"

FONT = "Quicksand_Book"
FONT_BOLD = "Quicksand_Bold"


class MedicalChatApp:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Medical ChatBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=500, bg=BLUE2)

        # head label
        head_label = Label(self.window, bg=BLUE2, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=8)
        head_label.place(relwidth=1)

        # divider
        line = Label(self.window, width=580, bg=BLUE1)
        line.place(relwidth=1, rely=0.07, relheight=0.02)

        # text input
        self.text_widget = Text(self.window, width=20, height=2, bg=BLUE2, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.79, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview())

        # bot label
        bottom_label = Label(self.window, bg=BLUE1, height=20)
        bottom_label.place(relwidth=1, rely=0.87)

        # input box
        self.msg_iput = Entry(bottom_label, bg=BLUE1, fg=TEXT_COLOR, font=FONT)
        self.msg_iput.place(relwidth=0.74, relheight=0.12, rely=0.045, relx=0.013)
        self.msg_iput.focus()
        self.msg_iput.bind("<Return>", self._on_enter_pressed)

        # send
        send_button = Button(bottom_label, text="SEND", font=FONT_BOLD, width=20, bg=PEACH, fg=BLUE2,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.79, rely=0.045, relheight=0.12, relwidth=0.18)

    def _on_enter_pressed(self, event):
        msg = self.msg_iput.get()
        self._insert_msg(msg, "You")

    def _insert_msg(self, msg, sender):
        if not msg:
            return
        self.msg_iput.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = MedicalChatApp()
    app.run()
