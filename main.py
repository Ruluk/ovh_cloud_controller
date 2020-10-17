import json

import provider

project_id = "cf542abba8324af5b07aa54d2b91fa31"
region = "BHS5"
instance_model = "b2-15"


def get_optimal_flavor_id() -> str:
    flavors = provider.get_flavors(project_id)
    filtered_flavors = list(filter(
        lambda flavor: flavor["region"] == region and flavor["name"] == instance_model,
        flavors))
    return filtered_flavors[0]["id"]


def get_latest_backup():
    backups = provider.get_backups(project_id)
    return backups[0]


def create_instance_from_backup(backup: dict, flavor_id: str):
    provider.create_instance(project_id, {
        "flavorId": flavor_id,
    })


if __name__ == '__main__':
    print("Welcome", client.get('/me'))
