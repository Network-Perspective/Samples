# coding: utf-8

"""
    Network Perspective

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: ext-v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from np_client.api.report_api import ReportApi


class TestReportApi(unittest.TestCase):
    """ReportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportApi()

    def tearDown(self) -> None:
        pass

    def test_report_export_metric_params(self) -> None:
        """Test case for report_export_metric_params

        Export metric params
        """
        pass

    def test_report_export_metric_related_values(self) -> None:
        """Test case for report_export_metric_related_values

        Export related metrics
        """
        pass

    def test_report_export_metric_values(self) -> None:
        """Test case for report_export_metric_values

        Export direct metrics
        """
        pass


if __name__ == '__main__':
    unittest.main()
