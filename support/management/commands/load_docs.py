from django.core.management.base import BaseCommand
from support.rag import load_documents, collection


class Command(BaseCommand):
    help = "Loads PDF documents from support/documents/ into ChromaDB"

    def handle(self, *args, **options):
        existing_count = collection.count()

        if existing_count > 0:
            self.stdout.write(
                self.style.WARNING(
                    f"Collection already has {existing_count} chunks — skipping to avoid duplicate IDs."
                )
            )
            return

        load_documents()
        self.stdout.write(self.style.SUCCESS("Documents loaded into ChromaDB."))