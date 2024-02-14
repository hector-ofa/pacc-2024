from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/hector-ofa/pacc-2024.git",
        entrypoint="weather2-tasks.py:pipeline",
    ).deploy(
        name="managed-deployment",
        work_pool_name="my-managed-pool",
    )