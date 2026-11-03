# Daily Challenge: Pagination - Week 2, Day 2

import math


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        page_num = int(page_num)
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} does not exist. Choose 1 to {self.total_pages}.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


# Step 6: Test the code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())    # ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())    # ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())    # ['y', 'z']

print(str(p.first_page()))      # a b c d, one per line

# Bonus: method chaining
print(p.first_page().next_page().next_page().next_page().get_visible_items())  # ['m', 'n', 'o', 'p']

# go_to_page with a page that doesn't exist raises a ValueError
for bad_page in [10, 0]:
    try:
        p.go_to_page(bad_page)
    except ValueError as error:
        print("ValueError:", error)
