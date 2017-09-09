from .context import auto_abstracts
import unittest

class TestAutoAbstractor(unittest.TestCase):
    def test_top_n(self):
        web_scrape = auto_abstracts.auto_abstractor.Scraping()
        document = web_scrape.scrape('http://jp.techcrunch.com/2017/08/30/20170829a-preview-of-the-first-wave-of-ar-apps-coming-to-iphones/')

        auto_abstractor = auto_abstracts.auto_abstractor.AutoAbstractor()
        abstractable_doc = auto_abstracts.auto_abstractor.AbstractableTopNRank()
        abstractable_doc.set_top_n(3)
        result = auto_abstractor.summarize(document, abstractable_doc)
        [print(sentence) for sentence in result["summarize_result"]]

if __name__ == '__main__':
    unittest.main()
