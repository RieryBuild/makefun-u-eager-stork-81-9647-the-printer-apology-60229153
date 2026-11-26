import os

LINE = "Sorry I printed Dave's expenses to the shared tray. 42 colleagues now know about the $800 lunch. I kept the receipt."

# Gate guards: the entry must be 1-120 characters, a single line, no padding.
assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must not start or end with whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
