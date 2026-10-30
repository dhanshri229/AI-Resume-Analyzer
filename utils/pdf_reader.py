import PyPDF2


# ---------------- PDF TEXT EXTRACTION ----------------

def extract_text(pdf_file):
    """
    Extract all text from a PDF file.
    """

    text = ""

    try:
        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("Error reading PDF:", e)
        return ""

    return text


# ---------------- TOTAL PAGES ----------------

def get_total_pages(pdf_file):
    """
    Return total number of pages in PDF.
    """

    try:
        reader = PyPDF2.PdfReader(pdf_file)
        return len(reader.pages)

    except Exception:
        return 0


# ---------------- PDF VALIDATION ----------------

def is_pdf_valid(pdf_file):
    """
    Check whether uploaded PDF is valid.
    """

    try:
        reader = PyPDF2.PdfReader(pdf_file)
        return len(reader.pages) > 0

    except Exception:
        return False