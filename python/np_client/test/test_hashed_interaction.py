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

from np_client.models.hashed_interaction import HashedInteraction

class TestHashedInteraction(unittest.TestCase):
    """HashedInteraction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HashedInteraction:
        """Test HashedInteraction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HashedInteraction`
        """
        model = HashedInteraction()
        if include_optional:
            return HashedInteraction(
                interaction_id = '',
                when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source_ids = {
                    'key' : ''
                    },
                target_ids = {
                    'key' : ''
                    },
                event_id = '',
                parent_event_id = '',
                channel_id = '',
                duration_minutes = 56,
                label = [
                    'Chat'
                    ]
            )
        else:
            return HashedInteraction(
        )
        """

    def testHashedInteraction(self):
        """Test HashedInteraction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()