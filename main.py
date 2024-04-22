# main.py

# Import necessary modules
from src.components.data_scrapping import WebScraper
from src.components.data_cleaner import TextCleaner
from src.components.data_analysis import SentimentAnalyzer

def main():
    
    data_folder = 'artifacts/extracted_text'
    stopwords_folder = 'artifacts/StopWords'
    cleaned_folder = 'artifacts/stopword_removed'
    stopwords_file_path = "artifacts/stopwords.txt"
    
    positive_words_file = "artifacts/MasterDictionary/positive-words.txt"
    negative_words_file = "artifacts/MasterDictionary//negative-words.txt"
    stopwords_removed_folder_path = "artifacts/stopword_removed"
    
    # Instantiate WebScraper with the path to the Excel file and the output folder
    scraper = WebScraper("artifacts/Input.xlsx", "artifacts/extracted_text")
    
    # Call the scrape_and_save method to perform scraping and saving
    scraper.scrape_and_save()
    
    cleaner = TextCleaner(data_folder, stopwords_folder, cleaned_folder, stopwords_file_path)
    
    cleaner.clean_files()
    
    analyzer = SentimentAnalyzer(positive_words_file, negative_words_file, stopwords_file_path, stopwords_removed_folder_path)
    
    analyzer.analyze_text_files()
    

if __name__ == "__main__":
    main()
