from util import env
import os

def isfile(relative_file):
    # Load dotenv.
    env.load_if_not_loaded_yet()

    # Get wordsmith dir from os.environ
    wordsmith_dir = os.environ['WORDSMITH_DIR']

    # Return
    return os.path.isfile(os.path.join(wordsmith_dir, relative_file))