import typer

app = typer.Typer()

@app.command()
def deploy(asset_type:str,asset_path:str):
    print(f"{asset_type} {asset_path}")

if __name__ == "__main__":
    app()
