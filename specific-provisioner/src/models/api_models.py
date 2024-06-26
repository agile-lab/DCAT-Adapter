from __future__ import annotations

from enum import Enum, StrEnum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Status(Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ValidationRequest(BaseModel):
    descriptor: str


class DescriptorKind(StrEnum):
    DATAPRODUCT_DESCRIPTOR = "DATAPRODUCT_DESCRIPTOR"
    COMPONENT_DESCRIPTOR = "COMPONENT_DESCRIPTOR"
    DATAPRODUCT_DESCRIPTOR_WITH_RESULTS = "DATAPRODUCT_DESCRIPTOR_WITH_RESULTS"


class ProvisioningRequest(BaseModel):
    descriptorKind: DescriptorKind
    descriptor: str = Field(
        ...,
        description="Descriptor specification in yaml format. Its structure changes according to `descriptorKind`.",  # noqa: E501
    )


class Status1(Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ValidationError(BaseModel):
    errors: List[str]


class ProvisionInfo(BaseModel):
    request: str = Field(
        ...,
        description="Provisioning descriptor of type `COMPONENT_DESCRIPTOR` (see [DescriptorKind](#/components/schemas/DescriptorKind) schema) in JSON format. It had been used to provision the data product component",  # noqa: E501
    )
    result: str = Field(
        ...,
        description="Result message (e.g. a provisiong error or a success message returned by the specific provisioner in the [ProvisioningStatus](#/components/schemas/ProvisioningStatus))",  # noqa: E501
    )


class SystemErr(BaseModel):
    error: str


class Info(BaseModel):
    publicInfo: Dict[str, Any] = Field(
        ...,
        description='Fields to display in the Marketplace UI. Note that only the values compliant to specific structures will be rendered in the "Technical Information" card of the Marketplace pages. [Check the documentation](https://docs.internal.witboost.agilelab.it/docs/p3_tech/p3_customizations/p3_4_templates/infrastructureTemplate#specific-provisioner-api-details) for additional details\n',  # noqa: E501
    )
    privateInfo: Dict[str, Any] = Field(
        ...,
        description="All the values in this object will be stored in the deployed descriptor, but will not be shown in the Marketplace UI",  # noqa: E501
    )


class UpdateAclRequest(BaseModel):
    refs: List[str] = Field(
        ...,
        description="Identities (i.e. users and groups) involved in the ACL update request",  # noqa: E501
        examples=[
            "user:alice",
            "user:bob",
            "group:groupA",
            "group:groupB",
            "group:groupC",
        ],
    )
    provisionInfo: ProvisionInfo


class ProvisioningStatus(BaseModel):
    status: Status1
    result: str
    info: Optional[Info] = None


class ValidationResult(BaseModel):
    valid: bool
    error: Optional[ValidationError] = None


class ValidationStatus(BaseModel):
    status: Status
    result: Optional[ValidationResult] = None
