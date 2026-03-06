import unittest
from app.services.excel_reader import ExcelReader
import pandas as pd
from typing import List
from app.models.report import Report
from app.services.downloader import PDFDownloader
import os
import shutil
# excel_reader = ExcelReader("GRI_2017_2020 (1).xlsx")
# reports = excel_reader.read_reports()
# print(reports[0].primary_url)




class TestStringMethods(unittest.TestCase):

    excel_reader = ExcelReader("GRI_2017_2020 (1).xlsx")
    reports = excel_reader.read_reports()
    TEST_FOLDER  = "downloads_tests"

    def setUp(self):
        os.makedirs(self.TEST_FOLDER, exist_ok=True)
        self.downloader = PDFDownloader(
            output_directory=self.TEST_FOLDER,
            max_workers=1,
            timeout_seconds=5
        )


    def tearDown(self):
        if os.path.exists(self.TEST_FOLDER):
            shutil.rmtree(self.TEST_FOLDER)


    def test_primary_url(self):
        report = Report(
            br_number="TEST_PRIMARY",
            primary_url="https://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf",
        )

        result = self.downloader._download_single_report(report)

        self.assertEqual(result.primary_url, "https://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf")
        self.assertEqual(result.status, "success")
    

    def test_fallback_url(self):
        report = Report(
            br_number="TEST_FALLBACK",
            primary_url="INVALID_URL",
            fallback_url="https://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf"
        )

        result = self.downloader._download_single_report(report)

        self.assertEqual(result.fallback_url, "https://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf")
        self.assertEqual(result.status, "success")
    

    def test_invalid_url(self):
        report = Report(
            br_number="TEST_INVALID",
            primary_url="INVALID_URL",
            fallback_url="INVALID_URL_TWO"
        )

        result = self.downloader._download_single_report(report)
        self.assertEqual(result.status, "failed")
        self.assertIsNone(result.file_path)
        
    
    def test_is_na(self):
        self.assertTrue(pd.isna(self.excel_reader.df['Pdf_URL'][5]))


    def test_5th_report_row(self):
        self.assertTrue(self.reports[5].primary_url, "http://ebooks.exakta.se/aak/2017/hallbarhetsrapport_2016_2017_en/pubData/source/aak_sustainability_report_2016_2017_ebook.pdf")


    def test_remove_na(self):
        self.assertNotEqual(self.excel_reader.df['Pdf_URL'][5], self.reports[5].primary_url)


if __name__ == '__main__':
    unittest.main()