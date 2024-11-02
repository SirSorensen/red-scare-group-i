# Introduction

This repository is for the [Red Scare](https://learnit.itu.dk/mod/assign/view.php?id=208004) project for the course "Algorithm Design, MSc CS (Autumn 2024)" at the IT University in Copenhagen.

## How to run the program

The program builds a graph from a file in the `data` folder 
Now, in `src\main.py`, change the `file_name`-variable to the name of the data-input from the `data` folder in the project (i.e. "G-ex" for `data/G-ex.txt`).

In your terminal, run one of the following commands:

```sh
cd src
python main.py

# Or

python src/main.py
```

Now you should have successfully run the program!

## How to update Overleaf submodule

In your terminal, write the following:

```sh
git submodule update --init --recursive
```

> If you are prompted for username and password, the username is `git` and the password is your `<Git authentication token>` from Overleaf.
>
> You can make a token at [https://www.overleaf.com/user/settings](https://www.overleaf.com/user/settings#project-sync-tokens).

## Running tests

Run one of the test scripts in the `test` folder.

Example:

```sh
python test/none_tests.py

# Or

cd test
python none_tests.py
```

To print the graph file name from the data folder add the word `debug` as an argument to the test file.

```sh
python tests/none_tests.py debug
```

## Visualizing a graph

### Videos

To get a video of a graph, run the following command:

```sh
py ./src/visualization/run_animation.py <data file name> 
```

The video will be saved in the `media/videos/1080p60` folder.

> Note: The videos work poorly for large and square graphs.

### Grid graphs

For the grid graphs i recommend running the following command:

```sh
py ./src/visualization/grid_draw.py <data file name>
```

The image will be saved in the `media/images` folder.

> Note: The structure used for the grid graphs can probably be used in implementations for other graph types as well.
