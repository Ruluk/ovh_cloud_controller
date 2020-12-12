from time import sleep

import src.provider as provider


def create_from_backup(project_id: str, backup: dict, flavor_id: str, ssh_key: str):
    return provider.create_instance(project_id, {
        "flavorId": flavor_id,
        "sshKeyId": ssh_key,
        "imageId": backup["id"],
        "name": backup["name"].split(" ")[0],
        "region": backup["region"],
    })


def delete(project_id: str, instance_name: str):
    instances = provider.get_all_instances(project_id)

    for instance in instances:
        if instance["name"] == instance_name:
            print("deleting instance", instance)
            provider.delete_instance(project_id, instance)
            break


def find_ip(project_id: str, instance_id: str) -> str:
    instance_ip = None

    while instance_ip is None:
        instance = provider.get_instance(project_id, instance_id)

        if len(instance["ipAddresses"]) > 0:
            instance_ip = instance["ipAddresses"][0]["ip"]

    return instance_ip


def wait_ready(project_id: str, instance_name: str):
    instance_ready = False
    instance_id = None
    print("Waiting for instance to be ready...")

    while instance_ready is False:
        if instance_id is None:
            instances = provider.get_all_instances(project_id)
            instance = [instance for instance in instances if instance["name"] == instance_name][0]
            instance_id = instance["id"]
        else:
            instance = provider.get_instance(project_id, instance_id)

        if instance["status"] == "ACTIVE":
            instance_ready = True
        else:
            print("Not ready yet. Trying again in 30 seconds.")
            sleep(30)
