import typer
from azure.identity import DefaultAzureCredential, AzureCliCredential,ChainedTokenCredential
from azure.ai.ml import MLClient
import os

app = typer.Typer()

@app.command()
def help():
    print(f"""
    Provide a subscription_id, a resource group name and a workspace_name.
    Then this app will print out the environments it finds beneath it.
    """)

@app.command()
def getenvlist(token:str,subscription_id:str,resource_group_name:str,workspace_name:str):
    print(f"Environments in /SUBSCRIPTIONS/{subscription_id}/RESOURCEGROUPS/{resource_group_name}/PROVIDERS/Microsoft.MachineLearningServices/WORKSPACES/{workspace_name} :")
    print(f"Length of token: {len(token)}")
    
    #access_token = os.environ.get("AZURE_ACCESS_TOKEN")

    #if (token is None) or (token ==""):
    #    credential = ChainedTokenCredential(
    #        AzureCliCredential(process_timeout=10),
    #        DefaultAzureCredential(process_timeout=10)
    #    )
    #else:
    credential = DefaultAzureCredential(managed_identity_client_id=token)

    client = MLClient(
        credential=credential,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        workspace_name=workspace_name
    )
    e_list = list(client.environments.list())
    for e in e_list:
        print(f"Environment: {e.name}, {e.latest_version}")

@app.command()
def listenvvars():
    for k, v in os.environ.items():
        print(f"{k}={v}")

if __name__ == "__main__":
    app()
