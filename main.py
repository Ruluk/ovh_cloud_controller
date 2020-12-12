import backup
import instance
import provider

project_id = "cf542abba8324af5b07aa54d2b91fa31"
backup_prefix = "big-blue"
region = "BHS5"
instance_model = "b2-15"


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
    latest_backup = backup.get_latest_starting_with(project_id, backup_prefix)
    new_instance = instance.create_from_backup(project_id, latest_backup, flavor_id, ssh_key)
    ip = instance.find_ip(project_id, new_instance["id"])
    print(new_instance)
    print(ip)


if __name__ == '__main__':
    main()
    # delete_all_instances()
