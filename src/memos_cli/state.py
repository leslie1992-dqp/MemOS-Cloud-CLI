"""Process-local runtime state for MemOS CLI."""
from __future__ import annotations

from dataclasses import dataclass

from memos_cli.config import MemOSConfig


@dataclass
class RuntimeOptions:
    """Global options resolved at the CLI entrypoint."""

    agent_mode: bool = False
    api_key: str | None = None
    base_url: str | None = None


_runtime_options = RuntimeOptions()


def is_agent_mode() -> bool:
    """Check if running in agent mode."""
    return _runtime_options.agent_mode


def set_runtime_options(
    *,
    agent_mode: bool | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
) -> None:
    """Update process-local runtime options."""
    global _runtime_options
    if agent_mode is not None:
        _runtime_options.agent_mode = agent_mode
    if api_key is not None:
        _runtime_options.api_key = api_key
    if base_url is not None:
        _runtime_options.base_url = base_url


def get_runtime_options() -> RuntimeOptions:
    """Return a snapshot of runtime options."""
    return RuntimeOptions(
        agent_mode=_runtime_options.agent_mode,
        api_key=_runtime_options.api_key,
        base_url=_runtime_options.base_url,
    )


def apply_runtime_overrides(config: MemOSConfig) -> MemOSConfig:
    """Apply CLI global overrides to a loaded config object."""
    updated = config.model_copy(deep=True)
    if _runtime_options.api_key:
        updated.platform.api_key = _runtime_options.api_key
    if _runtime_options.base_url:
        updated.platform.base_url = _runtime_options.base_url
    return updated
