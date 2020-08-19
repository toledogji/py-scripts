import os
import re

import PyPDF2

email_pattern = r"([a-zA-Z][a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-z]{2,5})"
pattern = re.compile(email_pattern)

out_file_name = "emails.csv"
out_file = open(out_file_name, "w")
out_file.write("filename, email\n")

dir_content = os.listdir(".")
pdf_files = [doc for doc in dir_content if doc.endswith("pdf")]
processed = 0

for pdf_file in pdf_files:
    print(f"Extracting email from {pdf_file}...")

    pdf_fd = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_fd)

    num_pages = pdf_reader.numPages
    emails = []

    for page in range(num_pages):
        page_obj = pdf_reader.getPage(page)
        text = page_obj.extractText()
        text = text.replace("\n", "")
        email_match = pattern.search(text)

        if email_match is not None:
            email = email_match.group()
            if email not in emails:
                emails.append(email)

    if len(emails) == 0:
        print(f"\t=> Email could not be extracted from file {pdf_file}.")

    pdf_fd.close()

    for email in emails:
        out_file.write(f"{pdf_file}, {email}\n")

    processed += 1

out_file.close()
print(f"Processed {processed} of {len(pdf_files)} documents")