import os
from time import sleep

import pytest

from integrations_app.public import _PATH_EXAMPLES
from lightning.app.testing.testing import run_app_in_cloud


@pytest.mark.cloud
def test_payload_example_cloud() -> None:
    with run_app_in_cloud(os.path.join(_PATH_EXAMPLES, "app_payload")) as (_, _, fetch_logs, _):

        has_logs = False
        while not has_logs:
            for log in fetch_logs(["flow"]):
                if "Application End!" in log:
                    has_logs = True
            sleep(1)
