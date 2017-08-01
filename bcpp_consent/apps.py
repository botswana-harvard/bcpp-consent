from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap


ANONYMOUS_CONSENT_GROUP = 'anonymous'


class AppConfig(DjangoAppConfig):
    name = 'bcpp_consent'
    anonymous_consent_group = ANONYMOUS_CONSENT_GROUP
#     subject_types = [
#         SubjectType('subject', 'Research Subject',
#                     Cap(model_name='bcpp_subject.subjectconsent', max_subjects=14999)),
#     ]


if settings.APP_NAME == 'bcpp_consent':

    from dateutil.tz.tz import gettz
    from datetime import datetime
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP066'
        protocol_number = '066'
        protocol_name = 'BCPP'
        protocol_title = 'Botswana Combination Prevention Project'
        subject_types = [
            SubjectType('subject', 'Research Subject',
                        Cap(model_name='bcpp_subject.subjectconsent', max_subjects=14999)),
            SubjectType('subject', 'Research Subject',
                        Cap(model_name='bcpp_subject.anonymousconsent', max_subjects=9999)),
        ]
        study_open_datetime = datetime(
            2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

#         @property
#         def site_name(self):
#             from edc_map.site_mappers import site_mappers
#             return site_mappers.current_map_area
#
#         @property
#         def site_code(self):
#             from edc_map.site_mappers import site_mappers
#             return site_mappers.current_map_code
