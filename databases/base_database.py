from abc import ABC, abstractmethod
from typing import Optional


class Database(ABC):
    """
    This interface defines basic operations for interacting with the database.

    """

    @abstractmethod
    async def create(self, user_data: dict) -> Optional[dict]:
        """
        Creates a new user in the database.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            Optional[dict]: A dictionary containing the created user information, or None on failure.
        """

    @abstractmethod
    def get_all_data(self) -> Optional[dict]:
        """
        Retrieves a user from the database based on their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[dict]: A dictionary containing user information if found,
                             or None if not found.
        """

    @abstractmethod
    def get_data_by_id(self, id: int) -> Optional[dict]:
        """
        Retrieves an from the database based on it's ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[dict]: A dictionary containing user information if found,
                             or None if not found.
        """

    @abstractmethod
    async def update_data(self, id: int, data_obj) -> Optional[dict]:
        """
        Update an Item in the DB.

        Args:
            user_id (int): The ID of the user to retrieve.
            data(dict): to Update

        Returns:
            Optional[dict]: A dictionary containing user information if found,
                             or None if not found.
        """

    async def delete_data(self, id: int) -> bool:
        """
        Deletes an Item.
        Args:
            user_id (int): The ID of the user to retrieve.
        Returns:
            True
        """
        return
