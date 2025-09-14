import json
import os
import random
import tkinter as tk
from tkinter import scrolledtext, messagebox

DATA_FILE = "ai_knowledge.json"

def load_knowledge():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_knowledge(knowledge):
    with open(DATA_FILE, "w") as f:
        json.dump(knowledge, f, indent=4)

def normalize(text):
    return text.strip().lower()

def parse_command(text):
    text = text.strip()
    if text.lower().startswith("teach:"):
        try:
            _, rest = text.split(":", 1)
            question, answer = rest.split("=", 1)
            return "teach", question.strip(), answer.strip()
        except ValueError:
            return "error", None, None
    elif text.lower().startswith("update:"):
        try:
            _, rest = text.split(":", 1)
            question, answer = rest.split("=", 1)
            return "update", question.strip(), answer.strip()
        except ValueError:
            return "error", None, None
    else:
        return "question", text, None

class MentorAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MentorAI - Learning AI")

        self.knowledge = load_knowledge()

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20)
        self.chat_area.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.grid(row=1, column=0, padx=10, pady=5)
        self.entry.bind("<Return>", self.process_input)

        self.send_button = tk.Button(root, text="Send", command=self.process_input)
        self.send_button.grid(row=1, column=1, padx=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_knowledge)
        self.reset_button.grid(row=1, column=2, padx=5)

        self.print_intro()

    def print_intro(self):
        intro_text = (
            "You can chat with MentorAI.\n"
            "If I don't know the answer, teach me using:\n"
            "  teach: question = answer\n"
            "To update an existing answer:\n"
            "  update: question = new_answer\n"
            "Click Reset to clear all learned data.\n"
            "Close the window to exit.\n\n"
        )
        self.append_chat("MentorAI", intro_text)

    def append_chat(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def reset_knowledge(self):
        if messagebox.askyesno("Confirmation", "All learned data will be deleted. Are you sure?"):
            self.knowledge = {}
            save_knowledge(self.knowledge)
            self.append_chat("MentorAI", "Knowledge base has been reset.")

    def process_input(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return

        self.append_chat("You", user_text)
        self.entry.delete(0, tk.END)

        cmd, q, a = parse_command(user_text)

        if cmd == "question":
            norm_q = normalize(q)
            if norm_q in self.knowledge:
                answer = random.choice(self.knowledge[norm_q])
                self.append_chat("MentorAI", answer)
            else:
                self.append_chat("MentorAI", "I don't know the answer. You can teach me using 'teach: question = answer'.")
        elif cmd == "teach":
            norm_q = normalize(q)
            if norm_q in self.knowledge:
                if a not in self.knowledge[norm_q]:
                    self.knowledge[norm_q].append(a)
                    self.append_chat("MentorAI", f"Learned a new answer for '{norm_q}'.")
                else:
                    self.append_chat("MentorAI", "I already know this answer.")
            else:
                self.knowledge[norm_q] = [a]
                self.append_chat("MentorAI", "Learned a new question and answer.")
            save_knowledge(self.knowledge)
        elif cmd == "update":
            norm_q = normalize(q)
            if norm_q in self.knowledge:
                self.knowledge[norm_q] = [a]
                save_knowledge(self.knowledge)
                self.append_chat("MentorAI", f"Updated the answer for '{norm_q}'.")
            else:
                self.append_chat("MentorAI", "I don't know this question yet. Use 'teach:' to add it first.")
        else:
            self.append_chat("MentorAI", "Invalid command format. Use 'teach:' or 'update:'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MentorAIApp(root)
    root.mainloop()
