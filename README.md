# Data Scraper and Analysis Project

This project is designed to scrape data from specified URLs, perform data analysis, and generate metric values for each document.

## Setup

To run this project, follow these steps:

1. Create a conda environment with Python version 3.8.0:
   ```bash
   conda create -n data-scraper python=3.8.0
Activate the conda environment:
bash
Copy code
conda activate data-scraper
Install required packages:
bash
Copy code
pip install -r requirements.txt
Running the Program
Once the environment is set up, follow these steps to run the program:

Navigate to the project directory.
Run the main script:
bash
Copy code
python main.py
Project Structure
scss
Copy code
Data Scraper and Analysis Project
│
├── README.md
├── main.py
├── requirements.txt
├── setup.py
├── analysis_results.xlsx
├── logs/
│   └── (log files)
├── src/
│   ├── components/
│   │   ├── data_scraper.py
│   │   ├── data_cleaner.py
│   │   ├── data_analysis.py
│   │   ├── logger.py
│   │   └── exception.py
│   └── StopWords/
│       ├── StopWords_Auditor.txt
│       ├── StopWords_Currencies.txt
│       ├── StopWords_DatesandNumbers.txt
│       ├── StopWords_Generic.txt
│       ├── StopWords_GenericLong.txt
│       ├── StopWords_Geographic.txt
│       └── StopWords_Names.txt
└── artifacts/
    ├── MasterDictionary/
    │   ├── negative-words.txt
    │   └── positive-words.txt
    ├── extracted_text/
    │   └── (scraped text files)
    └── removed_stopword/
        └── (text files with stopwords removed)
In this project structure:

README.md contains the project documentation.
main.py is the main script to run the program.
requirements.txt lists the required packages.
setup.py is the setup file for the project.
analysis_results.xlsx contains the output of the data analysis.
logs/ directory contains log files generated during program execution.
src/ directory contains the source code of the project.
components/ directory contains modules for data scraping, cleaning, analysis, logging, and exception handling.
StopWords/ directory contains various stopword files.
artifacts/ directory contains generated files during program execution, such as scraped text files and removed stopword files.
Functionality
The program consists of the following modules in src/components:

data_scraper.py: Scrapes data from an Excel file, iterates through the URL column, scrapes data from each URL, and stores the data in the artifacts/extracted_text folder in text format. Each file is named according to the url_id column in the Excel file.
data_cleaner.py: Reads each file from the artifacts/StopWords folder, stores each stopword in artifacts/stopwords.txt, and then iterates through each file from the artifacts/extracted_text folder to remove the stopwords using stopwords.txt. The cleaned files are stored in the artifacts/removed_stopword folder.
data_analysis.py: Analyzes each file in artifacts/removed_stopwords and calculates metric values such as Positive Score, Negative Score, Polarity Score, Subjectivity Score, Average Sentence Length, Percentage of Complex Words, Fog Index, Average Number of Words Per Sentence, Complex Word Count, Word Count, Syllable Count, and Personal Pronouns Count. The output is stored in an Excel file named analysis_results.xlsx against their file names derived from URL_id in the Excel file.
Contributing
Feel free to contribute to this project by forking the repository, making your changes, and submitting a pull request. Your contributions are greatly appreciated!

License
This project is licensed under the MIT License.

Contact
For any questions or suggestions regarding this project, please contact project_author@example.com.