"""Tests for adaptive-temperature-scaler."""
import unittest
from adaptive_temperature_scaler.scaler import AdaptiveTemperatureScaler


class TestScaler(unittest.TestCase):
    def setUp(self):
        self.scaler = AdaptiveTemperatureScaler()

    def test_code_clamp(self):
        res = self.scaler.evaluate_target_temperature("def calculate_fibonacci(n):")
        self.assertEqual(res["category"], "strict_syntax")
        self.assertLessEqual(res["recommended_temperature"], 0.1)

    def test_json_clamp(self):
        res = self.scaler.evaluate_target_temperature('Return response in {"status": "ok"} format')
        self.assertEqual(res["category"], "strict_syntax")
        self.assertLessEqual(res["recommended_temperature"], 0.1)

    def test_creative_expansion(self):
        res = self.scaler.evaluate_target_temperature("Tell a bedtime story", task_type="brainstorm")
        self.assertEqual(res["category"], "creative_expansion")
        self.assertGreaterEqual(res["recommended_temperature"], 0.7)
