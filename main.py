import PyPDF2
import pyttsx3


def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text


def text_to_speech(text, output_path="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


def convert_pdf_to_speech(pdf_path, output_path="output.mp3"):
    text = pdf_to_text(pdf_path)
    text_to_speech(text, output_path)


if __name__ == "__main__":
    pdf_path = "Generative AI-v4.pdf"
    output_path = "output.mp3"

    convert_pdf_to_speech(pdf_path, output_path)

    print(f"Conversion completed. Speech saved to {output_path}")
