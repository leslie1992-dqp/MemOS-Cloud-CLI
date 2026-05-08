"""Initialization command for MemOS CLI."""
from __future__ import annotations

import typer
from rich.console import Console
from rich.prompt import Prompt

from memos_cli.config import (
    DEFAULT_CONVERSATION_ID,
    DEFAULT_USER_ID,
    MemOSConfig,
    PlatformConfig,
    save_config,
)
from memos_cli.backend.memos_api import APIError, AuthError, get_backend

console = Console()


def init_cmd(
    api_key: str | None = typer.Option(None, "--api-key", "-k", help="MemOS API key"),
    base_url: str | None = typer.Option(None, "--base-url", "-u", help="API base URL"),
    user_id: str | None = typer.Option(None, "--user-id", help="Default user ID"),
    conversation_id: str | None = typer.Option(
        None, "--conversation-id", help="Default conversation ID"
    ),
):
    """Initialize MemOS CLI with your API credentials."""
    console.print("[bold blue]◆ MemOS CLI Initialization[/]\n")
    
    # Get API key
    if not api_key:
        api_key = Prompt.ask(
            "[bold]Enter your MemOS API key[/]",
            password=True,
        )
    
    if not api_key:
        console.print("[red]Error:[/] API key is required")
        raise typer.Exit(1)
    
    # Get base URL (optional)
    if not base_url:
        base_url = Prompt.ask(
            "API base URL",
            default="https://memos.memtensor.cn/api/openmem/v1",
        )

    if not user_id:
        user_id = Prompt.ask(
            "Default user ID",
            default=DEFAULT_USER_ID,
        )

    if not conversation_id:
        conversation_id = Prompt.ask(
            "Default conversation ID",
            default=DEFAULT_CONVERSATION_ID,
        )
    
    # Create and save config
    config = MemOSConfig(
        platform=PlatformConfig(
            api_key=api_key,
            base_url=base_url,
        ),
    )
    config.defaults.user_id = user_id or DEFAULT_USER_ID
    config.defaults.conversation_id = conversation_id or DEFAULT_CONVERSATION_ID

    try:
        get_backend(config).ping()
    except AuthError as exc:
        console.print(f"\n[red]Authentication failed:[/] {exc}")
        raise typer.Exit(1)
    except APIError as exc:
        console.print(f"\n[red]API error:[/] {exc}")
        raise typer.Exit(1)
    except Exception as exc:
        console.print(f"\n[red]Error:[/] {exc}")
        raise typer.Exit(1)

    save_config(config)

    console.print("\n[green]✓[/] Configuration saved successfully!")
    console.print(f"  Config file: [dim]~/.memos/config.yaml[/]")
    console.print(f"  Default user ID: [dim]{config.defaults.user_id}[/]")
    console.print(f"  Default conversation ID: [dim]{config.defaults.conversation_id}[/]")
    console.print("\n[dim]Try running:[/] memos add -m \"Your first memory\"")
