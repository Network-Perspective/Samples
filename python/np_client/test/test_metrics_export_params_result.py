# coding: utf-8

"""
    Network Perspective

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: ext-v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from np_client.models.metrics_export_params_result import MetricsExportParamsResult

class TestMetricsExportParamsResult(unittest.TestCase):
    """MetricsExportParamsResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricsExportParamsResult:
        """Test MetricsExportParamsResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsExportParamsResult`
        """
        model = MetricsExportParamsResult()
        if include_optional:
            return MetricsExportParamsResult(
                periods = [
                    ''
                    ],
                metrics = [
                    ''
                    ],
                related_metrics = [
                    ''
                    ],
                categories = [
                    ''
                    ]
            )
        else:
            return MetricsExportParamsResult(
        )
        """

    def testMetricsExportParamsResult(self):
        """Test MetricsExportParamsResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()