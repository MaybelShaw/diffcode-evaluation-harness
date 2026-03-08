EXECUTOR_REGISTRY = {}


def register_executor(language):
    def decorator(cls):
        EXECUTOR_REGISTRY[language] = cls
        return cls
    return decorator


def get_executor(language):
    if language not in EXECUTOR_REGISTRY:
        raise ValueError("No executor registered for language {}".format(language))
    return EXECUTOR_REGISTRY[language]()
