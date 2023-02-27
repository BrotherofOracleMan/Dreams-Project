# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class DreamAppPipeline:
    def __init__(self) -> None:
        hostname = '' #fill in using os env
        username='' #fill in using os env
        password='' # fill in using os env
        database = ''#fill in using os env

        self.connection = psycopg2.connect(host=hostname, user= username, password=password,dbname= database)

        self.cur = self.connection.cursor()

        self.cur.execute(
        """
        CREATE TABLE if not exists dreams(
            id serial PRIMARY KEY,
            date
        )
        """
        )

        pass
    def process_item(self, item, spider):
        return item