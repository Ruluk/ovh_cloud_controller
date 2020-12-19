from typing import List, Tuple, Optional

_default_instance_model = "s1-2"
_default_region = "BHS5"


def _find_option(opts: List[Tuple[str, str]], opt_name: str) -> Optional[str]:
    for opt, value in opts:
        if opt == opt_name:
            return value


def _get_instance_model(opts) -> str:
    model = _find_option(opts, "--instance-model")
    return model or _default_instance_model


def _get_project_id() -> str:
    file = open("ovh.conf")

    for line in file:
        if line.startswith("project_id"):
            return line.split("=")[1]
    else:
        raise FileNotFoundError("ovh.conf file needs to define the project_id")


def _get_region(opts) -> str:
    region = _find_option(opts, "--region")
    return region or _default_region
