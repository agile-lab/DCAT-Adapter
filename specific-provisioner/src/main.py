# generated by fastapi-codegen:
#   filename:  interface-specification.yml
#   timestamp: 2023-04-07T10:30:49+00:00

from __future__ import annotations

from typing import Union

from fastapi import FastAPI

from .models import (
    ProvisioningRequest,
    ProvisioningStatus,
    SystemError,
    UpdateAclRequest,
    ValidationError,
    ValidationRequest,
    ValidationResult,
    ValidationStatus,
)

app = FastAPI(
    title='Specific Provisioner Micro Service',
    description='Microservice responsible to handle provisioning and access control requests for one or more data product components.',  # noqa: E501
    version='{{version}}',
    servers=[{'url': '/datamesh.specificprovisioner'}],
)


@app.post(
    '/v1/provision',
    response_model=ProvisioningStatus,
    responses={
        '202': {'model': str},
        '400': {'model': ValidationError},
        '500': {'model': SystemError},
    },
    tags=['SpecificProvisioner'],
)
def provision(
    body: ProvisioningRequest,
) -> Union[ProvisioningStatus, str, ValidationError, SystemError]:
    """
    Deploy a data product or a single component starting from a provisioning descriptor
    """
    return SystemError(error="error")


@app.get(
    '/v1/provision/{token}/status',
    response_model=ProvisioningStatus,
    responses={'400': {'model': ValidationError}, '500': {'model': SystemError}},
    tags=['SpecificProvisioner'],
)
def get_status(token: str) -> Union[ProvisioningStatus, ValidationError, SystemError]:
    """
    Get the status for a provisioning request
    """
    return SystemError(error="error")


@app.post(
    '/v1/unprovision',
    response_model=ProvisioningStatus,
    responses={
        '202': {'model': str},
        '400': {'model': ValidationError},
        '500': {'model': SystemError},
    },
    tags=['SpecificProvisioner'],
)
def unprovision(
    body: ProvisioningRequest,
) -> Union[ProvisioningStatus, str, ValidationError, SystemError]:
    """
    Undeploy a data product or a single component given the provisioning descriptor relative to the latest complete provisioning request
    """  # noqa: E501
    return SystemError(error="error")


@app.post(
    '/v1/updateacl',
    response_model=ProvisioningStatus,
    responses={
        '202': {'model': str},
        '400': {'model': ValidationError},
        '500': {'model': SystemError},
    },
    tags=['SpecificProvisioner'],
)
def updateacl(
    body: UpdateAclRequest,
) -> Union[ProvisioningStatus, str, ValidationError, SystemError]:
    """
    Request the access to a specific provisioner component
    """
    return SystemError(error="error")


@app.post(
    '/v1/validate',
    response_model=ValidationResult,
    responses={'500': {'model': SystemError}},
    tags=['SpecificProvisioner'],
)
def validate(body: ProvisioningRequest) -> Union[ValidationResult, SystemError]:
    """
    Validate a provisioning request
    """
    return SystemError(error="error")


@app.post(
    '/v2/validate',
    response_model=None,
    responses={
        '202': {'model': str},
        '400': {'model': ValidationError},
        '500': {'model': SystemError},
    },
    tags=['SpecificProvisioner'],
)
def async_validate(
    body: ValidationRequest,
) -> Union[None, str, ValidationError, SystemError]:
    """
    Validate a deployment request
    """
    return SystemError(error="error")


@app.get(
    '/v2/validate/{token}/status',
    response_model=ValidationStatus,
    responses={'400': {'model': ValidationError}, '500': {'model': SystemError}},
    tags=['SpecificProvisioner'],
)
def get_validation_status(
    token: str,
) -> Union[ValidationStatus, ValidationError, SystemError]:
    """
    Get the status for a provisioning request
    """
    return SystemError(error="error")