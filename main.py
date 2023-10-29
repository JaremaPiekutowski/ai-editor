import os

from utils import DocumentProcessor, DocumentReader, DocumentWriter, Proofreader

# File path - read the "article" folder and get first file
input_file_path = "article/" + os.listdir("article")[0]
reader = DocumentReader(input_file_path)
output_file_path = "output/output.docx"
writer = DocumentWriter(output_file_path)

if __name__ == "__main__":
    article = reader.read_docx()
    print("ARTICLE READ. FIRST 10 CHARS:", article[:10])
    article_processor = DocumentProcessor(article)
    article_chunks = article_processor.chunk_document(4000)
    print("NUMBER OF CHUNKS", len(article_chunks))
    proofreader = Proofreader(
        document_chunks=article_chunks,
        engine="gpt-3.5-turbo-instruct",
        temperature=0.5
        )
    proofreader.process_document()
    writer.write_document(proofreader.outputs)
