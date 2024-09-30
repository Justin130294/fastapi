# project/app/models/tortoise.py

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


# Need to create a Pydantic model from the Tortoise model since TextSummary is a Tortoise model
SummarySchema = pydantic_model_creator(TextSummary)
