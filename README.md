
---

````markdown
# 🔐 Password Generator & Strength Checker – Python CLI Tool

## 🇬🇧 Description (English)

This is a simple yet functional CLI tool written in Python for generating secure passwords and evaluating their strength.

### 📦 Features

- Generate random passwords with options:
  - Uppercase letters
  - Symbols
  - Numbers
- Check the strength of any custom password:
  - Detects strong, moderate, average, weak, or very weak passwords
- Cross-platform terminal support (Windows/Linux/macOS)

### 💻 How to Use

```bash
python your_script_name.py
````

### 📋 Menu Options

```
[1] Generate a new password
[2] Check password strength
[3] Exit
```

### 📌 Notes

* Passwords are generated from customizable character pools.
* Strength checking is based on:

  * Length
  * Inclusion of uppercase, digits, and symbols

### 🧪 Example Output

```
>> 1
Password length: 16
Include uppercase? yes
Include numbers? yes
Include symbols? yes
Generated password: q2T!vsY8$@Wnm%K9
```

```
>> 2
Enter your password: password123
password is weak
```

---

## 🇩🇪 Beschreibung (Deutsch)

Dies ist ein einfaches, aber nützliches CLI-Tool in Python zum Erstellen sicherer Passwörter und zur Überprüfung ihrer Stärke.

### 📦 Funktionen

* Generierung von Passwörtern mit Auswahloptionen:

  * Großbuchstaben
  * Sonderzeichen
  * Zahlen
* Passwortstärke prüfen:

  * Erkennung von starken, mittleren oder schwachen Passwörtern
* Plattformübergreifende Unterstützung für Terminale (Windows/Linux/macOS)

### 💻 Verwendung

```bash
python dein_script_name.py
```

### 📋 Menüoptionen

```
[1] Neues Passwort generieren
[2] Passwortstärke prüfen
[3] Beenden
```

### 📌 Hinweise

* Passwörter werden aus wählbaren Zeichensätzen generiert.
* Die Stärkeprüfung basiert auf:

  * Länge
  * Großbuchstaben, Zahlen und Sonderzeichen

### 🧪 Beispielausgabe

```
>> 1
Passwortlänge: 16
Großbuchstaben einfügen? yes
Zahlen einfügen? yes
Sonderzeichen einfügen? yes
Generiertes Passwort: q2T!vsY8$@Wnm%K9
```

```
>> 2
Passwort eingeben: password123
Passwort ist schwach
```

---

## 📜 License / Lizenz

MIT License – free for personal and commercial use.

```

---

Let me know if you'd like:
- A `.gitignore` that excludes `__pycache__/`
- CLI argument version (without interactive `input()`)
- Version with password saving and clipboard copy features
```
