class reservationBook(Book):
    def __init__(self, time, day):
        self.time = time
        self.day = day
# 예약날짜 입력 -> 예약성공하면 끝.예약실패하면 실패했습니다.
# 다른 날짜에 예약하세요 하며 다시 def실행
    def res_book(self):
        pass