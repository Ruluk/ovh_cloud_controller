import provider

project_id = "cf542abba8324af5b07aa54d2b91fa31"
backup_prefix = "big-blue"
region = "BHS5"
instance_model = "b2-15"


def create_instance_from_backup(backup: dict, flavor_id: str, ssh_key: str):
    provider.create_instance(project_id, {
        "flavorId": flavor_id,
        "sshKeyId": ssh_key,
        "imageId": backup["id"],
        "name": backup["name"].split(" ")[0],
        "region": backup["region"],
    })


def delete_all_instances():
    instances = provider.get_all_instances(project_id)

    for instance in instances:
        print("deleting instance", instance)
        provider.delete_instance(project_id, instance)


def get_latest_backup(prefix: str):
    backups = provider.get_backups(project_id)
    filtered_backups = [backup for backup in backups if backup["name"].startswith(prefix)]
    return filtered_backups[0]


def get_optimal_flavor_id() -> str:
    flavors = provider.get_flavors(project_id)
    filtered_flavors = [flavor["id"] for flavor in flavors if
                        flavor["region"] == region and flavor["name"] == instance_model]
    return filtered_flavors[0]


def get_ssh_key() -> str:
    return provider.get_ssh_keys(project_id)[0]["id"]


def main():
    flavor_id = get_optimal_flavor_id()
    ssh_key = get_ssh_key()
    backup = get_latest_backup(backup_prefix)
    create_instance_from_backup(backup, flavor_id, ssh_key)


if __name__ == '__main__':
    main()
    # delete_all_instances()
