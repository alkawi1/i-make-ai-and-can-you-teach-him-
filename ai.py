import json
import os

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

def main():
    print("You can ask me questions in English.")
    print("If I don't know the answer, teach me with:")
    print("  teach: question = answer")
    print("Or update existing answer with:")
    print("  update: question = new_answer")
    print("Type 'reset' to clear all learned data.")
    print("Type 'exit' to quit.\n")

    knowledge = load_knowledge()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "reset":
            knowledge = {}
            save_knowledge(knowledge)
            print("AI knowledge has been reset.")
            continue

        cmd, q, a = parse_command(user_input)

        if cmd == "question":
            norm_q = normalize(q)
            if norm_q in knowledge:
                import random
                print("AI:", random.choice(knowledge[norm_q]))
            else:
                print("AI: I don't know the answer. You can teach me using 'teach: question = answer'")
        elif cmd == "teach":
            norm_q = normalize(q)
            if norm_q in knowledge:
                if a not in knowledge[norm_q]:
                    knowledge[norm_q].append(a)
                    print(f"AI: Learned new answer for '{norm_q}'.")
                else:
                    print("AI: I already know this answer.")
            else:
                knowledge[norm_q] = [a]
                print(f"AI: Learned new question and answer.")
            save_knowledge(knowledge)
        elif cmd == "update":
            norm_q = normalize(q)
            if norm_q in knowledge:
                knowledge[norm_q] = [a]
                save_knowledge(knowledge)
                print(f"AI: Updated answer for '{norm_q}'.")
            else:
                print("AI: I don't know this question yet. Use 'teach:' to add it first.")
        else:
            print("AI: Invalid command format. Use 'teach:' or 'update:'")

if __name__ == "__main__":
    main()
