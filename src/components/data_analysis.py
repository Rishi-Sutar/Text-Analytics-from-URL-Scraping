import os
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import re
from src.logger import logging

class SentimentAnalyzer:
    def __init__(self, positive_words_file, negative_words_file, stopword_file, stopwords_removed_folder):
        self.positive_words = self.read_words_from_file(positive_words_file)
        self.negative_words = self.read_words_from_file(negative_words_file)
        self.stop_words = self.read_words_from_file(stopword_file)
        self.stopwords_removed_folder = stopwords_removed_folder

    def read_words_from_file(self, file_path, encoding='latin-1'):
        with open(file_path, 'r', encoding=encoding) as file:
            words = set(file.read().splitlines())
        return words

    def calculate_scores(self, text):
        tokens = nltk.word_tokenize(text.lower())
        positive_score = sum(1 for token in tokens if token in self.positive_words)
        negative_score = sum(1 for token in tokens if token in self.negative_words)
        total_words = len(tokens)
        polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
        return positive_score, negative_score, polarity_score, subjectivity_score


    def calculate_average_sentence_length(self, text):
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        num_sentences = len(sentences)
        num_words = len(words)
        if num_sentences == 0:
            return 0
        return num_words / num_sentences

    def calculate_percentage_complex_words(self, complex_word_count, word_count):
        percent_complex_word = (complex_word_count / word_count)
        return percent_complex_word
    
    def calculate_fog_index(self, avg_sentence_length, percentage_complex_words):
        return 0.4 * (avg_sentence_length + percentage_complex_words)

    def calculate_avg_word_per_sentence(self, text):
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        return len(words) / len(sentences) if len(sentences) > 0 else 0

    def calculate_complex_word_count(self, text):
        # Initialize a list to store complex words
        complex_words = []

        # Tokenize the text into words
        words = word_tokenize(text.lower())

        # Iterate through each word
        for word in words:
            # Calculate syllable count for the current word
            syllable_count = self.calculate_syllable_count(word)

            # If the word has more than two syllables, add it to the list of complex words
            if syllable_count > 2:
                complex_words.append(word)

        return len(complex_words)

    def calculate_word_count(self, text):
        # Tokenize the text into words
        words = nltk.word_tokenize(text)

        # Get English stopwords
        stop_words = set(stopwords.words('english'))

        # Remove stopwords and punctuation
        cleaned_words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]

        return len(cleaned_words) 
    
    def calculate_syllable_count(self, text):

        count = 0
        words = word_tokenize(text.lower())
        # Iterate through each word and count syllables
        for word in words:
            # Remove any trailing "es" or "ed"
            if word.endswith("es") or word.endswith("ed"):
                word = word[:-2]
        
            vowels = "aeiou"
            vowel_count = sum(1 for char in word if char in vowels)
            count += vowel_count
    
            syllable_count = count / len(words)
                
        return syllable_count

    def calculate_personal_pronouns_count(self, text):
        personal_pronouns = ["I", "we", "my", "ours", "us"]
        pattern = re.compile(r'\b(?:{})\b'.format('|'.join(personal_pronouns)), flags=re.IGNORECASE)
        return len(re.findall(pattern, text))

    def calculate_avg_word_length(self, text):
        words = word_tokenize(text)
        total_length = sum(len(word) for word in words)
        if len(words) > 0:
            return total_length / len(words) 
        else:
            return 0
    
    def analyze_text_files(self):
        data = []
        for file_name in os.listdir(self.stopwords_removed_folder):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.stopwords_removed_folder, file_name)
                with open(file_path, 'r', encoding='latin-1') as file:
                    text = file.read()
                    positive_score, negative_score, polarity_score, subjectivity_score = self.calculate_scores(text)
                    avg_sentence_length = self.calculate_average_sentence_length(text)
                    complex_word_count = self.calculate_complex_word_count(text)
                    word_count = self.calculate_word_count(text)
                    percentage_complex_words = self.calculate_percentage_complex_words(complex_word_count, word_count)
                    fog_index = self.calculate_fog_index(avg_sentence_length, percentage_complex_words)
                    avg_word_per_sentence = self.calculate_avg_word_per_sentence(text)
                    syllable_count = self.calculate_syllable_count(text)
                    personal_pronouns_count = self.calculate_personal_pronouns_count(text)
                    avg_word_length = self.calculate_avg_word_length(text)
                    data.append({
                        'File Name': file_name,
                        'Positive Score': positive_score,
                        'Negative Score': negative_score,
                        'Polarity Score': polarity_score,
                        'Subjectivity Score': subjectivity_score,
                        'Average Sentence Length': avg_sentence_length,
                        'Percentage of Complex Words': percentage_complex_words,
                        'Fog Index': fog_index,
                        'Average Number of Words Per Sentence': avg_word_per_sentence,
                        'Complex Word Count': complex_word_count,
                        'Word Count': word_count,
                        'Syllable Count': syllable_count,
                        'Personal Pronouns Count': personal_pronouns_count,
                        'Average Word Length': avg_word_length
                    })
        df = pd.DataFrame(data)
        output_file = "analysis_results.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Analysis results saved to {output_file}")
        logging.info("Analysis results saved")

# Example usage:
# positive_words_file = "artifacts/MasterDictionary/positive-words.txt"
# negative_words_file = "artifacts/MasterDictionary//negative-words.txt"
# folder_path = "artifacts/stopword_removed"
# stopword_file = "artifacts/stopwords.txt"
# analyzer = SentimentAnalyzer(positive_words_file, negative_words_file, stopword_file, folder_path)
# analyzer.analyze_text_files()
