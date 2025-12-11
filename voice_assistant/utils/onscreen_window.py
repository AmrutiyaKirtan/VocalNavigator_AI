import tkinter as tk

class OnScreenAssistant:
    def __init__(self, command_callback=None):
        self.root = tk.Tk()
        self.root.title("Voice Assistant")
        self.root.attributes("-topmost", True)
        self.root.geometry("400x250+50+50")
        self.root.resizable(False, False)
        
        # Output text area
        self.text_widget = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12), height=10)
        self.text_widget.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.text_widget.insert(tk.END, "[Assistant Ready]\n")
        self.text_widget.config(state=tk.DISABLED)
        
        # Command input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Command input field
        self.command_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.command_entry.bind("<Return>", self.on_command_enter)
        
        # Submit button
        submit_btn = tk.Button(input_frame, text="Submit", command=self.on_command_submit)
        submit_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        self.command_callback = command_callback

    def update_display(self, transcript, gemini_response=None):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, f"You said: {transcript}\n")
        if gemini_response:
            self.text_widget.insert(tk.END, f"Gemini: {gemini_response}\n")
        self.text_widget.config(state=tk.DISABLED)
        self.root.update()

    def on_command_enter(self, event):
        self.on_command_submit()

    def on_command_submit(self):
        command = self.command_entry.get().strip()
        if command and self.command_callback:
            self.command_entry.delete(0, tk.END)
            self.command_callback(command)

    def run(self):
        self.root.mainloop()

# For testing
if __name__ == "__main__":
    def test_callback(cmd):
        print(f"Command received: {cmd}")
    
    win = OnScreenAssistant(test_callback)
    win.run()
    win.run() 