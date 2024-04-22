import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.exception import CustomException
from src.logger import logging
import sys
import os

class WebScraper:
    def __init__(self, excel_file, extracted_folder_path):
        try:
            self.df = pd.read_excel(excel_file) # reading excel file
            self.extracted_folder_path = extracted_folder_path
            logging.info("Excel file loaded successfully.")
        except Exception as e:
            raise CustomException(e,sys)
            
        
    def scrape_and_save(self):
        
        """
            This function takes excel file iterate through it, takes url from "url" column , 
            extracts the data and saves it into individual files name according to "url_id" column
        """
        try:
            
            if self.df is None:
                logging.error("WebScraper was not initialized properly. Exiting.")
                return
            
            if not os.path.exists(self.extracted_folder_path):
                os.makedirs(self.extracted_folder_path)
                logging.info("Created extracted_text folder")
            
            # Iterate through each URL
            for index, row in self.df.iterrows():
                url = row['URL']
                name = row['URL_ID']
                # Send request to the URL
                response = requests.get(url)
                if response.status_code == 200:
                    # Parse HTML content
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    #Find elements with class entry-title
                    title = soup.find('h1', class_='entry-title')
                    # Find elements with class td-post-content
                    td_post_content_elements = soup.find_all(class_='td-post-content')
                    
                    # Extract text from each element
                    extracted_text = ""
                    if title:
                        title_text = title.text.strip()
                        extracted_text += title_text + '\n'
                    for element in td_post_content_elements:
                        extracted_text += element.get_text(separator='\n') + '\n'
                    
                    output_file = f"artifacts/extracted_text/{name}.txt"
                    
                    with open(output_file, 'w' ,encoding='utf-8') as f:
                        f.write(extracted_text)    
                else:
                    logging.info(f"Failed to fetch data from {url} : {name}")
                
            logging.info(f"Data Scraping Done.....")
        
        except Exception as e:
            raise CustomException(e,sys)
        
# def main():
#     scraper = WebScraper("artifacts/Input.xlsx", "artifacts/extracted_text")
#     scraper.scrape_and_save()
# Usage:
# if __name__ == "__main__":
#     pass