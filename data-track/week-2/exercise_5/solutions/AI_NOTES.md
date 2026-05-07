# AI Notes — Exercise 5 (reference)

This is a stand-in for the file you write yourself. Two short paragraphs.

## What the LLM helped with

Asked Claude: "How should I avoid the file `io.py` shadowing the stdlib `io` module?" Claude pointed out that any local file named after a stdlib module replaces it for `import` purposes anywhere downstream — Gotcha #5 from the chapter — and suggested `io_layer.py`, `data_io.py`, or moving the I/O functions into a package. I picked `io_layer.py` because it kept the file flat and the name still reads as "the I/O layer of the pipeline".

## What I rejected

Claude also suggested wrapping `read_users` in a try/except that returns an empty list if the file is missing. I rejected this: silently swallowing a `FileNotFoundError` would let `main.py` "succeed" with zero output even when the input wasn't there. The right behaviour is to crash loudly so the operator sees the missing file. Defensive code that hides real failures is one of the silent-failure traps Week 2 spent chapters teaching us to avoid.

(Your version doesn't need to be polished prose. Two short paragraphs is fine. The point is the *habit* of evaluating LLM output, not collecting suggestions wholesale.)
