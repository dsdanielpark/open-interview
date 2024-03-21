from PyPDF2 import PdfReader


def load_file_content(file_path):
    """
    Reads the content of a file. Supports .txt and .pdf file formats.
    """
    text_content = ""
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text_content = " ".join(
            page.extract_text()
            for page in reader.pages
            if page.extract_text() is not None
        )
    else:
        raise ValueError("Unsupported file format. Please use .txt or .pdf files.")
    return text_content
