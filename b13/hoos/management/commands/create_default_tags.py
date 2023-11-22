from django.core.management.commands import makemigrations
from django.core.management.commands import migrate
from ...models import Tag

class CreateDefaultTagsCommand(makemigrations.Command):
    help = 'Create initial set of tags'

    def handle(self, *args, **options):
        default_tags = [
            'Career',
            'Club',
            'Arts and Sciences',
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
            Tag.objects.get_or_create(**{'name': tag})

        migrate.Command().handle(*args, **options)
