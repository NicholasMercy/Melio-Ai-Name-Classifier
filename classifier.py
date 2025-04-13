def classify_name(name):
    name = name.lower()

    if any(keyword in name for keyword in ["university", "college", "institute", "school"]):
        return "University"

    elif any(keyword in name for keyword in ["inc", "ltd", "llc", "corp", "technologies", "solutions"]):
        return "Company"

    else:
        return "Person"


if __name__ == "__main__":
    test_names = [
        "Harvard University",
        "Google Inc",
        "Jane Doe",
        "Amazon LLC",
        "Stanford",
        "Dr. Emily Clark",
        "Tech Solutions Ltd",
        "Oxford College",
        "Michael Jordan"
    ]

    for name in test_names:
        label = classify_name(name)
        print(f"{name} → {label}")
