from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


class Task(TaskInterface):
    """
    A tool to enforce Swift style and conventions.
    """

    name = "Swift Lint"
    slug = "swift-lint "
    subscription_level = SubscriptionLevels.FREE
    actions = None

    # For code format tasks, specify if they can automatically fix errors.
    # If they can there will be a button for users to click in github ui.
    can_fix = False

    # Valid types include:
    # CODE_FORMAT: clones the repo and runs shell scripts against the contents
    # CODE_ANALYSIS: not used
    # WORKFLOW: only works with meta data from the webhook, i.e. repo not cloned
    # DEPLOY: still experimental - runs in ECS
    # UNIT_TEST: still experimental - runs in ECS
    type = TaskTypes.FOO
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
    handler = "task"

    # Use the execute function if the task type is WORKFLOW
    def execute(self, github_body, settings) -> bool:
        pass
