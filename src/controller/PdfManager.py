from pypdf import PdfReader

class PdfManager(object):
    def parsePdf(self, filename):
        reader = PdfReader(filename)
        print(f'Number of Pages: {len(reader.pages)}')
        for page in range(len(reader.pages)):
            text = reader.pages[page].extract_text()
        
        return text