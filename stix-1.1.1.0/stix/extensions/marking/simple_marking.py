import stix.bindings.extensions.marking.simple_marking as simple_marking_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class SimpleMarkingStructure(MarkingStructure):
    _binding = simple_marking_binding
    _binding_class = simple_marking_binding.SimpleMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1'
    _XSI_TYPE = "simpleMarking:SimpleMarkingStructureType"

    def __init__(self):
        super(SimpleMarkingStructure, self).__init__()
        self.statement = None

    def to_obj(self):
        obj = self._binding_class()

        MarkingStructure.to_obj(self, obj)

        obj.set_Statement(self.statement)

        return obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)
        if self.statement:
            d['statement'] = self.statement

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = SimpleMarkingStructure()
        MarkingStructure.from_obj(obj, m)
        m.statement = obj.get_Statement()

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None

        m = SimpleMarkingStructure()
        MarkingStructure.from_dict(marking_dict, m)
        m.statement = marking_dict.get('statement')

        return m


stix.data_marking.add_extension(SimpleMarkingStructure)

