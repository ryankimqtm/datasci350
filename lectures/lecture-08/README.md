# Lecture 08 - Review Session

Everything from Lectures 01 to 07, in six rounds, with a keyboard in front of you. This is preparation for Quiz 01.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-08/08-review.html)

## How the class works

Each round has a few minutes of revision, then an exercise you type yourself, then we check the answers together. You will be working for about half the class, so keep a terminal open beside the slides.

| Round | Topic | Lectures |
|:--|:--|:--|
| 1 | How computers store things | 01-02 |
| 2 | The shell | 03 |
| 3 | Files, wildcards, and text | 04 |
| 4 | Git on your machine | 05, 07 |
| 5 | GitHub and collaboration | 06, 07 |
| 6 | Checklist | all |

Everything you type goes into one throwaway folder, `~/ds350-review`, which we delete together at the end. Nothing you do in class can touch your real work.

Solutions to all six exercises are in the appendix slides, each with a button to jump there and back.

## Quiz 01

Next class, worth 6%.

You fork a repository, clone your own copy, work through a list of shell and Git tasks, record every command you run in `commands.txt`, push your work, and submit the link to your fork on Canvas.

Open notes, open slides, open web, AI allowed. Say which AI you used.

## Do this before the quiz

1. Check that Git knows who you are: `git config --list` should show your name and email.
2. Push something small to GitHub from the laptop you will bring. Any repository will do.
3. If that push works today, it will work in the quiz. If it does not, fix it now rather than during the quiz.
4. Charge your laptop and pack the charger.

Installing the GitHub CLI is worth it but not required. `gh auth login` handles sign-in in one step; a plain `git push` over HTTPS works too. Copy the install command from [cli.github.com](https://cli.github.com/) rather than typing it.

## The mistakes that actually cost marks

None of these is about knowing Git:

- Cloning the repository instead of forking it first, so the push is rejected
- Committing everything and never pushing
- Leaving `commands.txt` empty
- Submitting a link to my repository rather than to your own fork
- Working for an hour in the wrong directory

Running `git status` and `pwd` often prevents nearly all of them.
