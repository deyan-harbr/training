
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient

resource_client = get_client_from_cli_profile(ResourceManagementClient)
rg = resource_client.resource_groups.delete(resource_group_name="PythonAzureExample-Storage-01")


