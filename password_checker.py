import re
import getpass

password = getpass.getpass("Enter your password: ")
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome"
]

if password.lower() in common_passwords:
    print("\nWARNING: This is a commonly used password!")

score = 0
missing = []

if len(password) >= 8:
    score += 1
else:
    missing.append("Use at least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    missing.append("Add an uppercase letter")

if re.search(r"[a-z]", password):
    score += 1
else:
    missing.append("Add a lowercase letter")

if re.search(r"[0-9]", password):
    score += 1
else:
    missing.append("Add a number")

if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    missing.append("Add a special character")

percentage = score * 20

if score <= 2:
    level = "WEAK"
elif score <= 4:
    level = "MEDIUM"
else:
    level = "STRONG"

print("\n==============================")
print("     PASSWORD SECURITY CHECK")
print("==============================")
print("Strength :", str(percentage) + "%")
print("Level    :", level)
report = open("security_report.txt", "w")

report.write("PASSWORD SECURITY REPORT\n")
report.write("=======================\n")
report.write("Strength: " + str(percentage) + "%\n")
report.write("Level: " + level + "\n")

if missing:
    report.write("\nRecommendations:\n")
    for item in missing:
        report.write("- " + item + "\n")
else:
    report.write("\nAll basic requirements are satisfied.\n")

report.close()

print("\nSecurity report saved as security_report.txt")
if missing:
    print("\nRecommendations:")
    for item in missing:
        print("-", item)
else:
    print("\nExcellent! All basic requirements are satisfied.")