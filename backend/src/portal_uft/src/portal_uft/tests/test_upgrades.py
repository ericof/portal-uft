"""Upgrades tests for this package."""
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501
from Products.GenericSetup.upgrade import listUpgradeSteps

import unittest


class UpgradeStepIntegrationTest(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING
    profile = "portal_uft:default"
    src = ""
    dst = ""
    steps = 1

    def setUp(self):
        self.portal = self.layer["portal"]
        self.setup = self.portal["portal_setup"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def _match(self, item, source, dest):
        source, dest = tuple([source]), tuple([dest])
        return item["source"] == source and item["dest"] == dest

    def available_steps(self) -> list:
        """Test available steps."""
        steps = listUpgradeSteps(self.setup, self.profile, self.src)
        steps = [s for s in steps if self._match(s[0], self.src, self.dst)]
        return steps

    def test_available(self):
        """Test upgrade step is available."""
        if self.src and self.dst:
            steps = self.available_steps()
            self.assertEqual(len(steps), 1)


class V20220622001UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220622001."""

    src = "20220622001"
    dst = "20220622002"
    steps = 1


class V20220622002UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220622002."""

    src = "20220622002"
    dst = "20220622003"
    steps = 1


class V20220622003UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220622003."""

    src = "20220622003"
    dst = "20220623001"
    steps = 1


class V20220623001UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220623001."""

    src = "20220623001"
    dst = "20220623002"
    steps = 1


class V20220623002UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220623002."""

    src = "20220623002"
    dst = "20220623003"
    steps = 1


class V20220623003UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220623003."""

    src = "20220623003"
    dst = "20220629001"
    steps = 1


class V20220629001UpgradeTest(UpgradeStepIntegrationTest):
    """Test upgrade step from version 20220629001."""

    src = "20220629001"
    dst = "20220630001"
    steps = 1
