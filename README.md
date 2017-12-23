# Setup

1. Clone the repository and all submodules

`$ git clone --recursive https://github.com/croach/blog.git`

> NOTE: If you've cloned the repository without the `--recursive` option, you can simply run `git submodule update --init --recursive` to setup all of the submodules.

2. Create the conda environment from the environment file

`$ conda env create -f environment.yml`

3. Start the development server

`$ make devserver`

4. Navigate to "localhost:8000" for the main site, or "localhost:8000/drafts" for drafts.


# To Do

1. Add the data files to the voter_fraud repository
2. ~~Remove danielfrg's `pelican-ipynb` from my list of submodules and add my own forked version of the library and use the `add_preprocessor_support` branch.~~
3. ~~Remove my old theme from the list of submodules as well.~~
