import pandas as pd


alice = r"C:\Users\Simrun Sharma\Desktop\NLP\Final_Project\all_chapterized_books\11-chapters\chapters_10_to_12.txt"


with open(alice, "r", encoding="utf-8") as f:
    content = f.read()

print(content[:500])
