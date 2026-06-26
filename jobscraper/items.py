# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    code = scrapy.Field()
    address = scrapy.Field()
    applies = scrapy.Field()
    code = scrapy.Field()
    company_alias = scrapy.Field()
    company_name_mn = scrapy.Field()
    company_name_en = scrapy.Field()
    salary = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_phrase = scrapy.Field()
    search_description = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()

    addr_id = scrapy.Field()
    applies = scrapy.Field()
    company_id = scrapy.Field()
    company_name = scrapy.Field()
    description = scrapy.Field()
    hits = scrapy.Field()
    id = scrapy.Field()
    job_level = scrapy.Field()
    mlevel = scrapy.Field()
    profession_id = scrapy.Field()
    requirements = scrapy.Field()
    salary = scrapy.Field()
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    salary_phrase = scrapy.Field()
    shares = scrapy.Field()
    skills = scrapy.Field()
    sort_time = scrapy.Field()  ## when job was bumped
    time = scrapy.Field()   ## when job was first posted
    timetype = scrapy.Field()
    timetype_id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

        ## Company infoo
    alias = scrapy.Field()
    branch_id = scrapy.Field()                                                   ## salbar id
    branch_name = scrapy.Field()                   ## salbar name
    comp_id = scrapy.Field()
    founded_year = scrapy.Field()
    group_id = scrapy.Field()
    membership_alias = scrapy.Field()
    membership_title = scrapy.Field()
    name = scrapy.Field()
    staffs_cnt = scrapy.Field()
    website = scrapy.Field()
    work_count = scrapy.Field()
