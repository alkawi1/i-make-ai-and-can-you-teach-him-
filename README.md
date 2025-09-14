# Simple Teach-able AI in Python

This is a basic command-line AI program written in Python.  
You can ask questions in English, and the AI will try to answer them based on what it has learned from you.

## Features

- Ask any question in English.
- If the AI doesn't know the answer, it will ask you to teach it.
- Teach the AI using commands.
- Update answers if needed.
- Reset all learned data anytime.

## How to use

1. Run the program:

```bash
python ai_teachable.py

    Ask a question by typing it and pressing Enter.

    If the AI doesn't know the answer, teach it using:

teach: question = answer

    To update an existing answer, use:

update: question = new_answer

    To reset all learned data, type:

reset

    To exit the program, type:

exit

Example

You: What is AI?
AI: I don't know the answer. You can teach me using 'teach: question = answer'
You: teach: What is AI? = AI means Artificial Intelligence.
AI: Learned new question and answer.
You: What is AI?
AI: AI means Artificial Intelligence.

Feel free to modify and improve the program!

