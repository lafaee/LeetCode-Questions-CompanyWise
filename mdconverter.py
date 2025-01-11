import csv
import argparse

def csv_to_markdown(csv_file, markdown_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)    
        rows = list(reader)

    with open(markdown_file, 'w') as mdfile:

        mdfile.write('| ' + ' | '.join(rows[0]) + ' |\n')
        mdfile.write('| ' + ' | '.join(['---'] * len(rows[0])) + ' |\n')
        for row in rows[1:]:
            mdfile.write('| ' + ' | '.join(row) + ' |\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file to a Markdown table.")
    parser.add_argument("csv_file", help="Input CSV file")
    parser.add_argument("markdown_file", help="Output Markdown file")
    args = parser.parse_args()

    csv_to_markdown(args.csv_file, args.markdown_file)
