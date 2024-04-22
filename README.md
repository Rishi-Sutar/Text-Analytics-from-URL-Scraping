# Data Scraper and Analysis Project

## Usage

To run the project, follow these steps:

1. Create a Conda environment with Python version 3.8.0.
2. Activate the Conda environment.
3. Run `pip install -r requirements.txt` to install all required packages.
4. Run `python main.py` to execute the program.

This project is designed to scrape data from specified URLs, clean the extracted text, and perform data analysis on the cleaned text files. The program is divided into three modules located in `src/components`:

1. **data_scraper.py**: This module is responsible for scraping data from an Excel file, iterating through the URLs listed in a column, and extracting data from each URL. The extracted data is stored in the `artifacts/extracted_text` folder in text format. Each file is named according to the `url_id` column in the Excel file.

2. **data_cleaner.py**: After data extraction, the `data_cleaner.py` module reads each file from the `artifacts/extracted_text` folder, identifies stopwords, and stores them in `artifacts/stopwords.txt`. Then, it removes the stopwords from each file and stores the cleaned text files in the `artifacts/removed_stopwords` folder.

3. **data_analysis.py**: The `data_analysis.py` module analyzes each file in the `artifacts/removed_stopwords` folder. It calculates various metrics such as Positive Score, Negative Score, Polarity Score, Subjectivity Score, Average Sentence Length, Percentage of Complex Words, Fog Index, Average Number of Words Per Sentence, Complex Word Count, Word Count, Syllable Count, and Personal Pronouns Count. The output of this analysis is stored in an Excel file against their corresponding file names, which are derived from the `url_id` column in the Excel file.
