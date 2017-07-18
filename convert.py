from decimal import Decimal
import xml.sax

def check_record(stack):
    if [elem['name'] for elem in stack] == ['HealthData', 'Record']:
        record_elem = stack[1]
        check_body_mass(record_elem)

def check_body_mass(record_elem):
    attrs = record_elem['attrs']
    if attrs['type'] == 'HKQuantityTypeIdentifierBodyMass':
        date = attrs['startDate'][:10]

        assert attrs['unit'] == 'lb'
        pounds = Decimal(attrs['value'])
        grams = pounds * 454

        print('{}, {}'.format(date, grams))

class Handler(xml.sax.handler.ContentHandler):
    stack = []

    def startElement(self, name, attrs):
        self.stack.append({
            'name': name,
            'attrs': {name: attrs.getValue(name) for name in attrs.getNames()}
        })    

        check_record(self.stack)

    def endElement(self, name):
        self.stack.pop()

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 1

    parser = xml.sax.make_parser()
    parser.setContentHandler(Handler())

    with open(sys.argv[1]) as export:
        parser.parse(export)

