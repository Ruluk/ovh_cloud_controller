from typing import List

import ovh

client = ovh.Client()


def create_instance(project_id: str, instance: dict):
    return client.post(f"/cloud/project/{project_id}/instance", **instance)


def get_backups(project_id: str):
    return client.get(f"/cloud/project/{project_id}/snapshot")


def get_flavors(project_id: str):
    return client.get(f"/cloud/project/{project_id}/flavor")


def get_ssh_keys(project_id: str) -> List[dict]:
    return client.get(f"/cloud/project/{project_id}/sshkey")
