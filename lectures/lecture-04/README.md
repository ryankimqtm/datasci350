# Lecture 04 - More About the Command Line

Everything you can do to files, text, and repetitive work without ever touching a mouse.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-04/04-more-command-line.html)

## What we cover

- Managing files: `mkdir`, `touch`, `rm`, `rmdir`, `cp`, and `mv`
- Acting on many files at once with wildcards (`*`, `?`) and braces (`{}`)
- Locating files with `find`, by name, size, type, or depth
- Reading text with `cat`, `head`, `tail`, and `wc`
- Searching with `grep` and editing with `sed`
- `nano`, for quick edits inside the terminal
- Redirects (`>`, `>>`), pipes (`|`), `for` loops, and your first shell script

## Files in this folder

- `sonnets.txt` holds Shakespeare's sonnets, used for all the text examples. Download it from this folder, or with the `curl` command shown on the slides.
- `create_project.sh` is the example script from the scripting section.
- `meals/` is a small folder used to demonstrate `grep -r`.

## Practice

Two exercises. The first builds a small project structure, then renames, copies, and deletes parts of it. The second works on `sonnets.txt`, including two harder questions about matching lines that start with a given word. Solutions are in the appendix slides at the end.

Be careful with `rm -r`, `rm -rf`, and `sed -i`. All three change or delete things immediately, with no undo and no Trash. Read the path before you press Enter.

## Before the next class

1. Work through both exercises.
2. Install Git. Download it from [git-scm.com](https://git-scm.com/downloads).
3. Create a GitHub account if you have not already.

Next time we leave the shell and start on version control: project structure, Git, and GitHub. You will use them every week for the rest of the course.

Many thanks to [Davi Moreira](https://davi-moreira.github.io) and [Simon Munzert](https://github.com/intro-to-data-science-21/lectures/tree/main) for sharing their materials, which I used as a basis for this lecture.
