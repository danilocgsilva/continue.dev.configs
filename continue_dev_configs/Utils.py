class Utils:
    @staticmethod
    def get_current_time() -> str:
        """
        Returns the current date and time in the format: YEAR_MONTH_DAY_HOUR_MINUTE_SECOND
        Example: 2024_12_25_14_30_45
        """
        from datetime import datetime
        return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        