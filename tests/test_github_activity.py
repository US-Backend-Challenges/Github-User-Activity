import json
from click.testing import CliRunner
from main import cli
import requests_mock
from pathlib import Path

def test_github_activity():
    runner = CliRunner()
  
    THIS_DIR = Path(__file__).parent
    mock_data = json.loads((THIS_DIR / "mock.json").read_text())

    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/users/kamranahmedse/events", json=mock_data)

        result = runner.invoke(cli, ["github-activity", "kamranahmedse"])

    assert result.exit_code == 0
    # assert "6323174530" in result.output
    # assert "PushEvent" in result.output
    assert "kamranahmedse/reminder" in result.output

def test_github_activity_error():
    runner = CliRunner()

    result = runner.invoke(cli, ["github-activity", "nonexistinguser"])

    assert "Connection error" in result.output or "Unexpected error" in result.output