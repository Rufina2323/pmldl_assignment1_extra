import subprocess


def start_services_callable():
    subprocess.run(["docker", "network", "create", "ml-model-network"])

    subprocess.run(["docker", "stop", "api"])
    subprocess.run(["docker", "rm", "api"])
    subprocess.run(["docker", "build", "-t", "ml-model-api", "/opt/airflow/code/deployment/api"])
    subprocess.run(["docker", "run", "-d", "--network", "ml-model-network", "--name", "api", "ml-model-api"])

    subprocess.run(["docker", "stop", "app"])
    subprocess.run(["docker", "rm", "app"])
    subprocess.run(["docker", "build", "-t", "ml-model-app", "/opt/airflow/code/deployment/app"])
    subprocess.run(["docker", "run", "-d", "-p", "8501:8501", "--name", "app", "-e", "ENDPOINT_URL=http://api:8000/inference", "--network", "ml-model-network", "ml-model-app"])
