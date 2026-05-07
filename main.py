import customtkinter as ctk
import os

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class TextApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Disappearing Text App")
        self.window.geometry('810x650')
        
        # UI Elements
        self.title_label = ctk.CTkLabel(
            self.window, 
            text="Disappearing Text Writing App", 
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        self.instruction_label = ctk.CTkLabel(
            self.window, 
            text="Start typing to begin. If you stop for 10 seconds, your work disappears.\n(Work is automatically appended to doc.txt when the timer expires)", 
            text_color='gray70',
            font=("Arial", 16)
        )
        self.instruction_label.pack(pady=5)

        self.timer_label = ctk.CTkLabel(
            self.window, 
            text="10", 
            font=("Arial", 50, "bold"),
            text_color="green"
        )
        self.timer_label.pack(pady=10)

        self.textbox = ctk.CTkTextbox(
            self.window, 
            width=700, 
            height=300, 
            font=("Arial", 20),
            wrap="word"
        )
        self.textbox.pack(padx=50, pady=20, fill="both", expand=True)
        self.textbox.focus()
        self.textbox.bind("<Key>", self.reset_timer)

        # App State
        self.timer = None
        self.remaining_time = 10

    def reset_timer(self, event=None):
        if self.timer:
            self.window.after_cancel(self.timer)
        
        self.remaining_time = 10
        self.update_ui_state()
        self.timer = self.window.after(1000, self.update_timer)

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time > 0:
            self.update_ui_state()
            self.timer = self.window.after(1000, self.update_timer)
        else:
            self.save_and_clear()

    def update_ui_state(self):
        self.timer_label.configure(text=str(self.remaining_time))
        
        if self.remaining_time >= 7:
            color = "green"
        elif self.remaining_time >= 4:
            color = "blue"
        else:
            color = "red"
        
        self.timer_label.configure(text_color=color)
        self.textbox.configure(text_color=color)

    def save_and_clear(self):
        user_text = self.textbox.get("1.0", "end-1c").strip()
        if user_text:
            self.save_text(user_text)
        
        self.textbox.delete("1.0", "end")
        self.remaining_time = 10
        self.update_ui_state()
        if self.timer:
            self.window.after_cancel(self.timer)
            self.timer = None

    def save_text(self, text):
        file_path = 'doc.txt'
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, 'a') as f:
            if file_exists and os.path.getsize(file_path) > 0:
                f.write('\n\n' + '-'*20 + '\n\n')
            f.write(text)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = TextApp()
    app.run()
