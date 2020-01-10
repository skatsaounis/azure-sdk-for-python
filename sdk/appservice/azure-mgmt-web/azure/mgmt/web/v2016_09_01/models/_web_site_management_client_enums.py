# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    in_progress = "InProgress"
    deleting = "Deleting"


class HostingEnvironmentStatus(str, Enum):

    preparing = "Preparing"
    ready = "Ready"
    scaling = "Scaling"
    deleting = "Deleting"


class InternalLoadBalancingMode(str, Enum):

    none = "None"
    web = "Web"
    publishing = "Publishing"


class ComputeModeOptions(str, Enum):

    shared = "Shared"
    dedicated = "Dedicated"
    dynamic = "Dynamic"


class WorkerSizeOptions(str, Enum):

    default = "Default"
    small = "Small"
    medium = "Medium"
    large = "Large"
    d1 = "D1"
    d2 = "D2"
    d3 = "D3"


class AccessControlEntryAction(str, Enum):

    permit = "Permit"
    deny = "Deny"


class RouteType(str, Enum):

    default = "DEFAULT"
    inherited = "INHERITED"
    static = "STATIC"


class ManagedServiceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"


class AutoHealActionType(str, Enum):

    recycle = "Recycle"
    log_event = "LogEvent"
    custom_action = "CustomAction"


class ConnectionStringType(str, Enum):

    my_sql = "MySql"
    sql_server = "SQLServer"
    sql_azure = "SQLAzure"
    custom = "Custom"
    notification_hub = "NotificationHub"
    service_bus = "ServiceBus"
    event_hub = "EventHub"
    api_hub = "ApiHub"
    doc_db = "DocDb"
    redis_cache = "RedisCache"
    postgre_sql = "PostgreSQL"


class ScmType(str, Enum):

    none = "None"
    dropbox = "Dropbox"
    tfs = "Tfs"
    local_git = "LocalGit"
    git_hub = "GitHub"
    code_plex_git = "CodePlexGit"
    code_plex_hg = "CodePlexHg"
    bitbucket_git = "BitbucketGit"
    bitbucket_hg = "BitbucketHg"
    external_git = "ExternalGit"
    external_hg = "ExternalHg"
    one_drive = "OneDrive"
    vso = "VSO"


class ManagedPipelineMode(str, Enum):

    integrated = "Integrated"
    classic = "Classic"


class SiteLoadBalancing(str, Enum):

    weighted_round_robin = "WeightedRoundRobin"
    least_requests = "LeastRequests"
    least_response_time = "LeastResponseTime"
    weighted_total_traffic = "WeightedTotalTraffic"
    request_hash = "RequestHash"


class SupportedTlsVersions(str, Enum):

    one_full_stop_zero = "1.0"
    one_full_stop_one = "1.1"
    one_full_stop_two = "1.2"


class SslState(str, Enum):

    disabled = "Disabled"
    sni_enabled = "SniEnabled"
    ip_based_enabled = "IpBasedEnabled"


class HostType(str, Enum):

    standard = "Standard"
    repository = "Repository"


class UsageState(str, Enum):

    normal = "Normal"
    exceeded = "Exceeded"


class SiteAvailabilityState(str, Enum):

    normal = "Normal"
    limited = "Limited"
    disaster_recovery_mode = "DisasterRecoveryMode"


class StatusOptions(str, Enum):

    ready = "Ready"
    pending = "Pending"
    creating = "Creating"


class OperationStatus(str, Enum):

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"