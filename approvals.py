import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

# Function to Fetch All Games


def find_all_approvals():
    data = SUPA.table("approvals").select("*").execute()
    # Equivalent for SQL Query "SELECT * FROM games;"
    return data['data']


approvals = find_all_approvals()

# Function to add a new game


def add_approval_to_DB(title, project_name, value) -> dict:

    approval = {
        "title": title,
        "project_name": project_name,
        "value": value
    }
    data = SUPA.table("approvals").insert(approval).execute()
    # Equivalent to the SQL Insert

    return data['data']
