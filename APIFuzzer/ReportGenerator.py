import unittest
import HTMLTestRunner
import os
import SeleniumCases
import SearchForProductCase
import OrderSummaryCase

indir = os.getcwd()


class MyTestSuite(unittest.TestCase):
    smoke_test = unittest.TestSuite()
    smoke_test.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(SearchForProductCase.SearchForProduct),
        unittest.defaultTestLoader.loadTestsFromTestCase(OrderSummaryCase.OrderSummeryCase),
    ])
    #search_test = unittest.TestLoader().loadTestsFromTestCase(SeleniumCases.PythonOrgSearch)

    #creating_test_suite = unittest.TestSuite([search_test])

    outfile = open('C:\\Users\\bhagi\\PycharmProjects\\APIFuzzer\\templates\htmlreport.html', "wb")

    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke_Test'
    )

    # run the suite using HTMLTestRunner
    runner.run(smoke_test)


if __name__ == '__main__':
    unittest.main()