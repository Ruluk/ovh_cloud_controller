import src.provider as provider


def get_optimal_id(project_id: str, region: str, instance_model: str) -> str:
    flavors = provider.get_flavors(project_id)
    filtered_flavors = [flavor["id"] for flavor in flavors if
                        flavor["region"] == region and flavor["name"] == instance_model]
    return filtered_flavors[0]
