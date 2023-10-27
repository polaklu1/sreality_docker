from scrapy import Field, Item


class SrealityItem(Item):
    """
    Scrapy Item blueprints
    """
    name = Field()
    locality = Field()
    image_url = Field()
