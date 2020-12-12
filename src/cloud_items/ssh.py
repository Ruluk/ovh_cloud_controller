import src.provider as provider


def get_key(project_id: str) -> str:
    return provider.get_ssh_keys(project_id)[0]["id"]
