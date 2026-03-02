# read_games.py
# Reads all items from the DynamoDB Games table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Attr

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Games"

def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_game(game):
    """Print a single game's details in a readable format."""
    title = game.get("Title", "Unknown Title")
    developer = game.get("Developer", "Unknown Developer")

    print(f"  Title : {title}")
    print(f"  Developer: {developer}")
    print()

def print_all_games():
    """Scan the entire Games table and print each item."""
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])

    if items:
        print("Games found:\n")
        for game in items:
            print_game(game)
    else:
        print("No games found.")

def main():
    print_all_games()

if __name__ == "__main__":
    main()