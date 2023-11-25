from django.core.management.base import BaseCommand
from django.core.management import call_command
from ...models import Tag

class Command(BaseCommand):
    help = 'Create initial set of tags'

    def handle(self, *args, **options):
        default_tags = [
            'Arts and Sciences',
            'Career',
            'Club',
            'Concert',
            'Culture',
            'Education',
            'Engineering',
            'Food',
            'McIntire',
            'Religious',
            'Social',
            'Sports',
            'Theatre',
        ]

        for tag in default_tags:
            Tag.objects.get_or_create(name=tag)

        # Run migrate command to apply changes to the database
        call_command('migrate', *args, **options)
