from django.contrib import admin
from .models import CricketPlayer, CricketTeam, Users,Challenges, PlayerEleven, BowlingLineUp

# Register your models here.
admin.site.register(CricketPlayer)
admin.site.register(CricketTeam)
admin.site.register(Users)
admin.site.register(Challenges)
admin.site.register(PlayerEleven)
admin.site.register(BowlingLineUp)