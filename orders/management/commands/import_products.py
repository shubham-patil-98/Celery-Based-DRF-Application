from django.core.management.base import BaseCommand
from orders.tasks import import_products_from_excel

class Command(BaseCommand):
    help = 'Import products from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='(e.g., /home/shubham/Celery_App/ecommerce/uploads/Product_data.xlsx)')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        import_products_from_excel.delay(file_path)
        self.stdout.write(self.style.SUCCESS('Task for importing products has been initiated.'))
