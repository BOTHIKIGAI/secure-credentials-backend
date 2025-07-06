"""Provide a FastAPI application for saving credentials securely."""

from fastapi import FastAPI

app = FastAPI(
    title="Save Credentials API",
    description="A API to save credentials in a secure way.",
    version="1.0.0",
    contact={
        "name": "Juan Esteban Cajiao Madero",
        "github": "BOTHIKIGAI",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/license/mit/",
    },
)
