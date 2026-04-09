from dataclasses import dataclass, field
from typing import Dict


@dataclass(frozen=True)
class AppConfig:
    MODEL_ID: str = "immrass/pro_news_classifier"

    TOP_P_THRESHOLD: float = 0.95
    MAX_LENGTH: int = 128
    APP_TITLE: str = "News Intelligence Engine"
    LABELS_MAP: Dict[int, str] = field(
        default_factory=lambda: {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}
    )
