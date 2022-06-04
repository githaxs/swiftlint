import os
from task_interfaces import StaticAnalysisTask, SubscriptionLevels


class Task(StaticAnalysisTask):
    """
    A tool to enforce Swift style and conventions.
    """

    name = "Swift Lint"
    subscription_level = SubscriptionLevels.STARTUP
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
