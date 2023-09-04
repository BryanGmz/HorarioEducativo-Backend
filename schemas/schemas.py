from pydantic import BaseModel
from typing import Optional
from datetime import time

class GenerateSchedule(BaseModel):
    start_time:time
    end_time:time
    time_frame:time