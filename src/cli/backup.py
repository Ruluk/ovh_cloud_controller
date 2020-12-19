from src.cloud_items import backup

from .config import _get_project_id

commands = {
    "create-from-instance": lambda opts, arg:
    backup.create_from_instance(_get_project_id(), arg),
}
