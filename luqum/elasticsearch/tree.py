import abc
import re


class JsonSerializableMixin:

    @property
    @abc.abstractmethod
    def json(self):
        return


class AbstractEItem(JsonSerializableMixin):

    boost = None
    _fuzzy = None

    _KEYS_TO_ADD = ('boost', 'fuzziness', )
    ADDITIONAL_KEYS_TO_ADD = ()

    def __init__(self, method='term', field='text'):
        self.method = method
        self.field = field

    @property
    def json(self):
        json = {self.method: {self.field: {}}}
        inner_json = json[self.method][self.field]

        # add base conf
        keys = self._KEYS_TO_ADD + self.ADDITIONAL_KEYS_TO_ADD
        for key in keys:
            value = getattr(self, key)
            if value is not None:
                inner_json[key] = value

        return json

    @property
    def fuzziness(self):
        return self._fuzzy

    @fuzziness.setter
    def fuzziness(self, fuzzy):
        self.method = 'fuzzy'
        self._fuzzy = fuzzy


class EWord(AbstractEItem):

    ADDITIONAL_KEYS_TO_ADD = ('value', )

    def __init__(self, value):
        super().__init__()
        self.value = value


class EPhrase(AbstractEItem):

    ADDITIONAL_KEYS_TO_ADD = ('query',)
    _proximity = None

    def __init__(self, phrase):
        super().__init__(method='match_phrase')
        self.query = re.search(r'"(?P<value>.+)"', phrase).group("value")

    @property
    def slop(self):
        return self._proximity

    @slop.setter
    def slop(self, slop):
        self._proximity = slop
        self.ADDITIONAL_KEYS_TO_ADD += ('slop', )


class ERange(AbstractEItem):

    def __init__(self, lt=None, lte=None, gt=None, gte=None):
        super().__init__(method='range')
        if lt:
            self.lt = lt
            self.ADDITIONAL_KEYS_TO_ADD += ('lt', )
        elif lte:
            self.lte = lte
            self.ADDITIONAL_KEYS_TO_ADD += ('lte', )
        else:
            raise ValueError
        if gt:
            self.gt = gt
            self.ADDITIONAL_KEYS_TO_ADD += ('gt', )
        elif gte:
            self.gte = gte
            self.ADDITIONAL_KEYS_TO_ADD += ('gte', )
        else:
            raise ValueError


class AbstractEOperation(JsonSerializableMixin):

    def __init__(self, items):
        self.items = items

    @property
    def json(self):
        return {'bool': {self.operation: [item.json for item in self.items]}}


class EShould(AbstractEOperation):
    operation = 'should'


class EMust(AbstractEOperation):
    operation = 'must'


class EMustNot(AbstractEOperation):
    operation = 'must_not'