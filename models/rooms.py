# -*- coding: utf-8 -*-

#roomtypes.py

from odoo import models, fields, api
class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'rooms masterlist'
    _order="name"

    name = fields.Char("Rooms")
    description = fields.Char("Description")
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")

    roomtypename=fields.Char("Room Type",related='roomtype_id.name')