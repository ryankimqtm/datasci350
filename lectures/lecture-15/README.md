# Lecture 15 - Retrieval-Augmented Generation and Fine-Tuning

The last lecture of the AI module. Lecture 12 put a model on your laptop, and lecture 14 called one from your own code. This lecture answers the question both left open: how do you make a model answer questions about documents it has never read?

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-15/15-rag-finetuning.html)

## What we cover

- Embeddings for whole passages, not just words, and cosine similarity in one line of numpy
- Getting embeddings from Ollama with `embeddinggemma`, on the server you have been running since lecture 12
- RAG in products you already use: Gemini Notebook, file upload in chat apps, AI answers in search
- The five stages: chunk, embed, store, retrieve, generate, and where each one fails
- Why retrieval beats pasting everything in: the cost arithmetic, and "lost in the middle"
- Chunking, and what a chunking rule silently throws away
- A working pipeline in about 50 lines of plain Python (`demo/rag.py`), read line by line
- Measuring retrieval with gold questions and a hit rate
- Hybrid search, BM25, and rerankers, for the questions embeddings get wrong
- Prompt injection through a poisoned corpus, and three partial defences
- Vector databases and approximate nearest neighbour search, in concept
- Fine-tuning: context versus weights, what training pairs look like, LoRA, and Unsloth
- Distillation, how a large model writes training data for a small one, and the dispute it started
- The ladder: prompt, then RAG, then fine-tune, climbed only when the rung below fails

## The idea the lecture is built on

Retrieval is a filter in front of the context window. Instead of sending a model everything you own and hoping it finds the answer, you send it the three passages most likely to contain one.

That filter is arithmetic, not intelligence. Embed the chunks once, embed the question, take a dot product, sort:

```python
chunk_vectors /= np.linalg.norm(chunk_vectors, axis=1, keepdims=True)
question_vector /= np.linalg.norm(question_vector)
scores = chunk_vectors @ question_vector
top = np.argsort(scores)[::-1][:3]
```

There is no neural network at question time. A matrix multiplication and a sort do the retrieving, and the chat model only writes the final sentence.

## Before class

Warning: the two model downloads total about 2 GB. Do not attempt them on classroom wifi.

1. Install or update Ollama from [ollama.com](https://ollama.com/).
2. Run `ollama pull embeddinggemma`.
3. Run `ollama pull llama3.2:1b`.
4. Run `pip install ollama numpy`.
5. Run `ollama -v` to confirm the version.

If `ollama pull embeddinggemma` fails, your Ollama is too old. Update the application. The older `nomic-embed-text` (274 MB) works as a fallback.

Students who cannot run local models use the OpenRouter variant in Appendix 03, with the key from lecture 14.

## The demo folder

`demo/rag.py` is the whole pipeline in one file. `demo/corpus/` holds eight of this course's own READMEs: the course README, both quiz briefs, lectures 10, 11, 12 and 14, and the tutorials index. The paragraph-chunking rule turns those eight files into 132 chunks.

Run it with a question:

```bash
python rag.py "What does Quiz 02 cover?"
```

The script prints the corpus size, the three retrieved chunks with their scores, and the answer. Printing the chunks is the point. When an answer is wrong, they tell you whether retrieval or generation failed.

## What the evaluation found

Seven gold questions, each with the file that should answer it. Five of seven retrieved the right file in the top three, and the two misses were the useful part.

| Question | Top score | What came back |
| -------- | --------- | -------------- |
| When is Quiz 02? | 0.58 | The lecture 12 README's paragraph about Quiz 02 |
| How much is the final project worth? | 0.38 | The quiz READMEs, saying "worth 6%" about themselves |

Neither question is answerable. No file in the corpus gives a quiz date, and none states the project's weight. The gold answers named files that could not answer them, and running the evaluation is what revealed it.

The quiz-date miss is the more instructive one. It scored higher than any question that succeeded. A confidence threshold would have passed it straight to the model with a chunk that looks perfect and lacks the fact, which is why a high score means the topic matched and never that the answer is present.

## Retrieval repeats, generation does not

Run the script four times and the scores are identical every time. Embedding is arithmetic and never samples. The written answer can still change between runs, so treat the retrieved chunks as the reproducible part of the output and the prose as the part that needs checking.

## Practice

The exercise is on the slides, with notes in Appendix 01 and troubleshooting in Appendix 04.

Students run the pipeline, ask questions the corpus can answer, check each answer against the file it cites, then ask "What is the capital of Nepal?" and watch both stages behave. Retrieval always returns three chunks, because the top three of whatever exists is still three. Only the prompt's escape hatch can decline. Finally they set `TOP_K` to 1 and find which questions break first.

## Rendering

Run `quarto render 15-rag-finetuning.qmd` in this folder. If Quarto cannot find Python, set `QUARTO_PYTHON=~/miniconda3/bin/python3` first.

The deck is self-contained HTML and no code executes at render time, so rendering needs no network and no running Ollama. Every number on the slides, the scores, the hit rate, the chunk count and the sample output, came from real runs against this corpus with `embeddinggemma` and `llama3.2:1b` in August 2026. Re-run `rag.py` before teaching if the corpus files have changed, because the chunk count moves with them.

## Before the next class

1. Finish the exercise.
2. Keep Ollama and both models on the laptop you will bring.

Next class starts the cloud module. Every computer in this course has been yours so far, and next we borrow someone else's.

Quiz 03 covers the AI module and the cloud module.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
