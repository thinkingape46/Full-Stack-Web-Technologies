def greet_func(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    print("my_module.py is being run directly")
else:
    print("my_module.py has been imported")