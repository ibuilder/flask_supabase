import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

# Function to Fetch All Games


def find_approvals():
    data = supabase.table("approvals").select("*").execute()
    # Equivalent for SQL Query "SELECT * FROM games;"
    return data['data']


approvals = find_approvals()

# Function to add a new game


def insert_approval(title, project_name, value) -> dict:

    approval = {
        "title": title,
        "project_name": project_name,
        "value": value
    }
    data = supabase.table("approvals").insert(approval).execute()
    # Equivalent to the SQL Insert

    return data['data']
