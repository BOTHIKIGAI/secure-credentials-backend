# Copyright (c) 2025 Juan Esteban Cajiao Madero

"""Defines the Credentials entity for secure credential storage."""

from sqlmodel import Field, SQLModel


class Credentials(SQLModel, table=True):
    """
    Represents user credentials for secure storage.

    Attributes
    ----------
    id : int | None
        The unique identifier for the credentials.
    email : str
        The email associated with the credentials.
    username : str | None
        The username associated with the credentials.
    password : str
        The password for the credentials.

    """

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    username: str | None
    password: str
