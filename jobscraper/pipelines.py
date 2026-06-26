# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bs4 import BeautifulSoup


class JobscraperPipeline:
    from bs4 import BeautifulSoup

    def clean_requirements(self, text):
        if not text:
            return []
        
        soup = BeautifulSoup(text, 'html.parser')
        
        # handle <ul><li> structure
        if soup.find('li'):
            return [li.get_text(strip=True) for li in soup.find_all('li')]
        
        # handle <p><br> structure
        else:
            # replace <br> with newline then split
            for br in soup.find_all('br'):
                br.replace_with('\n')
            return [line.strip() for line in soup.get_text().splitlines() if line.strip()]

    def process_item(self, item, spider):
        if item.get('requirements'):
            item['requirements'] = self.clean_requirements(item['requirements'])
            

        if item.get('description'):
            soup = BeautifulSoup(item['description'], 'html.parser')
            item['description'] = [li.get_text(strip=True) for li in soup.find_all('li')]

        return item