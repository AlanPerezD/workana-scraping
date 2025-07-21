import csv
from bs4 import BeautifulSoup

# CSV output file
with open('projects.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
        'URL', 'Project title', 'Category', 'Subcategory',
        'Budget', 'Numbers of proposals (bids)',
        'Client frequency', 'Keywords', 'Age (date)'
    ])

    # Loop through HTML pages: page-1.html to page-20.html
    for page_num in range(1, 21):
        filename = f'./asset/page-{page_num}.html'
        with open(filename, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Loop through project-item elements from 3 to 22
        for i in range(3, 23):
            title_elem = soup.select_one(f'div.project-item:nth-child({i}) > div:nth-child(1) > h2:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
            date_elem = soup.select_one(f'div.project-item:nth-child({i}) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
            bids_elem = soup.select_one(f'div.project-item:nth-child({i}) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)')
            budget_elem = soup.select_one(f'div.project-item:nth-child({i}) > div:nth-child(5) > h4:nth-child(2) > span:nth-child(1) > span:nth-child(1)')

            url = title_elem.get('href') if title_elem else ''
            project_title = title_elem.get_text(strip=True) if title_elem else ''
            budget = budget_elem.get_text(strip=True) if budget_elem else ''
            bids = bids_elem.get_text(strip=True) if bids_elem else ''
            date = date_elem.get_text(strip=True) if date_elem else ''

            writer.writerow([
                url,
                project_title,
                '',  # Category
                '',  # Subcategory
                budget,
                bids,
                '',  # Client frequency
                '',  # Keywords
                date
            ])
