import requests
import click
from copy import deepcopy
from gui import GUI, rich_error

actions = {
    "CommitCommentEvent": {
        "created": 0
    },
    "CreateEvent": 0,
    "DeleteEvent": 0,
    "DiscussionEvent": {
        "created": 0
    },
    "ForkEvent": {
        "forked": 0
    },
    "GollumEvent": 0,
    "IssueCommentEvent": {
        "created": 0,
    },
    "IssuesEvent": {
        "opened": 0,
        "closed": 0,
        "reopened": 0
    },
    "MemberEvent": {
        "added": 0
    },
    "PublicEvent": 0,
    "PullRequestEvent": {
        "opened": 0,
        "closed": 0,
        "reopened": 0,
        "assigned": 0,
        "unassigned": 0,
        "labeled": 0,
        "unlabeled": 0,
    },
    "PullRequestReviewEvent": {
        "created": 0,
        "updated": 0,
        "dismissed": 0
    },
    "PullRequestReviewCommentEvent": {
        "created": 0
    },
    "PushEvent": 0,
    "ReleaseEvent": {
        "published": 0
    },
    "WatchEvent": {
        "started": 0
    }
}

@click.group()
def cli() -> None:
    pass

@click.command("github-activity")
@click.argument("username")
def github_activity(username: str) -> None:
    api = f"https://api.github.com/users/{username}/events"
    repositories = {}

    try:
        response = requests.get(api)

        events = response.json()

        for event in events:
            repository = event["repo"]["name"]
            
            if repository not in repositories:
                repositories[repository] = {
                    "repository": repository,
                    "actions": deepcopy(actions)
                }
            

            if isinstance(repositories[repository]["actions"][event["type"]], dict):
                repositories[repository]["actions"][event["type"]][event["payload"]["action"]] += 1
            else:
                repositories[repository]["actions"][event["type"]] += 1
            
        for repository in repositories:
            GUI(repositories[repository])
    except requests.exceptions.RequestException as e:
        rich_error(f"Connection error: {e}")
    except Exception as e:
        rich_error(f"Unexpected error: {e}")

cli.add_command(github_activity)

if __name__ == "__main__":
    cli()  