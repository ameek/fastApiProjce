## this is just the demo of fast api

### here the fast api starts at 8000 port

to start the project
1. create vertual env for your pyton
    * using python venv
    ```bash
    python -m venv <env_name>
    ```
    * using conda
    ```bash
    conda create --name <myenv> python=3.8
    ```

2. activate the virtual env
    * using python venv
    ```bash
    source <env_name>/bin/activate
    ```
    * using conda
    ```bash
    conda activate <myenv>
    ```

3. install requried packeges for fastApi
    ```bash
    pip install fastapi
    ```
    ```bash
    pip install 'uvicorn[standard]'
    ```
4. running the api
    ```bash
    uvicorn main:app --reload
    ```
5. test the api 
    ```
    localhost:8000/docs
    ```