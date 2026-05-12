import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
        if not text.strip():
            raise ValueError("No text found in the PDF.")
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {pdf_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while extracting text: {str(e)}")

def extract_text_from_text(txt_path: str) -> str:
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
        if not text.strip():
            raise ValueError("No text found in the text file.")
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {txt_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while extracting text: {str(e)}")
    
def clean_text(text: str) -> str:
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    cleaned_text = ' '.join([word for word in word_tokens if word.isalpha() and word not in stop_words])
    return cleaned_text