"""CLI for adaptive-temperature-scaler."""
import sys
import argparse
from .scaler import AdaptiveTemperatureScaler


def main():
    parser = argparse.ArgumentParser(description="Adaptive Temperature Scaler")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        scaler = AdaptiveTemperatureScaler()
        prompt1 = "Generate a JSON schema for user registration"
        prompt2 = "Brainstorm 10 sci-fi movie plots about rogue satellites"
        print(f"Prompt 1: {scaler.evaluate_target_temperature(prompt1)}")
        print(f"Prompt 2: {scaler.evaluate_target_temperature(prompt2, task_type='brainstorm')}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
