# Functions 2: Shown Isn't Given Back

**Time:** 60 minutes

**Files in this repo**

| File | Used in |
|---|---|
| `pizza_order.py` | Parts 1–3 |
| `add_tools.py` | Part 2C |
| `dinner_with_friends.py` (empty) | Part 4 |

## How this activity works

You'll predict what code does, run it, figure out why, change it, and then build something of your own. Wrong predictions are expected. They show you exactly which idea to look at next.

### When you're stuck

Raise your hand when either of these is true:

- You've been stuck on one step for **5 minutes**, or
- You've tried **two different things** and neither worked.

Look for the 🙋 symbol in this guide. It marks the places where fellows most often get stuck, and asking for help there is the right move.

**When you ask for help, come with:**

1. The line of code you're stuck on
2. What you predicted
3. What actually happened
4. What you've tried so far

The ✅ symbol marks a checkpoint where you show an instructor your work before moving on.

---

## The big ideas (come back to this table)

| # | Idea | Try it (in a file, with `print`) |
|---|---|---|
| 1 | Defining a function stores its steps under a name. Nothing inside runs until the function is called. | `def add(a, b):` / `    return a + b`, then `print(add(2, 3))` |
| 2 | A call hands its values to the function by position, not by name, and runs the whole body again each time. | `def minus(a, b):` / `    return a - b`, then `b = 10`, `a = 3`, `print(minus(b, a))` |
| 3 | A call is replaced by the value the function gives back, so a call can go anywhere a value can. | `print(add(2, 3) * 10)`, `print(add(2, 3) > 4)`, `print(add(add(1, 2), 4))` |
| 4 | Showing a value on screen and giving it back are separate acts. | `def show_add(a, b):` / `    print(a + b)`, then `total = show_add(2, 3)` and `print(total)` |
| 5 | A function that gives nothing back hands back `None` ("nothing came back"). Most operations can't use it. | `print(show_add(2, 3) + 1)` |
| 6 | The inner parts of a line run first, so output shows up in the order things run, not where the value is used. | `print("Sum:", show_add(2, 3))` |
| 7 | A big job can be split into small functions that hand their results to each other. One function can call another. | `def add_three(a, b, c):` / `    return add(add(a, b), c)`, then `print(add_three(1, 2, 3))` |

## Habits for today

**Coding habit:** Inside a function, **return** the answer by default. Use **print** only in a function whose whole job is to show something. Switch only when you get a **runtime error** (a crash that mentions `NoneType`) or a **logic error** (it runs, but `None` shows up where a number should be). One function, one job: if a function does two steps, split out a helper.

**Working habit: Debug with a plan, not random changes.**

- Before you change anything, say what you expected, what actually happened, and which line you think caused it.
- Change one thing at a time, and predict what the change will do before you run it.
- If two changes in a row didn't do what you predicted, stop editing and trace the values line by line, or ask for help.

---

## Part 1: Predict & Run (10 minutes)

Open `pizza_order.py`. **Don't run it yet.**

1. Fill in the `# Data types of these values:` comment and every `# Prediction:` line.
2. Run `python3 pizza_order.py`.
3. Fill in each `# Actual:` and `# Explanation:` line. Use the big ideas table.

Answer these as comments at the bottom of `pizza_order.py`:

1. What is the data type of `guests`? What data type does `slices_needed(guests)` give back?
2. What does the line `slices_needed(guests)` print? Why?
3. What does `print("Slices:", slices_needed(guests))` print? Why is it different from the line above?
4. What does the last line print? Why are there two lines? Why does `6.0` come first, and why does the sentence say `None`?

**Swap with a partner** and compare answers.

🙋 **Ask for help if:** you and your partner can't agree on why the sentence says `None`.

---

## Part 2: Investigate (10 minutes)

### A) Break down the last line

Fill in this table for `print("Order", pizzas_needed(guests), "pizzas")`, in the order Python works things out.

| Line/Expression | Evaluated Value | Data Type | Shown on screen? |
|---|---|---|---|
| `guests` | | | |
| `slices_needed(guests)` | | | |
| `slices_needed(guests) / 8` | | | |
| `pizzas_needed(guests)` | | | |
| `print("Order", ___, "pizzas")` | | | |

Self-check: the "Shown on screen?" column should account for both lines that printed, in the same order.

🙋 **Ask for help if:** you can't find which row put `6.0` on the screen.

### B) Compare

Why did `print("Slices:", slices_needed(guests))` show a usable number, but `print("Order", pizzas_needed(guests), "pizzas")` showed `None`? Write your answer and name the idea number(s) that explain it.

### C) Run `add_tools.py` (2 minutes)

Run it as a file (`python3 add_tools.py`), not in the REPL. The REPL shows every value automatically, which would hide what we're looking at. Predict the output on paper first.

Then answer:

1. Which line printed the `5` on its own line? Why didn't `add(2, 3)` print anything?
2. Why does `minus(b, a)` give `7` and not `-7`?

✅ **Checkpoint:** Tell an instructor, in one sentence, the difference between showing a value and giving it back.

---

## Part 3: Modify (13 minutes)

Work in `pizza_order.py`.

### 1. Fix the error

Change **one line** in `pizzas_needed` so the last line prints `Order 6.0 pizzas`.

Self-check: run it. The output should now have only two lines, and the last one should read `Order 6.0 pizzas`.

### 2. Variation

Keep your fix. Now change the **helper**: in `slices_needed`, change `return guests * 3` to `print(guests * 3)`. Predict, then run.

Answer as comments:

1. `48` is on the screen, so why did `pizzas_needed` crash?
2. The error message names two lines. Which line is the real cause?

🙋 **Ask for help if:** you're about to change the line the error points to and you can't say why that line is the cause. Use the working habit: say what you expected, what happened, and which line you suspect.

Change the helper back to `return` before Exercise 3.

### 3. Trace

Replace the last line with:

```python
print("Order", pizzas_needed(guests + 8), "pizzas")
```

**Before running**, trace it as comments, one step per line: what `guests + 8` becomes, what `slices_needed` gives back, what `pizzas_needed` gives back, and what the final `print` gets. Then run it and compare.

---

## Part 4: Make (12 minutes)

**Task: dinner_with_friends.** In `dinner_with_friends.py`, work out what each friend pays for a dinner out, using small functions that hand their results to each other.

**Requirements**

1. `subtotal(food, drinks)` **returns** food plus drinks.
2. `add_tax(amount)` **returns** the amount plus 10% tax.
3. `split(total, people)` **returns** each person's share.
4. `dinner_bill(food, drinks, people)` calls all three helpers and **returns** each person's share. It does no math of its own.
5. `show_share(label, share)` **prints** the share, then prints `Pricey night` if the share is over 25 and `Good deal` otherwise.
6. Run it for two dinners by calling `dinner_bill` twice. Never type a computed number into the code.
7. The program must run without crashing.

**Check your output.** Taco night: food 48, drinks 12, 3 people. Birthday dinner: food 90, drinks 30, 4 people.

```
Taco night, each pays: 22.0
Good deal
Birthday dinner, each pays: 33.0
Pricey night
```

Tip: test each helper on its own before you connect them, for example `print(subtotal(48, 12))` should show `60`.

🙋 **Ask for help if:** you see `None` or a `NoneType` error and can't find which function is showing its answer instead of giving it back.

✅ **Checkpoint:** Show an instructor your code and point to the function that does only printing. Explain why every other function returns.

---

## Part 5: Independent check (10 minutes)

Your instructor will hand this out. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

One new tool: `round()`. Change `add_tax` to use NYC's 8.875% sales tax: `amount + amount * 8.875 / 100`. Run `print(split(add_tax(60), 3))`. Then use `round(share, 2)` so the share shows only two decimal places. Should the rounding go in `split` or in `show_share`? Why?
