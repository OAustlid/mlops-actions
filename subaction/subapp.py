import typer
from azure.identity import DefaultAzureCredential, AzureCliCredential,ChainedTokenCredential
from azure.ai.ml import MLClient

app = typer.Typer()

@app.command()
def deploy(asset_type:str,asset_path:str):
    print(f"subaction: {asset_type} {asset_path}")


if __name__ == "__main__":
    app()
