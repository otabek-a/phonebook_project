# Phonebook Project

- This project is a simple phonebook application that allows users to add, edit, and delete contacts.

## Create virtual environment

```bash
python3 -m venv env
```

## Activate virtual environment

```bash
source env/bin/activate
```

## Activate for Windows

```bash
env\Scripts\activate
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Create Contact class

- Attributes:
  - First name (str)
  - Last name (str)
  - Phone number (str)

- Methods:
  - add_contact (New entries with unique name)
  - edit_contact
  - delete_contact