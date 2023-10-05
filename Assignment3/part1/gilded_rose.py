# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            self.update_sulfuras(item)

        item.sell_in -= 1  # Decrease sell_in for all items

        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name.find("Conjured"):
            self.update_conjured_item(item)
        else:
            self.update_normal_item(item)
            
        # quality of item is never negative
        item.quality = max(0, item.quality)

    def update_sulfuras(self, item):
        item.quality = 80 # sulfuras quality should be 80 at all times
        
    def update_aged_brie(self, item):
        item.quality = min(50, item.quality + 1)

    def update_backstage_passes(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in <= 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

    def update_conjured_item(self, item):
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)
    def update_normal_item(self, item):
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)