import csv
import os
import sys

SUPPORTED_TRANSLATIONS = ["kjv", "vul"]

if len(sys.argv) != 2:
    print("error: no translation arg was provided")
    sys.exit(1)

translation = sys.argv[1]
if translation not in SUPPORTED_TRANSLATIONS:
    print("error: translation", translation, "not supported")
    sys.exit(1)

base_dir = translation
if not os.path.exists(base_dir):
    os.mkdir(base_dir)

with open(f"{translation}.tsv") as file:
    row_data = csv.reader(file, delimiter="\t")
    for row in row_data:
        if len(row) < 6:
            print('not formatted correctly...', row)
            continue
        book_name = row[0]
        book_path = os.path.join(base_dir, book_name)
        if not os.path.exists(book_path):
            os.mkdir(book_path)
        chapter = row[3]
        chapter_path = os.path.join(book_path, chapter)
        if not os.path.exists(chapter_path):
            os.mkdir(chapter_path)
        verse_number = row[4]
        verse = row[5]
        file_name = os.path.join(chapter_path, f'{verse_number}.html')
        if os.path.exists(file_name):
            continue 
        print(verse, file=open(file_name, 'w'))
