from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
                 description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_river = Room(title="Shaky Bridge", description="""The deep river flows from north 
to east. The cold breeze chills the air.""")

r_lava = Room(title="Lava Pit",
              description="""You get stuck in a pit of molten lava, better find a way out fast.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")


r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_river.save()
r_lava.save()
r_narrow.save()
r_treasure.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_narrow.connectRooms(r_river, "e")
r_river.connectRooms(r_narrow, "w")

r_river.connectRooms(r_lava, "n")
r_lava.connectRooms(r_river, "s")


players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()
