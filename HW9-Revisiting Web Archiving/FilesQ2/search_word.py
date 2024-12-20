import os

input_directory = 'html_files'
term_to_search = 'assistant'
total_occurrences = 0

# List to store filenames containing the term and their TF values
matching_files = []

for filename in os.listdir(input_directory):
    if filename.endswith('.html'):
        input_file = os.path.join(input_directory, filename)
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            content_lower = content.lower()
            occurrences = content_lower.count(term_to_search)
            if occurrences > 0:
                # Calculate TF (Term Frequency)
                total_words = len(content_lower.split())
                tf = occurrences / total_words
                matching_files.append((filename, occurrences, tf))
            total_occurrences += occurrences

print(f"Total occurrences of '{term_to_search}' in HTML files: {total_occurrences}")

if matching_files:
    print("\nFiles containing the term 'payment':")
    print("Filename\tOccurrences\tTF")
    for filename, count, tf in matching_files:
        print(f"{filename}\t{count}\t{tf:.4f}")
else:
    print("No files contain the term 'payment'.")
