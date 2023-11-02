import os

from utils import DocumentProcessor, DocumentReader, DocumentWriter, Proofreader

CHUNK_SIZE = 4000

input_file_path = "article/" + os.listdir("article")[0]
reader = DocumentReader(input_file_path)
output_file_path = "output/output.docx"
writer = DocumentWriter(output_file_path)

if __name__ == "__main__":
    article = reader.read_docx()
    article_processor = DocumentProcessor(article)
    article_chunks = article_processor.chunk_document(CHUNK_SIZE)
    proofreader = Proofreader(
        document_chunks=article_chunks, engine="gpt-3.5-turbo-instruct", temperature=0.5
    )
    proofreader.process_document()
    writer.write_document(proofreader.outputs)
