import os
from nltk.tokenize import word_tokenize # type: ignore
from src.exception import CustomException
from src.logger import logging
import sys
import os

class TextCleaner:
    def __init__(self, data_folder, stopwords_folder, cleaned_folder, stopwords_file_path):
        self.data_folder = data_folder
        self.stopwords_folder = stopwords_folder
        self.cleaned_folder = cleaned_folder
        self.stopwords_file_path = stopwords_file_path
        
        try:
            
            # Check if the cleaned folder exists, if not, create it
            if not os.path.exists(self.cleaned_folder):
                os.makedirs(self.cleaned_folder)

            # Read custom stopwords from files in stopwords folder
            for filename in os.listdir(self.stopwords_folder):
                if filename.endswith('.txt'):
                    with open(os.path.join(self.stopwords_folder, filename), 'r') as f:
                        custom_stopwords = set(f.read().splitlines())
                        self.stop_words = custom_stopwords      

            # Write stopwords to the file
            with open(self.stopwords_file_path, 'w') as file:
                file.write("\n".join(self.stop_words))
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def remove_stopwords(self, text):

        word_tokens = word_tokenize(text.lower()) # tokenize text
        filtered_text = [word for word in word_tokens if word not in self.stop_words] # remove stopwords
        return ' '.join(filtered_text) # join remaining words back into a string


    def clean_files(self):
        
        """
        Iterate through each file in the directory 'artifacts/extracted_text' and remove stopwords from given stopwords list
        """
        
        try:

            for filename in os.listdir(self.data_folder):
                if filename.endswith('.txt'):  # assuming all files are text files
                    input_file_path = os.path.join(self.data_folder, filename)
                    output_file_path = os.path.join(self.cleaned_folder, filename)
                    with open(input_file_path, 'r', encoding="utf-8") as file:
                        content = file.read()
                    
                    cleaned_content = self.remove_stopwords(content)
                    
                    # Write cleaned content to the new file in the cleaned folder
                    with open(output_file_path, 'w', encoding="utf-8") as file:
                        file.write(cleaned_content)
            logging.info("Removed Stopwords from Extracted Text files and store files in stopword_removed directory")
        except Exception as e:
            raise CustomException(e,sys)

# def main():
#     data_folder = 'artifacts/extracted_text'
#     stopwords_folder = 'artifacts/StopWords'
#     cleaned_folder = 'artifacts/stopword_removed'
#     stopwords_file_path = "artifacts/stopwords.txt"

#     cleaner = TextCleaner(data_folder, stopwords_folder, cleaned_folder, stopwords_file_path)
#     cleaner.clean_files()

# if __name__ == "__main__":
#     main()