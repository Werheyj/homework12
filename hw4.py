import logging
import unittest
from hw1 import RunnerTest


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(levelname)s * %(message)s')

    unittest.main()
