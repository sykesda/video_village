# DAS added Pi.__str__()

from django.db import models


class Pi(models.Model):
    mac_address = models.CharField(max_length=255)

    def __str__(self):
        return "Pi {}: {}".format(self.id, self.mac_address)
