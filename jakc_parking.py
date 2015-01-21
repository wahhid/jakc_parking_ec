from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('done','Close'),
]


class park_vehicle_type(osv.osv):
    _name = "park.vehicle.type"
    _description = "Parking Vehicle Type"
    _columns = {
        'name': fields.char('Name', size=100),
        'state': fields.selection(AVAILABLE_STATES,size=16),
    }
park_vehicle_type()


class park_shift(osv.osv):
    _name = "park.shift"
    _description = "Parking Shift"
    _columns = {
        'name': fields.char('Name', size=100),
        'start_time': fields.float('Start Time'),
        'end_time': fields.float('End Time'),
        'state': fields.selection(AVAILABLE_STATES,size=16),
    }
park_shift()

class park_image_type(osv.osv):
    _name = "park.image.type"
    _description = "Parking Image Type"
    _columns = {
        'name': fields.char('Name',size=100),
    }    
park_image_type()
