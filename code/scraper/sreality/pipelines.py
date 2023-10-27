from sqlalchemy.orm import sessionmaker
from scraper.sreality.models import Items, create_items_table, db_connect


class SrealityPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(Items).filter_by(**item).one_or_none()
        if instance:
            return instance
        sreality_item = Items(**item)

        try:
            session.add(sreality_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item