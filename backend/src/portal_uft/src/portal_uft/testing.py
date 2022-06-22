from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import portal_uft


class PORTAL_UFTLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=portal_uft)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "portal_uft:default")
        applyProfile(portal, "portal_uft:initial")


PORTAL_UFT_FIXTURE = PORTAL_UFTLayer()


PORTAL_UFT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PORTAL_UFT_FIXTURE,),
    name="PORTAL_UFTLayer:IntegrationTesting",
)


PORTAL_UFT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PORTAL_UFT_FIXTURE, WSGI_SERVER_FIXTURE),
    name="PORTAL_UFTLayer:FunctionalTesting",
)


PORTAL_UFTACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PORTAL_UFT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="PORTAL_UFTLayer:AcceptanceTesting",
)
