from datetime import timedelta

from django.utils import timezone

from lego.apps.events.constants import PRESENT
from lego.apps.events.models import Event, Registration
from lego.apps.events.tests.utils import get_dummy_users
from lego.apps.users.models import AbakusGroup, User
from lego.utils.test_utils import BaseTestCase


class DeleteUserTestCase(BaseTestCase):
    fixtures = [
        "test_abakus_groups.yaml",
        "test_companies.yaml",
        "test_users.yaml",
        "test_events.yaml",
    ]

    def setUp(self):
        Event.objects.all().update(
            start_time=timezone.now() + timedelta(hours=3),
            merge_time=timezone.now() + timedelta(hours=12),
        )

    #    def test_delete_user_soft(self):

    def test_delete_user_registration_not_present(self):
        #        event = Event.objects.get(title="POOLS_WITH_REGISTRATIONS")
        #        event_id = event.id
        #        user_id = event.registrations.all().first().user.id
        #        no_of_regs_before = event.number_of_registrations
        #        User.objects.get(id=user_id).delete(force=True)
        #        self.assertEqual(event.number_of_registrations, no_of_regs_before - 1)
        #        self.assertEqual(len(Event.objects.all().filter(id=event_id)), 1)
        #        self.assertEqual(len(User.objects.all().filter(id=user_id)), 0)
        #        event = Event.objects.get(title="POOLS_NO_REGISTRATIONS")
        #        event_id = event.id
        event = Event.objects.get(title="POOLS_NO_REGISTRATIONS")
        event_id = event.id
        users = get_dummy_users(4)
        for user in users:
            AbakusGroup.objects.get(name="Abakus").add_user(user)
            registration = Registration.objects.get_or_create(event=event, user=user)[0]
            event.register(registration)

        registration = event.registrations.all().first()
        precence = registration.precence
        self.assertNotEqual(precence, PRESENT)

        user_id = registration.user.id
        no_of_regs_before = event.number_of_registrations
        no_of_waiting_registrations_before = event.waiting_registrations.count()
        self.assertEqual(no_of_waiting_registrations_before, 1)

        User.objects.get(id=user_id).delete(force=True)
        no_of_waiting_registrations_after = event.waiting_registrations.count()
        self.assertEqual(no_of_waiting_registrations_after, 0)
        self.assertEqual(event.number_of_registrations, no_of_regs_before - 1)
        self.assertEqual(len(Event.objects.all().filter(id=event_id)), 1)
        self.assertEqual(len(User.objects.all().filter(id=user_id)), 0)


#    def test_delete_user_registration_not_present(self):

#    def test_delete_user_registration_present(self):
