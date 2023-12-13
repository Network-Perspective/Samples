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

from np_client.models.report_sync_completed_command import ReportSyncCompletedCommand

class TestReportSyncCompletedCommand(unittest.TestCase):
    """ReportSyncCompletedCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportSyncCompletedCommand:
        """Test ReportSyncCompletedCommand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportSyncCompletedCommand`
        """
        model = ReportSyncCompletedCommand()
        if include_optional:
            return ReportSyncCompletedCommand(
                service_token = '',
                sync_period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sync_period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                success = True,
                message = ''
            )
        else:
            return ReportSyncCompletedCommand(
        )
        """

    def testReportSyncCompletedCommand(self):
        """Test ReportSyncCompletedCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()