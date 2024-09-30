# project/app/api/crud.py

from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


# Utility function to create a new summary
async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


# Utility function to read the summary from the database
async def get(id: int) -> Union[dict, None]:
    # The values method is used to create a valuesQuery object that is executed with await
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


# Utility function to get all summaries from the database
async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
