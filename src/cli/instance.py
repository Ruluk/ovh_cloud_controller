from src.cloud_controllers import instance
from src.cloud_items import instance as instance_item

from .config import _get_project_id, _get_region, _get_instance_model

commands = {
    "create-from-latest-backup": lambda opts, arg:
    print(instance.create_from_latest_backup(_get_project_id(), _get_region(opts), _get_instance_model(opts), arg)[1]),

    "delete": lambda opts, arg:
    instance_item.delete(_get_project_id(), arg),

    "wait-ready": lambda opts, arg:
    instance_item.wait_ready(_get_project_id(), arg),
}
