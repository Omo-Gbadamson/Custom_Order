from datetime import datetime
from .db import db
# from .db import gend




class CustomOrder(db.Document):
    product_category_id = db.StringField(required=True)
    product_sub_category_id = db.StringField()
    gender = db.StringField(choices=[(1,"Male"), (2,"Female")])
    size = db.StringField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta ={
        "ordering": ["-created_at"]
    }

class Measurement(db.Document):
    customer_order_id = db.StringField(required=True)
    shoulder = db.IntField()
    hand_length = db.IntField()
    chest_bust = db.IntField()
    stomach = db.IntField()
    top_length = db.IntField()
    round_arm = db.IntField()
    waist = db.IntField()
    tight = db.IntField()
    knee = db.IntField()
    around_leg = db.IntField()
    leg_length = db.IntField()
    size = db.IntField()
    other_info = db.StringField()
    created_at = db.DateTimeField()

    meta = {
        "ordering" : ["-created_at"]
    }