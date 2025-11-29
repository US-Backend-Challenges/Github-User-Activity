from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.padding import Padding
from rich import box

console = Console()

def GUI(repository):
    name = repository["repository"]
    title = Text(name, style="bold cyan")
    lines = []

    a = repository["actions"]

    if a["CommitCommentEvent"]["created"] > 0:
        lines.append(f"✍️ Commited {a['CommitCommentEvent']['created']} comment(s) in {name}")

    if a["CreateEvent"] > 0:
        lines.append(f"✨ Created {a['CreateEvent']} branches/tags in {name}")

    if a["DeleteEvent"] > 0:
        lines.append(f"🗑️ Deleted {a['DeleteEvent']} branches/tags in {name}")

    if a["DiscussionEvent"]["created"] > 0:
        lines.append(f"💭 Created {a['DiscussionEvent']['created']} discussions in {name}")

    if a["ForkEvent"]["forked"] > 0:
        lines.append(f"🍴 Forked {a['ForkEvent']['forked']} in {name}")

    if a["GollumEvent"] > 0:
        lines.append(f"📘 {a['GollumEvent']} wiki pages updated in {name}")

    if a["IssueCommentEvent"]["created"] > 0:
        lines.append(f"💬 {a['IssueCommentEvent']['created']} issue(s) comments in {name}")

    if a["IssuesEvent"]["opened"] > 0:
        lines.append(f"🐛 Opened {a['IssuesEvent']['opened']} issue(s) in {name}")
    if a["IssuesEvent"]["closed"] > 0:
        lines.append(f"🛠️ Closed {a['IssuesEvent']['closed']} issue(s) in {name}")
    if a["IssuesEvent"]["reopened"] > 0:
        lines.append(f"🔄 Reopened {a['IssuesEvent']['reopened']} issue(s) in {name}")

    if a["MemberEvent"]["added"] > 0:
        lines.append(f"👤 Added {a['MemberEvent']['added']} collaborators in {name}")

    if a["PublicEvent"] > 0:
        lines.append(f"🌍 Made {name} public")

    if a["PullRequestEvent"]["opened"] > 0:
        lines.append(f"📥 Opened {a['PullRequestEvent']['opened']} pull request(s) in {name}")
    if a["PullRequestEvent"]["closed"] > 0:
        lines.append(f"📕 Closed {a['PullRequestEvent']['closed']} pull request(s) in {name}")
    if a["PullRequestEvent"]["reopened"] > 0:
        lines.append(f"📗 Reopened {a['PullRequestEvent']['reopened']} pull request(s) in {name}")
    if a["PullRequestEvent"]["assigned"] > 0:
        lines.append(f"🎯 Assigned {a['PullRequestEvent']['assigned']} pull request(s) in {name}")
    if a["PullRequestEvent"]["unassigned"] > 0:
        lines.append(f"🚫 Unassigned {a['PullRequestEvent']['unassigned']} pull request(s) in {name}")
    if a["PullRequestEvent"]["labeled"] > 0:
        lines.append(f"🏷️ Labeled {a['PullRequestEvent']['labeled']} pull request(s) in {name}")
    if a["PullRequestEvent"]["unlabeled"] > 0:
        lines.append(f"❌🏷️ Unlabeled {a['PullRequestEvent']['unlabeled']} pull request(s) in {name}")

    if a["PullRequestReviewEvent"]["created"] > 0:
        lines.append(f"👀 Created {a['PullRequestReviewEvent']['created']} review(s) in {name}")
    if a["PullRequestReviewEvent"]["updated"] > 0:
        lines.append(f"🔧 Updated {a['PullRequestReviewEvent']['updated']} review(s) in {name}")
    if a["PullRequestReviewEvent"]["dismissed"] > 0:
        lines.append(f"❌ Dismissed {a['PullRequestReviewEvent']['dismissed']} review(s) in {name}")

    if a["PullRequestReviewCommentEvent"]["created"] > 0:
        lines.append(f"📝 Review comments created {a['PullRequestReviewCommentEvent']['created']} in {name}")

    if a["PushEvent"] > 0:
        lines.append(f"📌 Push {a['PushEvent']} commits to {name}")

    if a["ReleaseEvent"]["published"] > 0:
        lines.append(f"🚀 {a['ReleaseEvent']['published']} releases published in {name}")

    if a["WatchEvent"]["started"] > 0:
        lines.append(f"⭐ Starred {name}")

    body = "\n".join(lines)

    panel = Panel(
        Padding(body, (1, 2)),
        title=title,
        border_style="bright_blue",
        box=box.ROUNDED,
        expand=True
    )

    console.print(panel)

def rich_error(message: str):
    console.print(
        Panel(
            Text(message, style="bold red"),
            border_style="red",
            title="❌ Error",
            expand=False
        )
    )