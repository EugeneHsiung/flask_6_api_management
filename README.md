# flask_6_api_management

# Flask-based RESTful API
Using the [templates](https://github.com/hantswilliams/HHA_504_2023/tree/main/WK6/code/flask) provided, I created flask examples named `app_basic.p` and `app_flasgger.py` inside this [folder](https://github.com/EugeneHsiung/flask_6_api_management/tree/main/examples.py). I combined both templates and created an `app.py` flask template for this assignment. By running this application, type in `python app.py` in the shell terminal. The output would be a json file. For example: replace everything after the .dev with `/home?name=John&lastname=Smith` and the output should result in `{
  "message": "Hello JOHN SMITH!"
}`

# Azure API deployment
1. Install [homebrew](https://brew.sh/) with ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)".``` However, I was unsuccessful in installing homebrew so I used this [guide](https://docs.brew.sh/Installation) unsupported method instead. Type in ```mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew` or `git clone https://github.com/Homebrew/brew homebrew``` then type in ```eval "$(homebrew/bin/brew shellenv)"
brew update --force --quiet
chmod -R go-w "$(brew --prefix)/share/zsh"```

2. Follow [python tutorial for HTTP function](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators).

To install the Core Tools package, type in:

```brew tap azure/functions
brew install azure-functions-core-tools@4
# if upgrading on a machine that has 2.x or 3.x installed:
brew link --overwrite azure-functions-core-tools@4```

3. Type in `func init LocalFunctionProj --python -m V2` to create a functions project in a folder named LocalFunctionProj
4. Type in `cd LocalFunctionProj` to go to the project folder
5. Open the file `function_app.py` and

type in:

```
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")```

6. In the local.settings.json file, update the `AzureWebJobsStorage` with `"AzureWebJobsStorage": "UseDevelopmentStorage=true"`

