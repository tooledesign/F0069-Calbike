# Virtualenv for TDG Projects

The venv folder is used for creating a Python virtual environment using Python's
virtualenv tool. For more information on the virtualenv tool consult the [user
guide](https://virtualenv.pypa.io/en/stable/userguide/).

To create the virtual environment, run the following command in a terminal:
`python -m venv C:\path\to\my\project\venv`. Currently the most simple way to choose between a Python 2 and Python 3 environment is to install Anaconda for both 2 and 3, which can coexist. Then to create the environment desired, open the prompt associated with the version desired. 

Every time you do work on this project, you should activate this project's
specific Python environment. If you're on Linux, use virtualenv's `source` command, i.e. `source
C:\path\to\my\project\venv\Scripts\activate`. If you're on Windows, enter `C:\path\to\my\project\venv\Scripts\activate.bat`.

Each project should also include the `requirements.txt` file in the top folder of the repository. This should contain a list of all Python libraries used, including the version used. This can be obtained by running `pip freeze` with the project environment active. You can customize this for a given project, but it generally should not deviate too substantially from the version stored in this repo. When setting up your virtual environment you can
install all the necessary packages **after** activating your virtual environment
using pip: `pip install -r C:\path\to\my\project\requirements.txt`

This will take a bit of time to run, and you need to be connected to the K:/ drive for it to work.
