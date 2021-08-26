
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
document...
"""

import unittest
import warnings

from test_huggin import nodes

class KNIMETestCase(unittest.TestCase):

    def setUp(self):
        self.dummy = 'dummy'
        self.arg = dict.fromkeys(['text', 'context', 'question'])
        self.text = """Almost five years ago, the International Consortium of Investigative Journalists published its Lux Leaks investigation, exposing how some of the world’s largest corporations cycled billions of dollars through Luxembourg so as to avoid paying huge amounts of tax — taxes that otherwise could have ended up in the coffers of other European countries.
                    The revelations laid bare more than 300 secret tax deals that Luxembourg had struck with global businesses, including Disney, Skype, GlaxoSmithKline, Koch Industries and Black & Decker.
                    In several cases, the deals — known as “tax rulings” — allowed firms to pay less than 1 percent tax in Luxembourg.
                    The EU’s second smallest member state was secretly offering huge tax favors on an industrial scale. 
                    In some instances, leaked documents showed officials even granted lucrative tax deductions for “deemed interest” — that is, pretend payments of interest on loans that, in reality, were interest-free.
                    In 2014, there were immediate calls for the European Union’s then-new competition commissioner Margrethe Vestager to take action.
                    If Luxembourg’s tax rulings were found to offer benefits to preferred companies then Vestager could use EU competition law — which bars countries from giving state aid to favored businesses — to reverse these deals and force multinationals to make up years of tax underpayment.
                    But Vestager declined immediate action.
                    """
        self.locations = ['Luxembourg', 'European Union']
        self.persons = ['Margrethe Vestager']
        self.question = "What was the tax rate payed by firms in Luxembourg?"
        self.sentence = "What a great Summer in Luxembourg!"
    
    def test1_sentiment():
        self.arg.update({'text': self.sentence})
        sent = nodes.KSentiment(); 
        res = sent(self.arg)
        self.assertEqual(res.label[0], 'POSITIVE')
        self.assertGreater(res.score[0], 0.5)

    def test1_ner():
        self.arg.update({'text': self.text})
        ner = nodes.KNER(); 
        res = ner(self.arg)
        self.assertNotEqual(set(res.loc[res.entity=='I-LOC','word'].values).intersection(locations), set())
        self.assertNotEqual(set(res.loc[res.entity=='I-PER','word'].values).intersection(persons), set())

    def test2_qa():
        self.arg.update({'context': self.text, 'question': self.question})
        qa = nodes.KQA()
        res = qa(self.arg)
        self.assertNotEqual(res.answer[0] = 'less than 1 percent tax')

    def test3_summary():
        self.arg.update({'text': self.text})
        summary = nodes.KSummary
        res = summary(self.arg)
        pass # what to test?

if __name__ == '__main__':
    unittest.main()