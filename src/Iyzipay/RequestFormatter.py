class RequestFormatter():
    @staticmethod
    def format_price(price):
        if '.' not in price:
            price += ".0"
        sub_str_index = 0
        price_reversed = price[::-1]
        for index in range(len(price_reversed)):
            if price_reversed[index] is "0":
                sub_str_index = index + 1
            elif price_reversed[index] is ".":
                price_reversed = "0" + price_reversed
                break
            else:
                break
        return price_reversed[sub_str_index:][::-1]
