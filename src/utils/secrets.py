from google.cloud import secretmanager
from google.oauth2 import service_account
import os


def start_secret_env():
    """Start load secret env."""
    try:
        secrets = access_secret_version(
            os.environ.get("PROJECT_ID"), os.environ.get("PROJECT_ENVIRON")
        )
        open(".env", "w").write(secrets)
        print("[CONFIG] ENV loaded...")
    except Exception as ex:
        print(ex)
        raise Exception("Error to load env config.")


def access_secret_version(project_id, project_environ, version_id="latest"):
    """Get secret valur of secret manager gcp."""
    credential = service_account.Credentials.from_service_account_file(
        f"src/configs/credential-gcp.json"
    )
    client = secretmanager.SecretManagerServiceClient(credentials=credential)
    name = f"projects/{project_id}/secrets/{project_environ}/versions/{version_id}"

    response = client.access_secret_version(name=name)
    secret_data = response.payload.data.decode("UTF-8")
    return secret_data


def get_all_crts_and_keys():
    """Save files of credential in dict memory."""
    files_required = [
        "list files download"
    ]
    files = {}
    for file in files_required:
        secret = access_secret_version("uoleti-staging", file)
        files[file] = secret
    print("[CONFIG] all files loaded...")
    return files
