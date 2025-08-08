from setuptools import setup, find_packages

setup(
    name="mechbot-2x",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "sqlalchemy>=2.0.23",
        "psycopg2-binary>=2.9.9",
        "redis>=5.0.1",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "test": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
        ]
    }
)
