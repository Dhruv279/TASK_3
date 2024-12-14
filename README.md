
# Project Setup

1. **Create a new directory for the project and initialize it:**

   ```bash
   mkdir library_api
   cd library_api
   python -m venv venv
   venv\Scripts\activate 
   ```

2. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

3. **Create the following file structure:**

   ```
   library_api/
   |-- main.py
   |-- models.py
   |-- database.py
   |-- schemas.py
   |-- crud.py
   ```

## Run the API

1. **Start the API server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation by visiting:**

   ```
   http://127.0.0.1:8000/docs
   ```

