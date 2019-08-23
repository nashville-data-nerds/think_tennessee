### How to link a Pull Request to an Issue

In order to link a pull request to an issue, you simply need to type `#` and then the number of the issue, such as `#13`.  This will create a link to the pull request.

### Creating a Visual with a Python Script

If you are creating a visual with a python script, please create a descriptive folder name in the `code` directory and include the following in it:
- A brief markdown document that includes relevant information such as the data source you used and a description of the visual.
- The python script that generates the visuals.
- A rendered version of the visual

### Creating a Visual with a Jupyter Notebook/Lab

When creating a visual within a notebook, please put it in the `notebooks` directory and provide a descriptive name of the notebook and please do the following:
- Include a brief markdown cell that explains the data source and the visual you are creating.
- When you submit the notebook, please have the visual rendered so it can be seen in GitHub for review.

### How to setup your Anaconda environment

#### Mac and Linux

If you have not already, please see [Installing Anaconda](https://docs.anaconda.com/anaconda/install/) for how to setup anaconda. Once you have anaconda setup, when you open a terminal, you should see a `(base)` in front of your username.

```
conda env create -f /path/to/environment.yml
```

You can also use the [setup_conda_env.sh](https://github.com/nashville-data-nerds/think_tennessee/blob/master/development/setup_conda_env.sh) under the `development` directory which will take care of setting up the environment.

#### Windows

*This will also work in Mac via the Anaconda application, however I always strongly recommend getting more familiar with a terminal where possible.*

1. Open the Anaconda Navigator.
2. In the left panel, go to `Environments`
3. Select `Import` towards the bottom.
4. Under Specification File, choose the file browser and select the [environment file](environment.yml) in Think Tennessee repository.  The name should auto-populate
5. Select `Import` - this should then create your environment.

### How to update your Anaconda environment

#### Mac and Linux

Found the easiest way to update is to simply wipe out the previous environment and reinstall it.  You can use the script [setup_conda_env.sh](https://github.com/nashville-data-nerds/think_tennessee/blob/master/development/setup_conda_env.sh) to do this.  Be sure to be in your base environment when doing this.


