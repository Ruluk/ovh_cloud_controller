from typing import Tuple

from src.cloud_items import flavor, ssh, backup, instance


def create_from_latest_backup(
        project_id: str, region: str, instance_model: str, backup_prefix: str) -> Tuple[object, str]:
    flavor_id = flavor.get_optimal_id(project_id, region, instance_model)
    ssh_key = ssh.get_key(project_id)
    latest_backup = backup.get_latest_starting_with(project_id, backup_prefix)
    new_instance = instance.create_from_backup(project_id, latest_backup, flavor_id, ssh_key)
    ip = instance.find_ip(project_id, new_instance["id"])

    return new_instance, ip
