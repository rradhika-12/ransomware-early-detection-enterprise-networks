from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel


class NormalizedEvent(BaseModel):
    event_id: str
    timestamp: datetime
    source_type: str
    event_type: str
    host: Optional[str] = None
    user: Optional[str] = None
    process_name: Optional[str] = None
    file_path: Optional[str] = None
    src_ip: Optional[str] = None
    dst_ip: Optional[str] = None
    raw: Dict[str, Any] = {}