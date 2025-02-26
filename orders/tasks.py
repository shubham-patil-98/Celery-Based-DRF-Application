from celery import shared_task
import pandas as pd
from .models import Product

@shared_task
def import_products_from_excel(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Validate required columns
        required_columns = {'product_name', 'amount'}
        if not required_columns.issubset(df.columns):
            return f"Invalid Excel file format. Missing columns: {required_columns - set(df.columns)}"

        # Process the rows
        for _, row in df.iterrows():
            # Check if product already exists using product_name
            if not Product.objects.filter(product_name=row['product_name']).exists():
                Product.objects.create(product_name=row['product_name'], amount=row['amount'])
        return f"Imported {len(df)} products successfully."
    except Exception as e:
        return f"Task failed: {str(e)}"
    
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def debug_task():
    logger.info("Debug task executed!")

