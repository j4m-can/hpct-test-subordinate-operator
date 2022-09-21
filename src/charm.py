#!/usr/bin/env python3
# Copyright 2022 John
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from ops.main import main

from hpctlib.interface.relation import interface_registry
from hpctlib.misc import service_forced_update
from hpctlib.ops.charm.service import ServiceCharm

# from hpctlib.interface import interface_registry


logger = logging.getLogger(__name__)


class HpctTestSubordinateCharm(ServiceCharm):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)

        self.framework.observe(
            self.on.test_ready_relation_joined, self._on_test_ready_relation_joined
        )

        # superinterface
        self.readysi = interface_registry.load("relation-subordinate-ready", self, "test-ready")

        # syncs and handlers
        self.service_init_sync("test-ready", False, self._sync_handler)

    def _service_start(self, event):
        self.service_set_sync("test-ready", True)

    @service_forced_update("config-changed")
    def _on_test_ready_relation_joined(self, event):
        key = "test-ready"
        self.service_set_sync(key)

    def _sync_handler(self, key, value):
        match key:
            case "test-ready":
                readyi = self.readysi.select(self.unit)
                readyi.status = self.service_get_sync(key)


if __name__ == "__main__":
    main(HpctTestSubordinateCharm)
