import fitz
import csv
import os

def extract_table_from_pdf(pdf_file, csv_file):
    doc = fitz.open(pdf_file)
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        for i in range(doc.page_count):
            csv_writer = csv.writer(csvfile)
            page=doc[i]
            tables=page.find_tables()
            if tables.tables:
                d = tables[0].extract()
                if i == 0:
                    head = [i.replace('\n',' ') for i in d[0]]
                    csv_writer.writerow(head)
                csv_writer.writerows(d[1:])
            print(f'{i}/{doc.page_count}')

extract_table_from_pdf('EB_Purchase_Detail.pdf', 'EB_Purchase_Detail.csv')
extract_table_from_pdf('EB_Purchase_Detail.pdf', 'EB_Redemption_Detail.csv')