Title: Running Jupyter Lab as a Desktop Application
Slug: jupyterlab-desktop-app
Date: 2018-01-18
Category: Jupyter
Tags: jupyter
Status: published
Author: Christopher Roach
Summary: A quick post on how to run Jupyter Lab using Chrome's app mode

So, [Jupyter Lab](https://jupyterlab-tutorial.readthedocs.io/en/latest/index.html) is starting to get really interesting as a day-to-day replacement for standard Jupyter Notebooks and as a python competitor to R’s [RStudio IDE](https://www.rstudio.com/products/RStudio/). But, while a Jupyter Notebook with its multi-page interface feels right at home in the browser, I feel that as a single page application, Jupyter Lab would work better as a standalone desktop app without all the unwanted “chrome” that comes with the standard web browser. Luckily, the Chrome browser has an application mode that allows it to run with all of the toolbars and unnecessary UI removed. Using this mode will give you back a good deal of screen real estate and make Jupyter Lab feel more like a native application rather than a website running inside of your browser. 

To use the application mode of Chrome with Jupyter Lab, you simply need to run the Jupyter Lab server with the `--no-browser` option to prevent it from popping open the application in your default browser.

```
$ jupyter lab --no-browser
```

Then, copy the URL printed out to the terminal (example below).

```
...
[I 09:36:41.608 LabApp] The Jupyter Notebook is running at:
[I 09:36:41.608 LabApp] http://localhost:8888/?token=<token>
[I 09:36:41.608 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 09:36:41.609 LabApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=<token>
```

And, to [open Chrome in application mode](https://stackoverflow.com/questions/16124877/how-do-you-hide-the-address-bar-in-google-chrome-for-chrome-apps) with the Jupyter Lab URL, you simply need to call it with the `--app=<URL>` option and pass the URL you just copied. 

On a Mac, the command to do so would look like the following.

```
$ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --app=http://localhost:8888/?token=<token>
```

Once you run the command, you should see something like the following window pop up.

![Jupyter Lab Running in App Mode](/images/jupyterlab_desktop_app/jupyterlab_app_mode.png)

Notice the distinct lack of any and all toolbars. In fact, the only toolbar that shows up is the set of menus in the Jupyter Lab application.

## Making the change permanent

Now, if running two commands with a few extra options every time you want to open up Jupyter Lab happens to be a bit too much for you, you’re in luck. You can make this behavior permanent by simply modifying the config to change the default browser for Jupyter Lab.

If you’ve modified your default Jupyter Notebook configuration in the past, you can simply open up the configuration file that already exists (`~/.jupyter/jupyter_notebook_config.py`) and add the following line to it.

```python
c.LabApp.browser = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --app=%s'
```

However, if this is your first time ever modifying your Jupyter Notebook configuation, you’ll probably need to generate it first. You can do so with the following command.

```
$ jupyter lab --generate-config
```

After generating the config, simply open up the newly created file and add the browser config line from above. Once you’ve modified the config, you can simply call `jupyter lab` and the app will open up in a pristine window devoid of all the typical bells and whistles.