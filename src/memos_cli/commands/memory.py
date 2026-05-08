"""Typer entrypoints for memory operations."""
from __future__ import annotations

import typer

from memos_cli.commands.memory_cmd import cmd_add, cmd_delete, cmd_get, cmd_list, cmd_search


def add(
    text: str | None = typer.Argument(None, help="Text content to add as memory."),
    message: str | None = typer.Option(None, "--message", "-m", help="Text content to add."),
    user_id: str | None = typer.Option(None, "--user-id", help="User ID"),
    agent_id: str | None = typer.Option(None, "--agent-id", help="Agent ID"),
    app_id: str | None = typer.Option(None, "--app-id", help="App ID"),
    run_id: str | None = typer.Option(None, "--run-id", help="Run ID"),
    conversation_id: str | None = typer.Option(None, "--conversation-id", help="Conversation ID"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Add a new memory."""
    cmd_add(
        text,
        message=message,
        user_id=user_id,
        agent_id=agent_id,
        app_id=app_id,
        run_id=run_id,
        conversation_id=conversation_id,
        json_output=json_output,
    )


def search(
    query: str | None = typer.Argument(None, help="Search query"),
    query_option: str | None = typer.Option(None, "--query", "-q", help="Search query"),
    user_id: str | None = typer.Option(None, "--user-id", help="User ID"),
    agent_id: str | None = typer.Option(None, "--agent-id", help="Agent ID"),
    app_id: str | None = typer.Option(None, "--app-id", help="App ID"),
    run_id: str | None = typer.Option(None, "--run-id", help="Run ID"),
    conversation_id: str | None = typer.Option(None, "--conversation-id", help="Conversation ID"),
    limit: int = typer.Option(10, "--limit", "-n", min=1, help="Number of results"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Search memories."""
    cmd_search(
        query,
        query_option=query_option,
        user_id=user_id,
        agent_id=agent_id,
        app_id=app_id,
        run_id=run_id,
        conversation_id=conversation_id,
        limit=limit,
        json_output=json_output,
    )


def list(
    user_id: str | None = typer.Option(None, "--user-id", help="User ID"),
    limit: int | None = typer.Option(None, "--limit", "-n", min=1, help="Maximum memories to return"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """List memories."""
    cmd_list(user_id=user_id, limit=limit, json_output=json_output)


def get(
    memory_id: str = typer.Argument(..., help="Memory ID"),
    user_id: str | None = typer.Option(None, "--user-id", help="User ID"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Get a specific memory by ID."""
    cmd_get(memory_id, user_id=user_id, json_output=json_output)


def delete(
    memory_id: str = typer.Argument(..., help="Memory ID to delete"),
    user_id: str | None = typer.Option(None, "--user-id", help="User ID"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Delete a memory by ID."""
    cmd_delete(memory_id, user_id=user_id, json_output=json_output)
