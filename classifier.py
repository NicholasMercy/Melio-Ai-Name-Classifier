def classify_name(name):

    name = name.lower()

   if any(keyword in name for keyword in ["university", "college", "institute", "school"]):
        return "University"
   
    elif any(keyword in name for keyword in ["inc", "ltd", "llc", "corp", "technologies", "solutions"]):
        return "Company"

    else:
        return "Person"