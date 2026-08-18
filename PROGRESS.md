# Progress Log

This is the running log kept by the Student Progress Coach for this repo. Each daily review appends a dated entry — newest entries are prepended at the top, so the most recent review is always what you see first when you open this file.

## 2026-08-19

**Since yesterday:** 1 commit, 1 file — function parameters, default arguments

**What I saw:** In `Week1/Day4/exercisexp.py` you finished the `describe_city(city, country="Unknown")` exercise, giving `country` a default value and then calling the function four times — three times with an explicit country ("Tokyo"/"Japan", "Paris"/"France", "Jerusalem"/"Israel") and once with just `"Atlantis"` to trigger the default. That last call is exactly the point of the exercise: it actually exercises the default-argument behavior instead of just defining it and never using it, which is easy to skip. This builds directly on `display_message()` and `favorite_book(title)` earlier in the same file, so you're stacking no-argument → required-argument → default-argument functions in order.

**Recommendations:**
- Add an f-string print for the "Atlantis" case too (or a comment showing the output) so it's visible at a glance that the default kicked in, rather than having to run the file to check.
- This file only has one exercise left blank before it (`display_message`/`favorite_book`/`describe_city` are now all done) — worth a quick look at whether Day4 has further exercises after this one so momentum doesn't stall here.

**Streak:** 1 day
