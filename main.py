import tkinter as tk
import time
import lorem



class TypingSpeedTest:
    def __init__(self, root):
        self.Tk = root
        self.Tk.title("Typing Speed Test")

        self.sample_text = ""

        self.start_time = None
        self.random()
        self.end_time = None

        self.create_widgets()
    def random(self):
        paragraph = lorem.paragraph()
        self.sample_text=paragraph
    def create_widgets(self):
        self.text_label = tk.Label(self.Tk, text="Type the following text as quickly and accurately as you can: \n when click start  text change")
        self.text_label.pack(pady=10)

        self.sample_text_label = tk.Label(self.Tk, text=self.sample_text, wraplength=400, justify='left')
        self.sample_text_label.pack(pady=10)

        self.entry = tk.Text(self.Tk, height=10, width=50)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.Tk, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)

        self.submit_button = tk.Button(self.Tk, text="Submit", command=self.end_test)
        self.submit_button.pack(pady=5)
        self.submit_button.config(state=tk.DISABLED)

        self.result_label = tk.Label(self.Tk, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        self.random()
        self.sample_text_label.config(text=self.sample_text)
        self.entry.delete(1.0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)

    def end_test(self):
        self.end_time = time.time()
        input_text = self.entry.get(1.0, tk.END).strip()
        Question=self.sample_text.split()
        Answer=input_text.split()
        print(Answer)
        word_count=0
        if len(Question)>len(Answer):
            min=Answer
        else:
            min=Question
        for i in range(0,len(min)):
            if Question[i] == Answer[i]:
                word_count+=1
        time_taken = self.end_time - self.start_time
        wpm = (word_count / time_taken) * 60

        self.result_label.config(text=f"Words per minute: {wpm:.2f} WPM \n input: {input_text}")

        self.start_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)



if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()