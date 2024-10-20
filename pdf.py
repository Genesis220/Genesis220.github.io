import os
import datetime

# Define paths
pdf_folder = './assets/pdfs'
post_folder = './_posts'

# Get the current date for naming the post
today = datetime.date.today()

# Scan the PDF folder for files
pdf_files = os.listdir(pdf_folder)

# Loop over each PDF file and create a markdown file if it doesn't already exist
for pdf_file in pdf_files:
    # Ignore non-pdf files
    if not pdf_file.endswith('.pdf'):
        continue
    
    # Generate a markdown filename based on the current date and PDF name
    pdf_name = os.path.splitext(pdf_file)[0]
    markdown_filename = f"{post_folder}/{today}-{pdf_name}.md"

    # Check if the markdown file already exists
    if os.path.exists(markdown_filename):
        print(f"{markdown_filename} already exists, skipping...")
        continue

    # Create the markdown content
    markdown_content = f"""---
layout: article
title: "{pdf_name.capitalize()}"
date: {today}
pdf: "{pdf_file}"
---
"""

    # Write the markdown file
    with open(markdown_filename, 'w') as md_file:
        md_file.write(markdown_content)
        print(f"Created: {markdown_filename}")
