# OVH Cloud Controller

CLI to control some elements of the OVH Public Cloud through its API.

## Setup

Before running the CLI, first, create a `ovh.conf` file in the root directory of the repository, including the project
ID. For example:

```toml
[default]
endpoint=ovh-ca

[ovh-ca]
application_key=abc123def456
application_secret=abc123def456abc123def456
consumer_key=<Will be filled by script>

[custom]
project_id=abc123def456abc123def456
```

Second, make sure you have `jq` installed.

Third, run `bash get_consumer_key.sh` to fill a new consumer key. It will require a web authentication.

Then, you're ready to go!

## CLI Usage

```bash
python main.py <command>
 
Available commands:
help

backup create-from-instance <instance-name>

instance create-from-latest-backup [--region=BHS5] [--instance-model=s1-2] <backup-prefix>
instance delete <instance-name>
instance wait-ready <instance-name>
```
