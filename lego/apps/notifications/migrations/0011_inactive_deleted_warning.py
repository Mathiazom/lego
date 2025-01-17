from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0010_auto_20200221_2137"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationsetting",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("weekly_mail", "weekly_mail"),
                    ("event_bump", "event_bump"),
                    ("event_admin_registration", "event_admin_registration"),
                    ("event_admin_unregistration", "event_admin_unregistration"),
                    ("event_payment_overdue", "event_payment_overdue"),
                    ("event_payment_overdue_creator", "event_payment_overdue_creator"),
                    ("meeting_invite", "meeting_invite"),
                    ("penalty_creation", "penalty_creation"),
                    ("restricted_mail_sent", "restricted_mail_sent"),
                    ("company_interest_created", "company_interest_created"),
                    ("comment", "comment"),
                    ("comment_reply", "comment_reply"),
                    ("announcement", "announcement"),
                    ("survey_created", "survey_created"),
                    ("registration_reminder", "registration_reminder"),
                    ("inactive_warning", "inactive_warning"),
                    ("deleted_warning", "deleted_warning"),
                ],
                max_length=64,
            ),
        ),
    ]
