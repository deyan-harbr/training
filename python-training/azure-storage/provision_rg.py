from azure.common.client_factory import  get_client_from_cli_profile
from azure.mgmt.resource import  ResourceManagementClient


resource_client = get_client_from_cli_profile(ResourceManagementClient)

rg_result = resource_client.resource_groups.create_or_update("PythonAzureExample-ResourceGroup-01",
                                                             {
                                                                 "location": "centralus"
                                                             })

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")