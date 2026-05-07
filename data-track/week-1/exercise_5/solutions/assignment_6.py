"""Reference solution (in-place over the starter).

The four numbered comments from the starter are preserved below;
solution code sits directly under each, with `# WHY ...:` notes.

Teaches: read / transform / write file pipeline with context managers
that guarantee the file handle is closed even on a crash mid-loop
(Ch9). Same shape every "ingest a file, transform, write back out"
pipeline takes — the assignment in the next chapter is a more
complex variant of this exact pattern.
"""

# 3. Use the with open(...) pattern to read the raw_data.txt file.
# WHY encoding="utf-8": pin the file's text encoding instead of
# falling back to whatever the OS prefers (cp1252 on Windows). For
# city names with diacritics ("São Paulo", "Curaçao") this prevents
# silent corruption when the file moves between machines or the
# script runs in a Docker container with a different default locale.
with open("raw_data.txt", encoding="utf-8") as f:
    raw_lines = f.readlines()

# 4. Loop through the lines and capitalize each city name (e.g., “Amsterdam”).
# 5. Store the cleaned names in a list.
cleaned_names = []
for line in raw_lines:
    # WHY .strip() then .title(): .strip() removes the trailing
    # newline AND any incidental leading/trailing whitespace.
    # .title() capitalises the first letter of every word, so
    # "the hague" becomes "The Hague" — the spec says "capitalize",
    # which for multi-word names means title-case rather than just
    # upper-first.
    cleaned_names.append(line.strip().title())

# 6. Use with open(...) again to write the cleaned names into a new file called processed_data.txt.
# WHY a separate `with open(..., "w")` block (rather than nesting
# inside the read block): keeps the read and write phases distinct.
# The read handle is closed before the write starts, so even if the
# write fails the input file is safely closed and untouched. Mixing
# read + write in one with-block is rarely needed and harder to
# reason about.
with open("processed_data.txt", "w", encoding="utf-8") as f:
    # WHY join + "\n": writelines() does NOT add line separators
    # between items (common gotcha — students assume it does).
    # join puts exactly one newline between names, then we add a
    # trailing newline so the file ends in \n (POSIX convention).
    f.write("\n".join(cleaned_names) + "\n")

print(f"Wrote {len(cleaned_names)} names to processed_data.txt")
# Expected: a new file `processed_data.txt` with:
#   Amsterdam
#   Rotterdam
#   The Hague
#   Utrecht
