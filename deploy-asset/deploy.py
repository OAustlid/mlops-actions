import typer

app = typer.Typer()

@app.command()
def deploy(asset_type:string, asset_path:string):
    print(f"Executing deploy for type {asset_type} and path {asset_path}")

if __name__=="__main__":
    app()