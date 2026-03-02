import unittest
from app.services.excel_reader import ExcelReader
import pandas as pd
from typing import List
from app.models.report import Report
# excel_reader = ExcelReader("GRI_2017_2020 (1).xlsx")
# reports = excel_reader.read_reports()
# print(reports[0].primary_url)




class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.excel_reader = ExcelReader("GRI_2017_2020 (1).xlsx")
        self.reports = self.excel_reader.read_reports()

    def test_primary_url(self):
        self.assertEqual(self.reports[0].primary_url, "http://arpeissig.at/wp-content/uploads/2016/02/D7_NHB_ARP_Final_2.pdf")
    
    def test_is_na(self):
        self.assertTrue(pd.isna(self.excel_reader.df['Pdf_URL'][5]))

    def test_5th_report_row(self):
        self.assertTrue(self.reports[5].primary_url, "http://ebooks.exakta.se/aak/2017/hallbarhetsrapport_2016_2017_en/pubData/source/aak_sustainability_report_2016_2017_ebook.pdf")

    def test_remove_na(self):
        self.assertNotEqual(self.excel_reader.df['Pdf_URL'][5], self.reports[5].primary_url)


if __name__ == '__main__':
    unittest.main()