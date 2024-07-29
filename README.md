##Data Scraper and Analysis Project

This project is designed to scrape data from URLs specified in an Excel file, clean the extracted text, and perform analysis on the cleaned data. Below are the instructions to set up and run the project.

#Setup

1. Create Conda Environment: Begin by creating a Conda environment with Python version 3.8.0.

    conda create --name data-analysis python=3.8.0

2. Install Dependencies: Install all required packages by running the following command:

    pip install -r requirements.txt

#Running the Program

Once the environment is set up and dependencies are installed, follow these steps to run the program:

1. Run main.py: Execute the main.py file to run all modules in sequence. This script will scrape data from URLs provided in the Excel file, clean the extracted text, and perform analysis on the cleaned data. 

    python main.py

#Folder Structure

- src/components/: Contains the modules for data scraping, cleaning, and analysis.
- artifacts/extracted_text/: Stores extracted text from URLs.
- artifacts/removed_stopwords/: Stores cleaned text files.
- artifacts/stopwords.txt: Contains the list of stopwords.

#Additional Notes

- Make sure to provide the Excel file with the necessary columns (url_id, URL) in the specified format for proper execution.
- Ensure that the URLs provided in the Excel file are accessible for data scraping.
