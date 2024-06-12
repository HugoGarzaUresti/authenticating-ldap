# Authenticating with LDAP

This guide demonstrates how to authenticate a user using an LDAP server in Python. We will use the `ldap3` library to connect to an LDAP server and perform authentication.

## Requirements

- Python 3.x
- `ldap3` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Update the LDAP server URL and DN in `app/__init__.py`:
    ```python
    server = Server('ldap://your-ldap-server', get_info=ALL)
    conn = Connection(server, f'uid={username},ou=users,dc=example,dc=com', password)
    ```

3. Run the application:
    ```sh
    python run.py
    ```

## Code Explanation

### `app/__init__.py`

This module contains the function `authenticate` which connects to the LDAP server and attempts to authenticate a user with the provided username and password.

- **`Server`**: Represents the LDAP server.
- **`Connection`**: Represents a connection to the LDAP server. The `bind` method is used to authenticate.

### `run.py`

This script serves as the entry point for the application. It prompts the user for their username and password, then calls the `authenticate` function.

## Additional Information

- Make sure your LDAP server details (URL, DN structure) are correctly configured.
- If you encounter issues, check the LDAP server logs for more details.
