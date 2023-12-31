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

from np_client.models.hashed_entity import HashedEntity

class TestHashedEntity(unittest.TestCase):
    """HashedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HashedEntity:
        """Test HashedEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HashedEntity`
        """
        model = HashedEntity()
        if include_optional:
            return HashedEntity(
                change_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ids = {
                    'key' : ''
                    },
                groups = [
                    ''
                    ],
                props = {
                    'key' : null
                    },
                relationships = [
                    np_client.models.hashed_entity_relationship.HashedEntityRelationship(
                        relationship_name = '', 
                        target_ids = {
                            'key' : ''
                            }, )
                    ]
            )
        else:
            return HashedEntity(
        )
        """

    def testHashedEntity(self):
        """Test HashedEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
