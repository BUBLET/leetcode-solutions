class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Если последнее число в списке меньше 9, то увеличиваем его на 1 и возвращаем список
        for i in range(1, len(digits) + 1):
            if digits[len(digits)-i] < 9:
                digits[len(digits)-i] += 1
                return digits
            else:
                # Иначе превращаем его в 0
                digits[len(digits)-i] = 0
        
        # Если по итогам цикла первый элемент списка 0 - вставляем в начало 1
        if digits[0] == 0:
            digits.insert(0, 1)

        # Если cписок состоял только из 9, то добавляем 0 в конец
        if len(digits) == 1 :
            digits.append(0)
        
        return digits