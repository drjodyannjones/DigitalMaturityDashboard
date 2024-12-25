import os

# Define the project structure as a dictionary
project_structure = {
    ".github/workflows": ["ci-cd.yml"],
    ".devcontainer": ["devcontainer.json"],
    "config": ["config.yaml", "secrets.yaml"],
    "dags": ["kpi_pipeline.py"],
    "dbt/models/staging": [],
    "dbt/models/marts": [],
    "dbt/models/gold": [],
    "dbt": ["dbt_project.yml"],
    "docker/airflow": ["Dockerfile", "requirements.txt"],
    "docker/metabase": ["Dockerfile"],
    "docker/postgres": ["Dockerfile", "init.sql"],
    "docs": ["architecture.md", "setup_guide.md"],
    "scripts": ["run_tests.sh", "deploy.sh"],
    "src/data/bronze": [],
    "src/data/silver": [],
    "src/data/gold": [],
    "src/utils": ["logger.py", "config_loader.py"],
    "src": ["main.py"],
    "tests": ["test_main.py"],
    "tests/test_utils": [],
}

# Files at the root level
root_files = [
    ".env", ".gitignore", "Makefile", "pyproject.toml", "README.md"
]

# Create directories and files
def create_structure(base_path):
    for path, files in project_structure.items():
        dir_path = os.path.join(base_path, path)
        os.makedirs(dir_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(dir_path, file)
            with open(file_path, 'w') as f:
                f.write("")  # Create an empty file

    for file in root_files:
        file_path = os.path.join(base_path, file)
        with open(file_path, 'w') as f:
            f.write("")

# Run the script
if __name__ == "__main__":
    base_path = os.getcwd()
    create_structure(base_path)
    print("✅ Project structure created successfully!")

