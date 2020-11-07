from typing import List

import ovh

client = ovh.Client()


def create_instance(project_id: str, instance: dict):
    return client.post(f"/cloud/project/{project_id}/instance", **instance)


def delete_instance(project_id: str, instance: dict):
    return client.delete(f"/cloud/project/{project_id}/instance/{instance['id']}")


def get_all_instances(project_id: str) -> List[dict]:
    return client.get(f"/cloud/project/{project_id}/instance")


def get_instance(project_id: str, instance_id: str) -> dict:
    return client.get(f"/cloud/project/{project_id}/instance/{instance_id}")


def get_backups(project_id: str):
    return client.get(f"/cloud/project/{project_id}/snapshot")


def get_flavors(project_id: str):
    return client.get(f"/cloud/project/{project_id}/flavor")


def get_ssh_keys(project_id: str) -> List[dict]:
    return client.get(f"/cloud/project/{project_id}/sshkey")
