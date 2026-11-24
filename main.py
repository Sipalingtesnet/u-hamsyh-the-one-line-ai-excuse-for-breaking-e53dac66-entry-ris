import os

LINE = "I fixed the outage, then fixed my fix, then fixed that fix. Production is now a museum of my good intentions."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)