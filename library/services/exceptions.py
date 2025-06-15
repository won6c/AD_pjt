class AlreadyBorrowedError(Exception):
    """사용자가 이미 해당 책을 대출 중인 경우"""
    def __init__(self, message="이미 이 책을 대출 중입니다."):
        self.message = message
        super().__init__(self.message)

class NotYourReviewError(Exception):
    """다른 사용자의 리뷰를 수정/삭제하려 한 경우"""
    def __init__(self, message="본인의 리뷰만 수정/삭제할 수 있습니다."):
        self.message = message
        super().__init__(self.message)

class ReviewNotFoundError(Exception):
    """해당 리뷰가 존재하지 않거나 권한이 없는 경우"""
    def __init__(self, message="해당 리뷰를 찾을 수 없거나 접근 권한이 없습니다."):
        self.message = message
        super().__init__(self.message)

class BookNotFoundError(Exception):
    """해당 도서를 찾을 수 없는 경우"""
    def __init__(self, message="해당 도서를 찾을 수 없습니다."):
        self.message = message
        super().__init__(self.message)
