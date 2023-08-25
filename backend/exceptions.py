from fastapi import HTTPException, status


not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Record not found"
)

no_content_exception = HTTPException(
    status_code=status.HTTP_204_NO_CONTENT,
    detail="Successfully Deleted"

)