from django.contrib import admin
from .models import Room, Player

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "n_to", "s_to", "e_to", "w_to")


admin.site.register(Room, RoomAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("user", "currentRoom", "uuid")


admin.site.register(Player, PlayerAdmin)
