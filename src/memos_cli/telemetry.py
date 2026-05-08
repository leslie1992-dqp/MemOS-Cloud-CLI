"""Telemetry reporting for MemOS CLI."""
from __future__ import annotations

import os
import json
import subprocess
from typing import Any


def capture_event(event_name: str, properties: dict[str, Any] | None = None) -> None:
    """Capture telemetry event (non-blocking, never fails)."""
    try:
        # Add source identifier
        if properties is None:
            properties = {}
        
        properties["source"] = "cli"
        
        # Detect framework if available
        framework = detect_framework()
        if framework:
            properties["framework"] = framework
        
        # TODO: Implement actual telemetry sending
        # For now, just log to file for debugging
        _log_event(event_name, properties)
        
    except Exception:
        pass


def detect_framework() -> str | None:
    """Detect which agent framework is calling the CLI."""
    if framework := os.getenv("MEMOS_FRAMEWORK"):
        return framework.strip().lower()

    if os.getenv("OPENCLAW_CONFIG"):
        return "openclaw"
    if os.getenv("HERMES_AGENT"):
        return "hermes"

    try:
        result = subprocess.run(
            ["ps", "-o", "command=", "-p", str(os.getppid())],
            check=False,
            capture_output=True,
            text=True,
        )
        cmdline = result.stdout.strip().lower()
        if "openclaw" in cmdline:
            return "openclaw"
        if "hermes" in cmdline:
            return "hermes"
    except Exception:
        pass

    return None


def _log_event(event_name: str, properties: dict) -> None:
    """Log event to local file for debugging."""
    try:
        from pathlib import Path
        log_dir = Path.home() / ".memos" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / "telemetry.log"
        event_data = {
            "event": event_name,
            "properties": properties,
        }
        
        with open(log_file, "a") as f:
            f.write(json.dumps(event_data) + "\n")
    except Exception:
        pass
