def greet(name):
    return f"Hello, {name}!"


def get_version():
    return "1.0.0"


if __name__ == "__main__":
    print(greet("CI/CD"))
    print(f"Version: {get_version()}")
