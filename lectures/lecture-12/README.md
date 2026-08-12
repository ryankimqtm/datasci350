# Lecture 12 - AI and Prompt Engineering

What a language model is actually doing when it answers you, and how to ask so that the answer is useful.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-ai-programming.html)

## What we cover

- How models read text: tokens rather than words, and why "ChatGPT" costs three of them
- Context windows, and what input and output tokens actually cost
- Embeddings, where words become points in space and meaning turns into geometry
- PTCF: Persona, Task, Context, Format
- Temperature, top-p, and top-k, and why you set temperature to 0 before debugging anything
- System prompts, the instructions you never see but always read the effects of
- Zero-shot, one-shot, and few-shot prompting, including when examples make things worse
- Chain-of-thought, and the phrase that triggers it
- Agents, the ReAct loop, and prompt injection
- Hallucination, bias, and jagged intelligence

## The framework, in four questions

Persona: who is answering? Task: what should they do? Context: what do they need to know? Format: what should come back?

The opening example makes the case on its own. "Analyse the sentiment of this headline" returns a thoughtful paragraph about mixed signals. "Classify this headline as BULLISH, BEARISH, or NEUTRAL. Output only one word" returns BULLISH. Same model, same headline, and only one of those fits in a column of a dataframe.

## Numbers worth remembering

Adding "Let's think step by step" moved GSM8K accuracy from 17.9% to 56.9% (Wei et al., 2022). On the easier benchmarks in the same paper it gained under two points. Chain-of-thought helps where the reasoning is the difficulty, and does almost nothing elsewhere.

Dell'Acqua et al. (2023) gave 758 consultants access to GPT-4 across 18 realistic tasks. On tasks inside the model's "jagged frontier", quality rose by about 40%. On tasks outside it, the consultants using AI scored 19 percentage points worse than the ones working without it. The tool made capable people worse at parts of their own job.

Output tokens cost five to six times more than input tokens on every model in the lecture's price table. "Be concise" is a budget decision as well as a style one.

## Practice

Open [Google AI Studio](https://aistudio.google.com/), which is free and shows you the temperature slider.

1. Paste this prompt: "Tell me about machine learning in healthcare".
2. Set the temperature to 0. Run it twice. Compare the two answers.
3. Set the temperature to 0.9. Run it twice more. Compare again.
4. Rewrite the prompt using all four parts of PTCF.
5. Run your version at temperature 0.
6. Count how many of your format instructions the model followed.

At temperature 0 the two answers should be almost identical. At 0.9 they will not be, and neither one is more correct than the other. If the model ignored an instruction in step 6, it was probably ambiguous rather than disobeyed.

Bring your rewritten prompt to class.

## Before the next class

1. Complete the exercise above.
2. Check that `quarto render` works on the laptop you will bring.
3. Push something small to GitHub from that same laptop.
4. Charge the laptop and pack the charger.

Next class is Quiz 02: Literate Programming, worth 6%. It covers lectures 10 and 11: Quarto, Markdown, citations, `freeze`, and building a site. Open notes, open slides, open web, AI allowed, and you must say which AI you used.

After the quiz, lecture 14 takes this material to the keyboard. You install a coding agent in your terminal, call a model from your own Python script, and run one on your own laptop with the internet switched off.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
