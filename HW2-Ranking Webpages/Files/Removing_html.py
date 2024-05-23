import os
from boilerpy3 import extractors

def process_html_with_boilerpy(html_content):
    try:
        extractor = extractors.ArticleExtractor()
        text = extractor.get_content(html_content)
        return text
    except Exception as e:
        print(f"Error processing HTML with BoilerPy3: {e}")
        return None

def main():
    input_directory = 'html_files'
    output_directory = 'processed_html_files'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.html'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.html")

            with open(input_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            processed_text = process_html_with_boilerpy(html_content)
            if processed_text:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(processed_text)

if __name__ == "__main__":
    main()