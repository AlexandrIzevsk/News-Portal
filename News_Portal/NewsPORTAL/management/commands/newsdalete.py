from django.core.management.base import BaseCommand, CommandError
from NewsPORTAL.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет новости и статьи выбранной категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы хотите удалить все новости и статьи категории {options["category"]}? yes/no ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(categorys=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Новости и статьи из категории {category.name} успешно удалены'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Новостей и статей категории {options["category"]} нет'))


