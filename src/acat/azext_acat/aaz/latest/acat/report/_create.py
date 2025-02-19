# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "acat report create",
)
class Create(AAZCommand):
    """Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report.

    :example: Report_CreateOrUpdate
        az acat report create --report-name testReportName --offer-guid 00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002 --resources "[{resource-id:/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/Microsoft.SignalRService/SignalR/mySignalRService,resource-origin:Azure,resource-type:Microsoft.SignalRService/SignalR}]" --storage-info "{account-name:testStorageAccount,location:'East US',resource-group:testResourceGroup,subscription-id:00000000-0000-0000-0000-000000000000}" --time-zone GMT Standard Time --trigger-time 2022-03-04T05:00:00.000Z

    :example: Report_CreateOrUpdate
        az acat report create --report-nameddd testReportName --offer-guid 00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002 --resources "[{resource-id:/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/Microsoft.SignalRService/SignalR/mySignalRService,resource-origin:Azure,resource-type:Microsoft.SignalRService/SignalR}]" --storage-info "{account-name:testStorageAccount,location:'East US',resource-group:testResourceGroup,subscription-id:00000000-0000-0000-0000-000000000000}" --time-zone GMT Standard Time --trigger-time 2022-03-04T05:00:00.000Z
        az acat report create --report-nameddd testReportName  --resources "[{resource-id:/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/Microsoft.SignalRService/SignalR/mySignalRService,resource-origin:Azure,resource-type:Microsoft.SignalRService/SignalR}]"
    """

    _aaz_info = {
        "version": "2024-06-27",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.appcomplianceautomation/reports/{}", "2024-06-27"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.report_name = AAZStrArg(
            options=["--report-name"],
            help="Report Name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[-a-zA-Z0-9_]{1,50}$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.offer_guid = AAZStrArg(
            options=["--offer-guid"],
            arg_group="Properties",
            help="A list of comma-separated offerGuids indicates a series of offerGuids that map to the report. For example, \"00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002\" and \"00000000-0000-0000-0000-000000000003\".",
        )
        _args_schema.resources = AAZListArg(
            options=["--resources"],
            arg_group="Properties",
            help="List of resource data.",
            required=True,
        )
        _args_schema.storage_info = AAZObjectArg(
            options=["--storage-info"],
            arg_group="Properties",
            help="The information of 'bring your own storage' binding to the report",
        )
        _args_schema.time_zone = AAZStrArg(
            options=["--time-zone"],
            arg_group="Properties",
            help="Report collection trigger time's time zone, the available list can be obtained by executing \"Get-TimeZone -ListAvailable\" in PowerShell. An example of valid timezone id is \"Pacific Standard Time\".",
            required=True,
            default="UTC",
        )
        _args_schema.trigger_time_by_codegen = AAZDateTimeArg(
            options=["--trigger-time-by-codegen"],
            arg_group="Properties",
            help="Report collection trigger time.",
            required=True,
        )

        resources = cls._args_schema.resources
        resources.Element = AAZObjectArg()

        _element = cls._args_schema.resources.Element
        _element.account_id = AAZStrArg(
            options=["account-id"],
            help="Account Id. For example - the AWS account id.",
        )
        _element.resource_id = AAZStrArg(
            options=["resource-id"],
            help="Resource Id - e.g. \"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1\".",
            required=True,
        )
        _element.resource_kind = AAZStrArg(
            options=["resource-kind"],
            help="Resource kind.",
        )
        _element.resource_origin = AAZStrArg(
            options=["resource-origin"],
            help="Resource Origin.",
            enum={"AWS": "AWS", "Azure": "Azure", "GCP": "GCP"},
        )
        _element.resource_type = AAZStrArg(
            options=["resource-type"],
            help="Resource type. e.g. \"Microsoft.Compute/virtualMachines\"",
        )

        storage_info = cls._args_schema.storage_info
        storage_info.account_name = AAZStrArg(
            options=["account-name"],
            help="'bring your own storage' account name",
        )
        storage_info.location = AAZStrArg(
            options=["location"],
            help="The region of 'bring your own storage' account",
        )
        storage_info.resource_group = AAZStrArg(
            options=["resource-group"],
            help="The resourceGroup which 'bring your own storage' account belongs to",
        )
        storage_info.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="The subscription id which 'bring your own storage' account belongs to",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ReportCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReportCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.AppComplianceAutomation/reports/{reportName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "reportName", self.ctx.args.report_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-27",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("offerGuid", AAZStrType, ".offer_guid")
                properties.set_prop("resources", AAZListType, ".resources", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("storageInfo", AAZObjectType, ".storage_info")
                properties.set_prop("timeZone", AAZStrType, ".time_zone", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("triggerTime", AAZStrType, ".trigger_time_by_codegen", typ_kwargs={"flags": {"required": True}})

            resources = _builder.get(".properties.resources")
            if resources is not None:
                resources.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.resources[]")
            if _elements is not None:
                _elements.set_prop("accountId", AAZStrType, ".account_id")
                _elements.set_prop("resourceId", AAZStrType, ".resource_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("resourceKind", AAZStrType, ".resource_kind")
                _elements.set_prop("resourceOrigin", AAZStrType, ".resource_origin")
                _elements.set_prop("resourceType", AAZStrType, ".resource_type")

            storage_info = _builder.get(".properties.storageInfo")
            if storage_info is not None:
                storage_info.set_prop("accountName", AAZStrType, ".account_name")
                storage_info.set_prop("location", AAZStrType, ".location")
                storage_info.set_prop("resourceGroup", AAZStrType, ".resource_group")
                storage_info.set_prop("subscriptionId", AAZStrType, ".subscription_id")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.cert_records = AAZListType(
                serialized_name="certRecords",
                flags={"read_only": True},
            )
            properties.compliance_status = AAZObjectType(
                serialized_name="complianceStatus",
                flags={"read_only": True},
            )
            properties.errors = AAZListType(
                flags={"read_only": True},
            )
            properties.last_trigger_time = AAZStrType(
                serialized_name="lastTriggerTime",
                flags={"read_only": True},
            )
            properties.next_trigger_time = AAZStrType(
                serialized_name="nextTriggerTime",
                flags={"read_only": True},
            )
            properties.offer_guid = AAZStrType(
                serialized_name="offerGuid",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resources = AAZListType(
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.storage_info = AAZObjectType(
                serialized_name="storageInfo",
            )
            properties.subscriptions = AAZListType(
                flags={"read_only": True},
            )
            properties.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            properties.time_zone = AAZStrType(
                serialized_name="timeZone",
                flags={"required": True},
            )
            properties.trigger_time = AAZStrType(
                serialized_name="triggerTime",
                flags={"required": True},
            )

            cert_records = cls._schema_on_200_201.properties.cert_records
            cert_records.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.cert_records.Element
            _element.certification_status = AAZStrType(
                serialized_name="certificationStatus",
            )
            _element.controls = AAZListType()
            _element.ingestion_status = AAZStrType(
                serialized_name="ingestionStatus",
            )
            _element.offer_guid = AAZStrType(
                serialized_name="offerGuid",
            )

            controls = cls._schema_on_200_201.properties.cert_records.Element.controls
            controls.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.cert_records.Element.controls.Element
            _element.control_id = AAZStrType(
                serialized_name="controlId",
            )
            _element.control_status = AAZStrType(
                serialized_name="controlStatus",
            )

            compliance_status = cls._schema_on_200_201.properties.compliance_status
            compliance_status.m365 = AAZObjectType(
                flags={"read_only": True},
            )

            m365 = cls._schema_on_200_201.properties.compliance_status.m365
            m365.failed_count = AAZIntType(
                serialized_name="failedCount",
                flags={"read_only": True},
            )
            m365.manual_count = AAZIntType(
                serialized_name="manualCount",
                flags={"read_only": True},
            )
            m365.not_applicable_count = AAZIntType(
                serialized_name="notApplicableCount",
                flags={"read_only": True},
            )
            m365.passed_count = AAZIntType(
                serialized_name="passedCount",
                flags={"read_only": True},
            )
            m365.pending_count = AAZIntType(
                serialized_name="pendingCount",
                flags={"read_only": True},
            )

            errors = cls._schema_on_200_201.properties.errors
            errors.Element = AAZStrType()

            resources = cls._schema_on_200_201.properties.resources
            resources.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.resources.Element
            _element.account_id = AAZStrType(
                serialized_name="accountId",
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )
            _element.resource_kind = AAZStrType(
                serialized_name="resourceKind",
            )
            _element.resource_origin = AAZStrType(
                serialized_name="resourceOrigin",
            )
            _element.resource_type = AAZStrType(
                serialized_name="resourceType",
            )

            storage_info = cls._schema_on_200_201.properties.storage_info
            storage_info.account_name = AAZStrType(
                serialized_name="accountName",
            )
            storage_info.location = AAZStrType()
            storage_info.resource_group = AAZStrType(
                serialized_name="resourceGroup",
            )
            storage_info.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )

            subscriptions = cls._schema_on_200_201.properties.subscriptions
            subscriptions.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
