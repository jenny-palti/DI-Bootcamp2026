# Progress Log

This is the running log kept by the Student Progress Coach for this repo. Each daily review appends a dated entry — newest entries are prepended at the top, so the most recent review is always what you see first when you open this file.

## 2026-08-19 (later same day)

**Since yesterday:** 1 commit, 1 file — the `random` module, `random.randint()`, conditional comparisons

**What I saw:** You went right on with `Week1/Day4/exercisexp.py` after this morning's review, adding Exercise 4 ("Random"): `compare_number(my_number)` calls `random.randint(1, 100)` and uses an `if`/`else` to compare it against the argument, printing a success message on a match and an f-string breakdown of both numbers on a miss. This is exactly the follow-through today's earlier entry nudged toward ("worth a quick look at whether Day4 has further exercises") — you didn't stall on `describe_city`, you kept going in the same file. The function correctly takes `my_number` as a parameter rather than hardcoding the comparison inline, consistent with the parameter-based functions you'd already built earlier in the file.

**Recommendations:**
- `compare_number(50)` is only ever called with one fixed value, so you'll almost always land on the "Fail" branch by chance (1/100 odds of a hit). Try calling it a few times with different numbers, or loop it a handful of times, so you actually see the "Success!" branch execute at least once.
- The file is growing into a full set of Day4 exercises in one script — once you're done, it'd be worth splitting exercises into separate files or adding clear `print("--- Exercise N ---")` separators, since right now the output of all four exercises runs together when you execute the file.

**Streak:** 1 day

## 2026-08-19

**Since yesterday:** 1 commit, 1 file — function parameters, default arguments

**What I saw:** In `Week1/Day4/exercisexp.py` you finished the `describe_city(city, country="Unknown")` exercise, giving `country` a default value and then calling the function four times — three times with an explicit country ("Tokyo"/"Japan", "Paris"/"France", "Jerusalem"/"Israel") and once with just `"Atlantis"` to trigger the default. That last call is exactly the point of the exercise: it actually exercises the default-argument behavior instead of just defining it and never using it, which is easy to skip. This builds directly on `display_message()` and `favorite_book(title)` earlier in the same file, so you're stacking no-argument → required-argument → default-argument functions in order.

**Recommendations:**
- Add an f-string print for the "Atlantis" case too (or a comment showing the output) so it's visible at a glance that the default kicked in, rather than having to run the file to check.
- This file only has one exercise left blank before it (`display_message`/`favorite_book`/`describe_city` are now all done) — worth a quick look at whether Day4 has further exercises after this one so momentum doesn't stall here.

**Streak:** 1 day
