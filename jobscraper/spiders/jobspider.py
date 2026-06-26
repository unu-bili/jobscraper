import scrapy
import json
from jobscraper.items import JobItem


class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    start_urls = ["https://zangia.mn"]
    headers = {
        'Referer': 'https://zangia.mn/',
        'Origin': 'https://zangia.mn',
    }

    async def start(self):
        url = "https://new-api.zangia.mn/api/jobs/search?limit=90&page=1&isSortByJobs=true&time=1"
        yield scrapy.Request(url, headers=self.headers, callback=self.parse)
        

    def parse(self, response):
        data = json.loads(response.text)
        jobs = data['items']
        meta = data['meta']
        job_item = JobItem()

        ## Getting info for each job
        for job in jobs:        
            # Go into each book individually
            job_code= job.get('code')
            job_item['code'] = job.get('code'),             ## gets code for api request for more info :PP

            job_url = 'https://new-api.zangia.mn/api/jobs/' + job_code  

            yield response.follow(job_url, headers=self.headers, callback = self.parse_job)


        ## Getting info from next page
        next_page = meta['nextPage']
        if next_page is not None:
            next_page_url = (f"https://new-api.zangia.mn/api/jobs/search?limit=90&page={next_page}&isSortByJobs=true&time=1")   
            yield scrapy.Request(next_page_url, callback = self.parse)


    def parse_job(self,response):
        job_data = json.loads(response.text)
        company_data = job_data['company']


        job_item = JobItem()


        job_item['addr_id'] = job_data.get('addr_id')
        job_item['applies'] = job_data.get('applies')
        job_item['company_id'] = job_data.get('company_id')
        job_item['company_name'] = job_data.get('company_name')
        job_item['description'] = job_data.get('description')
        job_item['hits'] = job_data.get('hits')
        job_item['id'] = job_data.get('id')
        job_item['job_level'] = job_data.get('job_level')
        job_item['mlevel'] = job_data.get('mlevel')
        job_item['profession_id'] = job_data.get('profession_id')
        job_item['requirements'] = job_data.get('requirements')
        job_item['salary'] = job_data.get('salary')
        job_item['salary_max'] = job_data.get('salary_max')
        job_item['salary_min'] = job_data.get('salary_min')
        job_item['salary_phrase'] = job_data.get('salary_phrase')
        job_item['shares'] = job_data.get('shares')
        job_item['skills'] = job_data.get('skills')
        job_item['sort_time'] = job_data.get('sort_time')  ## when job was bumped
        job_item['time'] = job_data.get('time')   ## when job was first posted
        job_item['timetype'] = job_data.get('timetype')
        job_item['timetype_id'] = job_data.get('timetype_id')
        job_item['title'] = job_data.get('title')
        job_item['url'] = job_data.get('url')

        ## Company infoo
        job_item['alias'] = company_data.get('alias')
        job_item['branch_id'] = company_data.get('branch_id')                                                   ## salbar id
        job_item['branch_name'] = company_data.get('branch_name')                   ## salbar name
        job_item['comp_id'] = company_data.get('comp_id')
        job_item['founded_year'] = company_data.get('founded_year')
        job_item['group_id'] = company_data.get('group_id')
        job_item['membership_alias'] = company_data.get('membership_alias')
        job_item['membership_title'] = company_data.get('membership_title')
        job_item['name'] = company_data.get('name')
        job_item['staffs_cnt'] = company_data.get('staffs_cnt')
        job_item['website'] = company_data.get('website')
        job_item['work_count'] = company_data.get('work_count')

        yield job_item


{"addr_id": 4976, 
 "applies": 9, 
 "company_id": 4486, 
 "company_name": "Гоёл Кашмер ХХК", 
 "description": "<ul>\r\n<li>Гоёл нэрийн бүтээгдэхүүний деталийг технологийн дагуу чанарын өндөр түвшинд оёх</li>\r\n<li>Бүх гейчын машин барьдаг байх</li>\r\n</ul>\r\n<p>&nbsp;</p>", 
 "hits": 87, 
 "id": 1140170, 
 "job_level": "Менежер", 
 "mlevel": 3, 
 "profession_id": 788, 
 "requirements": "<ul>\r\n<li>Тусгай дунд болон түүнээс дээш боловсролтой</li>\r\n<li>Таваар судлал, нэхмэл, оёмол, сүлжмэл, ээрмэлийн технологийн чиглэлээр их дээд сургууль төгссөн бол давуу тал болно.</li>\r\n<li>Бараа материалын өнгө чанар, хэрэглээний мэдрэмжтэй байх</li>\r\n<li>Мэргэжлийн бусад чадварууд</li>\r\n</ul>", 
 "salary": 7, 
 "salary_max": 3000000, 
 "salary_min": 2500000, 
 "salary_phrase": "2,500,000-3,000,000", 
 "shares": 0, 
 "skills": ["Цагийн менежмент", "Харилцааны чадвар", "Бүтээлч байдал", "Үйлдвэрлэлийн төлөвлөлт", "Чанарын хяналт", "Оёдлын технологи", "Нэхмэлийн үйлдвэрлэл", "Ноос боловсруулах"], 
 "sort_time": 1774595920, 
 "time": 1773717809, 
 "timetype": "Ээлжийн", 
 "timetype_id": 3, 
 "title": "Сүлжих машины оператор", 
 "url": "https://www.zangia.mn/job/_6cfa6loeek", 
 "alias": "goyolcashmere", 
 "branch_id": 10, 
 "branch_name": "Оёдол, сүлжмэл, ноос ноолуурын үйлдвэрлэл", 
 "comp_id": 4486, 
 "founded_year": "2005", 
 "group_id": 0, 
 "membership_alias": "bronze", 
 "membership_title": "Хүрэл", 
 "name": "Гоёл Кашмер ХХК", 
 "staffs_cnt": 200, 
 "website": "www.goyolcashmere.mn ,", 
 "work_count": 12},





        

