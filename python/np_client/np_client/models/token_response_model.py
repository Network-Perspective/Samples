# coding: utf-8

"""
    Network Perspective

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: ext-v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TokenResponseModel(BaseModel):
    """
    TokenResponseModel
    """ # noqa: E501
    access_token: Optional[StrictStr] = None
    token_type: Optional[StrictStr] = None
    expires_in: Optional[StrictInt] = None
    refresh_token: Optional[StrictStr] = None
    issued: Optional[StrictStr] = Field(default=None, alias=".issued")
    expires: Optional[StrictStr] = Field(default=None, alias=".expires")
    asclient_id: Optional[StrictStr] = Field(default=None, alias="as:client_id")
    user_name: Optional[StrictStr] = Field(default=None, alias="userName")
    __properties: ClassVar[List[str]] = ["access_token", "token_type", "expires_in", "refresh_token", ".issued", ".expires", "as:client_id", "userName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TokenResponseModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if access_token (nullable) is None
        # and model_fields_set contains the field
        if self.access_token is None and "access_token" in self.model_fields_set:
            _dict['access_token'] = None

        # set to None if token_type (nullable) is None
        # and model_fields_set contains the field
        if self.token_type is None and "token_type" in self.model_fields_set:
            _dict['token_type'] = None

        # set to None if refresh_token (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_token is None and "refresh_token" in self.model_fields_set:
            _dict['refresh_token'] = None

        # set to None if issued (nullable) is None
        # and model_fields_set contains the field
        if self.issued is None and "issued" in self.model_fields_set:
            _dict['.issued'] = None

        # set to None if expires (nullable) is None
        # and model_fields_set contains the field
        if self.expires is None and "expires" in self.model_fields_set:
            _dict['.expires'] = None

        # set to None if asclient_id (nullable) is None
        # and model_fields_set contains the field
        if self.asclient_id is None and "asclient_id" in self.model_fields_set:
            _dict['as:client_id'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TokenResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
            "token_type": obj.get("token_type"),
            "expires_in": obj.get("expires_in"),
            "refresh_token": obj.get("refresh_token"),
            ".issued": obj.get(".issued"),
            ".expires": obj.get(".expires"),
            "as:client_id": obj.get("as:client_id"),
            "userName": obj.get("userName")
        })
        return _obj

