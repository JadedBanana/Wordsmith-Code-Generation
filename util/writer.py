from util import env
import os

def write(full_str, relative_file):
    """
    Writes the string to a file.
    """
    # Load dotenv.
    env.load_if_not_loaded_yet()

    # Get wordsmith dir from os.environ
    wordsmith_dir = os.environ['WORDSMITH_DIR']

    # Open file, write, close
    rb = open(os.path.join(wordsmith_dir, relative_file), 'w')
    rb.write(full_str)
    rb.close()


if __name__ == '__main__':
    write(None, None)