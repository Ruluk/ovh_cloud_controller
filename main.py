from src.cloud_controllers import instance

project_id = "cf542abba8324af5b07aa54d2b91fa31"
backup_prefix = "big-blue"
region = "BHS5"
instance_model = "b2-15"


def main():
    _, ip = instance.create_from_latest_backup(project_id, region, instance_model, backup_prefix)
    print(ip)


if __name__ == '__main__':
    main()
    # delete_all_instances()
