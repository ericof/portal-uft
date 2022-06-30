"""Upgrades tests for this package."""
from parameterized import parameterized
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501
from Products.GenericSetup.upgrade import listUpgradeSteps

import unittest


class UpgradeStepIntegrationTest(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING
    profile = "portal_uft:default"

    def setUp(self):
        self.portal = self.layer["portal"]
        self.setup = self.portal["portal_setup"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def _match(self, item, source, dest):
        source, dest = tuple([source]), tuple([dest])
        return item["source"] == source and item["dest"] == dest

    def available_steps(self, src: str, dst: str) -> list:
        """Test available steps."""
        steps = listUpgradeSteps(self.setup, self.profile, src)
        steps = [s for s in steps if self._match(s[0], src, dst)]
        return steps

    @parameterized.expand(
        [
            ("20220622001", "20220622002", 1),
            ("20220622002", "20220622003", 1),
            ("20220622003", "20220623001", 1),
            ("20220623001", "20220623002", 1),
            ("20220623002", "20220623003", 1),
            ("20220623003", "20220629001", 1),
            ("20220629001", "20220630001", 1),
            ("20220630001", "20220630002", 1),
        ]
    )
    def test_available(self, src, dst, expected):
        """Test upgrade step is available."""
        steps = self.available_steps(src, dst)
        self.assertEqual(len(steps), expected)
