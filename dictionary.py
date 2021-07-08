monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv", "Not a valid key"))