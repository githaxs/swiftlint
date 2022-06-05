import os

events = [
    {
        "pull_request": {
            "head": {
                "ref": "GabeL7r-patch-9",
                "sha": "010313d956959cc081fc08e00e5e53b22222c0a3",
            },
            "commits": 468,
        },
        "repository": {"full_name": "githaxs/test"},
        "githaxs": {
            "token": os.getenv("GITHUB_TOKEN"),
            "subscription_level": 5,
            "task_settings": {},
            "full_event_name": "pull_request.opened",
        },
    }
]
