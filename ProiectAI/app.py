from tkinter import *
from chat import get_response, bot_name

BLUE1 = "#4A6274"
BLUE2 = "#1f2933"
PEACH = "#de9e97"
PINK = "#b1838e"
TEXT_COLOR = "#dbd5d5"

GREEN1 = "#4E6C50"
BEIGE1 = "#F2DEBA"

BEIGE2 = "#D7C0AE"
BLUEGREY = "#B7C4CF"

GREY1 = "#7F8487"
GREY2 = "#2B2B2B"

FONT = "Quicksand_Book"
FONT_BOLD = "Quicksand_Bold"


class MedicalChatApp:

    theme = 1;
    def __init__(self):
        self.window = Tk()
        self._setup_main_window(BEIGE1, GREEN1)

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self, color1, color2):
        self.window.title("Medical ChatBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=500, bg=color2)

        # head label
        head_label = Label(self.window, bg=color1, fg=color2, text="Welcome", font=FONT_BOLD, pady=8)
        head_label.place(relwidth=1)
        settings_button = Button(self.window, text="THEME", font=FONT_BOLD, width=20, bg=PEACH, fg=color2,
                             command=lambda: self._change_theme(None))
        settings_button.place(relx=0.79, rely=0.006, relheight=0.07, relwidth=0.18)

        # divider
        line = Label(self.window, width=580, bg=BLUE1)
        line.place(relwidth=1, rely=0.07, relheight=0.02)

        # text input
        self.text_widget = Text(self.window, width=20, height=2, bg=color2, fg=color1, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.79, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview())

        # bot label
        bottom_label = Label(self.window, bg=color1, height=20)
        bottom_label.place(relwidth=1, rely=0.87)

        # input box
        self.msg_iput = Entry(bottom_label, bg=color1, fg=color2, font=FONT)
        self.msg_iput.place(relwidth=0.74, relheight=0.12, rely=0.045, relx=0.013)
        self.msg_iput.focus()
        self.msg_iput.bind("<Return>", self._on_enter_pressed)

        # send
        send_button = Button(bottom_label, text="SEND", font=FONT_BOLD, width=20, bg=PEACH, fg=color2,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.79, rely=0.045, relheight=0.12, relwidth=0.18)

    def _on_enter_pressed(self, event):
        msg = self.msg_iput.get()
        self._insert_msg(msg, "You")


    def _change_theme(self, event):
        self.theme = self.theme+1;
        if (self.theme == 1):
            color1 = BLUE1
            color2 = BLUE2
        elif (self.theme == 2):
            color1 = GREEN1
            color2 = BEIGE1
        elif (self.theme == 3):
            color1 = GREY2
            color2 = GREY1
        else:
            self.theme = 0
            color1 = BEIGE1
            color2 = BLUEGREY
        self._setup_main_window(color1,color2)



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
