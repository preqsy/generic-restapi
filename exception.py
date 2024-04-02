from fastapi import HTTPException, status


class InvalidRequest(HTTPException):
    def __init__(self, detail:str="Invalid Request"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)