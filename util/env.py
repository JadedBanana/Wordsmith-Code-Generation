loaded = False

def load():
    """
    Loads the .env file. Also checks to make sure that the file exists, and that all required
    variables are accounted for.

    Raises:
        InvalidDotenvFileError : .env file is either missing or is lacking a required variable.
    """
    # Required imports
    import os

    # List of variables we should expect to see in every .env file.
    expected_dotenv_vars = [
        'WORDSMITH_DIR'
    ]

    # First, check that the .env file does exist.
    if not os.path.exists('.env'):
        raise ValueError('.env file missing from working directory')

    # Then, load .env.
    from dotenv import load_dotenv as dotenv_load
    dotenv_load()

    # Detect if any dotenv_vars are missing.
    for dotenv_var in expected_dotenv_vars:
        if dotenv_var not in os.environ.keys():
            raise ValueError(f'Missing variable {dotenv_var}')

    # Set loaded to True.
    global loaded
    loaded = True

def load_if_not_loaded_yet():
    """
    Loads if it hasn't been loaded already.
    """
    global loaded
    if not loaded:
        load()