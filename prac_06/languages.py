from programming_language import ProgrammingLanguage

def main():
    """Create and display information about different programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print each language's details
    print(python)
    print(ruby)
    print(visual_basic)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Find and print the languages with dynamic typing
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
