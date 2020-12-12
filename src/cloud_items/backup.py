from datetime import datetime

import src.provider as provider


def create_from_instance(project_id: str, instance_name: str) -> str:
    instances = provider.get_all_instances(project_id)

    for instance in instances:
        if instance["name"] == instance_name:
            provider.create_backup(project_id, instance["id"], f"{instance_name} {datetime.today().isoformat(' ')}")
            return instance["id"]
    else:
        return ""


def get_latest_starting_with(project_id: str, prefix: str):
    backups = provider.get_backups(project_id)
    filtered_backups = [backup for backup in backups if backup["name"].startswith(prefix)]
    return filtered_backups[0]
