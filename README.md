# Simple File-Based Contact Book

This is a command-line contact book application written in Python. It allows you to add, view, and search for contacts. All data is saved locally to a `contacts.txt` file, so your information persists between sessions.

## Features

-   **Add Contacts:** Save a new contact with a name and phone number.
-   **View All Contacts:** Display a list of all saved contacts.
-   **Search Contacts:** Look up a contact by name to find their phone number.
-   **Data Persistence:** Contact information is automatically saved to `contacts.txt` and loaded when the program starts.

## How it Works

The application stores contacts in a simple `key,value` format within a text file (`contacts.txt`), where the key is the contact's name and the value is their phone number.

## How to Run

1.  Make sure you have Python 3 installed.
2.  Download the `contact_book.py` file.
3.  Open your terminal or command prompt.
4.  Navigate to the directory containing the file.
5.  Run the script using:
    ```sh
    python contact_book.py
    ```
6.  A `contacts.txt` file will be created in the same directory to store your contacts.
