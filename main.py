from src import provider
from src.cloud_items import backup, instance

project_id = "cf542abba8324af5b07aa54d2b91fa31"
backup_prefix = "big-blue"
region = "BHS5"
instance_model = "b2-15"


def create_instance_from_latest_backup(backup_prefix: str):
    flavor_id = get_optimal_flavor_id()
    ssh_key = get_ssh_key()
    latest_backup = backup.get_latest_starting_with(project_id, backup_prefix)
    new_instance = instance.create_from_backup(project_id, latest_backup, flavor_id, ssh_key)
    ip = instance.find_ip(project_id, new_instance["id"])
    print(new_instance)
    print(ip)


def get_optimal_flavor_id() -> str:
    flavors = provider.get_flavors(project_id)
    filtered_flavors = [flavor["id"] for flavor in flavors if
                        flavor["region"] == region and flavor["name"] == instance_model]
    return filtered_flavors[0]


def get_ssh_key() -> str:
    return provider.get_ssh_keys(project_id)[0]["id"]


def main():
    create_instance_from_latest_backup(backup_prefix)


if __name__ == '__main__':
    main()
    # delete_all_instances()
