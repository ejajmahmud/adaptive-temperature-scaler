"""Core Adaptive Temperature Scaler implementation."""
import re
from typing import Dict, Any


class AdaptiveTemperatureScaler:
    def __init__(self, base_temp: float = 0.7, min_temp: float = 0.05, max_temp: float = 0.9):
        self.base_temp = base_temp
        self.min_temp = min_temp
        self.max_temp = max_temp

    def evaluate_target_temperature(self, context_text: str, task_type: str = "general") -> Dict[str, Any]:
        # Detect syntax-critical structures
        has_json = bool(re.search(r"(\{.*\}|\[.*\]|json|schema)", context_text, re.IGNORECASE))
        has_code = bool(re.search(r"(def |class |import |function |SELECT |WHERE |public class)", context_text))
        has_math = bool(re.search(r"(calculate|equation|sum|integral|proof|formula)", context_text, re.IGNORECASE))

        if has_json or has_code:
            target = self.min_temp
            category = "strict_syntax"
        elif has_math:
            target = 0.1
            category = "mathematical_reasoning"
        elif task_type == "brainstorm":
            target = self.max_temp
            category = "creative_expansion"
        else:
            target = self.base_temp
            category = "balanced_general"

        target = max(self.min_temp, min(self.max_temp, target))
        return {
            "recommended_temperature": round(target, 3),
            "category": category,
            "has_json_or_code": has_json or has_code,
            "has_math": has_math
        }
