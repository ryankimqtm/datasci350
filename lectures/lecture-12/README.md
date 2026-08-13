# Lecture 12 - Local Language Models

A language model is a file. Today you download one onto your laptop, run it from the terminal, and turn it into your own chatbot.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-local-models.html)

## What we cover

- How a model reads text: tokens rather than words, and why "ChatGPT" arrives as three of them
- Embeddings, where each token becomes a list of numbers and meaning turns into geometry
- Why a trained model is just a pile of learned numbers, and why that means it fits on a disk
- Ollama: install it, pull a model, chat with it, and inspect it
- Quantisation, and why a "1 billion parameter" model is never 1 GB
- How much RAM you need, and what to do when your laptop cannot spare it
- Hugging Face, for the models the Ollama library does not carry
- System prompts, PTCF, and temperature
- The `Modelfile`, which turns settings and a personality into a file you can commit
- Few-shot examples with `MESSAGE`, and the difference between asking and constraining
- Structured output with `--format json`
- Hallucination and bias, demonstrated on a model you can open

## The idea the lecture is built on

Training a model takes months on thousands of GPUs. Once it finishes, the result is a few billion numbers, and numbers can be written to disk.

So a trained language model is a file, not a service you rent. The one we use in class holds 1.2 billion numbers in 1.3 GB. If you can download a film, you can download a language model.

Everything else follows from that. You can inspect the file, pin its version, run it with the wifi off, and keep it after the company that made it has moved on.

## The commands worth memorising

| Command | What it does |
| ------- | ------------ |
| `ollama pull <model>` | Download a model |
| `ollama run <model>` | Start a conversation |
| `ollama ls` | List what you have downloaded |
| `ollama ps` | Show what is loaded in memory now |
| `ollama show <model>` | Print a model's details |
| `ollama rm <model>` | Delete it from disk |

Inside the chat, `/set parameter temperature 0` changes a setting, `/clear` forgets the conversation so far, and `/bye` leaves.

`ollama show llama3.2:1b` prints the first half of the lecture back at you: the parameter count, the context length in tokens, the embedding length, and the quantisation. Every one of those is a concept from the slides, printed from your own terminal.

## Reproducibility

`/clear` matters more than it looks. Inside one session the model can see its own previous answers, so asking the same question twice is not the same experiment twice. Set the temperature to 0 and clear the context before you compare anything.

A `Modelfile` records the model, the settings, and the system prompt in about fourteen lines of text. Commit it to Git and your assistant behaves the same next week and on someone else's machine. This is the argument we made for Quarto in lecture 10, applied to a chatbot.

The same reasoning applies to research. A closed model can change or vanish without warning, so work that relied on it cannot be repeated. Open weights let you pin the exact model, the way you already pin a package version ([Spirling, 2023](https://www.nature.com/articles/d41586-023-01295-4); [Palmer, Smith and Spirling, 2024](https://www.nature.com/articles/s43588-023-00585-1)).

## What a system prompt can and cannot do

Jeeves, the sarcastic butler we build in class, holds his tone perfectly for a whole conversation. Asked to follow a rule, the same system prompt does much worse: told to admit when he cannot do something, he invented a full weather forecast for Atlanta instead.

A system prompt sets a tone reliably. It sets a rule only approximately. `--format json` is different, because it constrains what the model is allowed to produce rather than asking politely. Even then, only the shape is guaranteed. The JSON we get in class is valid, and it still claims Paris has 21 million people.

## Practice

Install Ollama before class from <https://ollama.com/download>, then run `ollama pull llama3.2:1b`. The download is about 1.3 GB and it is slow on the university wifi.

The second exercise asks you to build Hobbes, a relentlessly cheerful butler who is the opposite of Jeeves:

1. Create a file called `Hobbes`, with no extension.
2. Write a `SYSTEM` block using all four parts of PTCF.
3. Give Hobbes three rules: three sentences at most, address the user as "my dear", and admit plainly when he cannot do something.
4. Run `ollama create hobbes -f Hobbes`.
5. Ask him to fix a Python bug, to look up tomorrow's weather, and what you asked him yesterday.
6. Write down which of your three rules he broke.

Bring your `Hobbes` file, one transcript where the model obeyed you, and one where it did not. The second is the more interesting half, and there will be one. Solutions are in the appendix slides.

## Before the next class

1. Install Ollama and run `ollama pull llama3.2:1b`.
2. Complete both exercises.
3. Check that `quarto render` works on the laptop you will bring.
4. Push something small to GitHub from that same laptop.
5. Charge the laptop and pack the charger.

Next class is Quiz 02: Literate Programming, worth 6%. It covers lectures 10 and 11: Quarto, Markdown, citations, `freeze`, and publishing a site. Open notes, open slides, open web, AI allowed, and you must say which AI you used.

After the quiz, lecture 14 keeps the model and changes the interface. Ollama has been running a small web server on `localhost:11434` all along, and Python can talk to it. We add coding agents in your terminal and hosted models through an API key. Keep Ollama installed.

## If something goes wrong

If `ollama` is not found, close the terminal and open a new one so it picks up the new `PATH`.

If answers arrive one word every few seconds, the model does not fit comfortably in RAM. Close your browser, then try `gemma3:1b` instead.

If your laptop cannot run any small model, tell me in class. Use [Google AI Studio](https://aistudio.google.com/) for the exercises in the meantime, and we will find you a lab machine.

Appendix 03 on the slides lists the rest of the common errors.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
