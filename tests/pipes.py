
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
document...
"""

import unittest
import warnings

from test_huggin import pipes

class PipelineTestCase(unittest.TestCase):

    def setUp(self):
        self.dummy = 'dummy'
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

    def test0_PipelineWrapper():
        P = pipes.PipelineWrapper()
        self.assertEqual(P.pipe, None)
        P = pipes.PipelineWrapper(self.dummy)
        self.assertEqual(P.pipe, self.dummy)
        with self.assertRaises(IOError):
            P(self.text)

    def test1_Sentiment():
        sent = pipes.Sentiment(); 
        self.assertEqual(sent.pipe, 'sentiment-analysis')
        res = sent(self.sentence)
        self.assertEqual(res.label[0], 'POSITIVE')
        self.assertGreater(res.score[0], 0.5)

    def test1_NER():
        ner = pipes.NER(); 
        self.assertEqual(ner.pipe, 'ner')
        res = ner(self.text)
        self.assertNotEqual(set(res.loc[res.entity_group=='LOC','word'].values).intersection(locations), set())
        self.assertNotEqual(set(res.loc[res.entity_group=='PER','word'].values).intersection(persons), set())

    def test2_QA():
        qa = pipes.QA()
        self.assertEqual(qa.pipe, 'question-answering')
        res = qa(question = self.question, context = self.text)
        self.assertNotEqual(res.answer[0] = 'less than 1 percent tax')

    def test3_Summary():
        summary = pipes.Summary
        self.assertEqual(summary.pipe, 'summarization')
        res = summary('text')
        pass # what to test?
        
    # and so on...
       
#/****************************************************************************/
def __runtest_this_module(*TestCases, **kwargs):
    if len(TestCases)==0:                       
        return
    for testCase in TestCases:
        try:
            t_class = testCase.__name__
            t_module = testCase.__module__
        except: raise IOError('unexpected input testing class entity')
        else:
            t_module_basename = t_module.split('.')[-1]        
        try:
            t_submodule = testCase.module
        except: raise IOError('unrecognised tested submodule')
        message = ''
        message += '\n{}: Test {}.py module of {}.{}'
        warnings.warn(message.format(t_class, t_submodule, metadata.package, t_module_basename))
        verbosity = kwargs.pop('verbosity',2)
        suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
        unittest.TextTestRunner(verbosity = verbosity).run(suite)
        if len(TestCases)>1 and testCase!=TestCases[-1]: 
            time.sleep(1)
    return

def runtest():
    __runtest_this_module(PipelineTestCase)
    return

if __name__ == '__main__':
    # runtest()
    unittest.main()
