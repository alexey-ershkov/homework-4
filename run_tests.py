# -*- coding: utf-8 -*-
import sys
import os
import unittest
import threading
from tests import *

results = []
test_reports_dir = "test_reports"


def run_tests(test_suite, test_runner_name):
    print(f"starting test_runner_#{test_runner_name}\n")

    report_filename = f"{test_reports_dir}/test_thread_{test_runner_name}_report.txt"

    with open(report_filename, "w") as output:
        runner_result = unittest.TextTestRunner(output, verbosity=3).run(test_suite)

        if runner_result.wasSuccessful():
            print(f"ended test_runner_#{test_runner_name}: ok\n")
        else:
            print(f"ended test_runner_#{test_runner_name}: failed\n")

        results.append(runner_result)


def create_suite(test_cases) -> unittest.TestSuite:
    loader = unittest.TestLoader()
    new_suite = unittest.TestSuite()

    for test_case in test_cases:
        new_suite.addTests(loader.loadTestsFromTestCase(test_case))

    return new_suite


if __name__ == '__main__':
    all_tests = {
        "alexey_ershkov": [
            FolderTests,
            WorkWithFilesTests,
            TrashBinTests,
            HistoryTests,
        ],
        "esuwu": [
            TabsAtHomePageTest,
            SortAndFilterTest,
            CreatingDocumentsTest,
        ],
        "nickeskov": [
            RecommendTests,
            DragAndDropUploadTests,
            UsualUploadTests
        ]
    }

    try:
        os.mkdir(test_reports_dir)
    except FileExistsError:
        pass

    threads = []

    for name, tests in all_tests.items():
        suite = create_suite(tests)
        thread = threading.Thread(target=run_tests, args=(suite, name))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for result in results:
        if not result.wasSuccessful():
            sys.exit(1)
