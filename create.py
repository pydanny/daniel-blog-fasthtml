from datetime import datetime
from pathlib import Path

from rich.prompt import Prompt, Confirm
from yaml import safe_dump

def main() -> None:
    while True:
        title: str = Prompt.ask("Title")
        if title:
            break
    while True:        
        description: str = Prompt.ask("Description")
        if description:
            break
    timestamp: str = Prompt.ask("Timestamp", default=datetime.now().isoformat()) 
    prefix: str = timestamp[:4]
    til: str = Confirm.ask("TIL")
    slug: str = Prompt.ask("Slug", default=f"{timestamp[:7]}-{title.lower().replace(' ', '-')}")

    data = {'published': True, 'description': description, 'date': timestamp, 'tags': []}

    data['title'] = title
    if til:
        data['title'] = f"TIL: {title}"
        slug = f"til-{slug}"
        data['tags'] = ['TIL', ]
        data["image"] = "/public/logos/til-1.png"
        data["twitter_image"] = "/public/logos/til-1.png"
        prefix = 'til'
    path = Path(f"posts/{prefix}/{slug}.md")
    text = f"---\n{safe_dump(data)}---\n"
    if description:
        text += f"\n\n_{description}_"
    path.write_text(text)

if __name__ == '__main__':
    main()