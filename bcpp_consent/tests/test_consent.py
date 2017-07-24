from django.test import TestCase
from edc_consent.site_consents import site_consents

from pprint import pprint


class TestConsent(TestCase):

    def test_consent(self):
        pprint(site_consents.registry)
