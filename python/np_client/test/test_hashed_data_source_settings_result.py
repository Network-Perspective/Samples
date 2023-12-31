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

from np_client.models.hashed_data_source_settings_result import HashedDataSourceSettingsResult

class TestHashedDataSourceSettingsResult(unittest.TestCase):
    """HashedDataSourceSettingsResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HashedDataSourceSettingsResult:
        """Test HashedDataSourceSettingsResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HashedDataSourceSettingsResult`
        """
        model = HashedDataSourceSettingsResult()
        if include_optional:
            return HashedDataSourceSettingsResult(
                whitelist = [
                    ''
                    ],
                blacklist = [
                    ''
                    ],
                custom_attributes = np_client.models.hashed_data_source_custom_attributes_settings_result.HashedDataSourceCustomAttributesSettingsResult(
                    group = [
                        ''
                        ], 
                    prop = [
                        ''
                        ], 
                    relationship = [
                        np_client.models.hashed_data_source_custom_relationship_settings_result.HashedDataSourceCustomRelationshipSettingsResult(
                            prop_name = '', 
                            relationship_name = '', )
                        ], )
            )
        else:
            return HashedDataSourceSettingsResult(
        )
        """

    def testHashedDataSourceSettingsResult(self):
        """Test HashedDataSourceSettingsResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
