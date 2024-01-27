from rest_framework.exceptions import ValidationError


class SellerLevelValidator:
    """ Валидатор для поля level продавца"""

    def __init__(self, level, provider):
        self.level = level
        self.provider = provider

    def __call__(self, value):
        """

        Возбуждается ValidationError если:
        - для продавца нулевого уровня выбирается поставщиком любой другой поставщик кроме текущего
        - для поставщика певрого уровня в качестве поставщика выбирается поставщик второго уровня
        """
        level = value.get(self.level)
        provider = value.get(self.provider)
        if provider:
            if level == 0 and provider != self:
                raise ValidationError('У поставщика нулевого уровня не может быть другого поставщика')
            elif level == 1 and provider.level == 2:
                raise ValidationError('У поставщика первого уровня не может поставщика второго уровня')
