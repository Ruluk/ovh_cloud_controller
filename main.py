from src.cloud_items import backup, instance, flavor, ssh

project_id = "cf542abba8324af5b07aa54d2b91fa31"
backup_prefix = "big-blue"
region = "BHS5"
instance_model = "b2-15"


def create_instance_from_latest_backup(backup_prefix: str):
    flavor_id = flavor.get_optimal_id(project_id, region, instance_model)
    ssh_key = ssh.get_key(project_id)
    latest_backup = backup.get_latest_starting_with(project_id, backup_prefix)
    new_instance = instance.create_from_backup(project_id, latest_backup, flavor_id, ssh_key)
    ip = instance.find_ip(project_id, new_instance["id"])
    print(new_instance)
    print(ip)


def main():
    create_instance_from_latest_backup(backup_prefix)


if __name__ == '__main__':
    main()
    # delete_all_instances()
