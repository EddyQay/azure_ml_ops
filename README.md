*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Operationalizing Machine Learning Using Azure

*TODO:* Write an overview to your project.
It is one thing building a machine learning model, and another thing making them operational. After traning a machine learning model, it needs to be deployed into the right environment to allow access. This may be in the form of API enpoints or webservices. This project details the steps involved in deploying a model to an endpoint, and made available as an HTTP REST API.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step.

## Key Steps
This project details the entire process from authentication to comsuming the deployed model API in 6 key steps:
1. Authentication
2. Creating The AutoML Experiment
3. Deploy the best model
4. Enable Logging
5. Documenting APi With Swagger
6. Consume model endpoints

### Authentication
Every user of the Azure ML Studio will have to be authorized in order to use the service. To gain authorization, the user will need to be authenticated. There are several ways of authenticating with the platform, but we'll be accessing our subscription by granting permission to a [Service Principal](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest#sign-in-with-a-service-principal) that we'll create using the Azure CLI tool ```az```. Below ar ethe steps ataken to authenticate with Azure:

- First, install the CLI tool using various ways outlined in detail, in [this documentation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&tabs=azure-powershell). For this step, we use the Powershell method in windows with this shell script:
```Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi``` 

- After we have installed the tool, we can sign in using the following command:
```az login```. This may automatically open a browser to allow us choose which account to sign in to, or the following url will have to be opened manually in order to complete the authentication step:
[https://aka.ms/devicelogin](https://aka.ms/devicelogin)

- Upon a sucessful sign in, we would access the current sucription through a Service Principal, an account not tied to any user, and which would allow us to execute scripts securely and store credentails locally. The screenshot below shows how we scucessfully create a service principal for this session:
![image](images/InkedService-principal-success_LI.jpg)

- Now will associate this service principal to the workspace we will be working with in our current Azure subscription:
![image](images/Workspace-share-success-LI.png)

### Creating The AutoML Experiment
After signing-in to our Azure ML Studio workspace with the service principal we created earlier on, it is time to create the AutoML experiment using the studio.

- **Uploading the dataset**: Select the **Datasets** tab in left navigation pane of the studio workspace, then the following steps follow: 
1. **Create dataset > From web files **
2. Enter [this url](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv), for the ```bankmarketing_train.csv``` dataset, into the **Web URL** textbox that comes with the dialog that appears.
3. Provide a name for the dataset, in this case, we used ```bankmarketing_train```, and click **Next**
4. For the **Column headers** field in the **Settings and preview** section, we select ```All files have the same headers```, then click **Next**
5. We click **Next** again till the last section, *confirm details*, then click **Create** when we have confirmed that everything looks good.

Now we should see our new dataset appear with the name we gave to it, in under the **Registered datasets** section, as shown below:
![image](images/Dataset-Registered-Success.png)

- **Creating the experiment**: 
1. Select the **Automated ML(preview)** tab in the left naviagtion pane, then click on **New Automated ML Run**
2. Now, in the *select dataset* section of the *Create new Automated ML run* dialog, we select the dataset we created earlier on, then click **Next**
3. In the *Configure run* section, we enter a name to use for our expeirment, under *Create new experiment*; in this case we use ```LoanSubscription```.
4. For our *Target column*, which is the column we wish to predict, we select **y** from the dropdown list.
5. Now we need a compute resource in order to run our experiment. It is necessary to create a new one by clicking **Create new compute** below the *select compute cluster* field.
6. In the *New compute cluster* dialog, we enter a name for the compute, in this case we use ```udacity-ml```.
7. Next we select ```Standard_DS12_v2``` for the *Virtual machine size* field and enter ```1`` as the minimum number of nodes, then click **Create**
8. Back in the *Create new Automated ML run* dialog, we select **Classification**, under *Select task type*, and then click ** View additional configuration settings**
9. First ensure that *Explain best model* is checked, then, in *Exit criterion*, set *training job time (hours)* to ```3```, and metric threshold to ```0.056```.
10. Set *Max concurrent iterations*, under the *Concurrency* sectoin, to ```5``` and click **Save**.
11. Now click **Finish** to start the process.

When the experiment is complete, it will appear as complete, as as shown below:
![image](images/Experiment-complete.png)

and the best model shown as below:
![image](Best-model-success-1.png)

- **Deploying The Best Model**:


## Creating And Publishing A Pipeline With Notebooks
This section highlights the steps taken to create the same project, but this time, using Jupyter Notebooks on Azure, utilising the same resources created earlier on. The results achieved is the same as that achieved with the Azure ML Studio in the earlier section.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
