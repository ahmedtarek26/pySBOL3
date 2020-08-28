import logging
import os
import unittest

import sbol3

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
SBOL3_LOCATION = os.path.join(MODULE_LOCATION, 'SBOLTestSuite', 'SBOL3')


class TestDocument(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logging.basicConfig(level=logging.INFO)

    def test_read_ntriples(self):
        # Initial test of Document.read
        test_path = os.path.join(SBOL3_LOCATION, 'entity', 'model',
                                 'model.nt')
        doc = sbol3.Document()
        doc.read(test_path, sbol3.NTRIPLES)
        doc.write('model.sbol', sbol3.NTRIPLES)

    def test_read_turtle(self):
        # Initial test of Document.read
        test_path = os.path.join(SBOL3_LOCATION, 'entity', 'model',
                                 'model.ttl')
        doc = sbol3.Document()
        doc.read(test_path, sbol3.TURTLE)

    def test_read_xml_model(self):
        # Initial test of Document.read
        test_path = os.path.join(SBOL3_LOCATION, 'entity', 'model',
                                 'model.rdf')
        doc = sbol3.Document()
        doc.read(test_path, sbol3.RDF_XML)
        self.assertIsNotNone(doc.find('https://sbolstandard.org/examples/toggle_switch'))
        self.assertIsNotNone(doc.find('toggle_switch'))
        self.assertIsNotNone(doc.find('https://sbolstandard.org/examples/model1'))
        # We have inferred the displayId of model1
        self.assertIsNotNone(doc.find('model1'))

    def test_read_turtle_interface(self):
        # Initial test of Document.read
        test_path = os.path.join(SBOL3_LOCATION, 'entity', 'interface',
                                 'interface.ttl')
        doc = sbol3.Document()
        doc.read(test_path, sbol3.TURTLE)

    def test_read_turtle_toggle_switch(self):
        # Initial test of Document.read
        test_path = os.path.join(SBOL3_LOCATION, 'toggle_switch',
                                 'toggle_switch.ttl')
        doc = sbol3.Document()
        doc.read(test_path, sbol3.TURTLE)

    def test_add(self):
        doc = sbol3.Document()
        type_uri = 'https://github.com/synbiodex/sbol3#TestObj'
        obj1 = sbol3.SBOLObject('obj', type_uri)
        with self.assertRaises(TypeError):
            doc.add(obj1)
        seq = sbol3.Sequence('seq1')
        doc.add(seq)
        seq2 = doc.find(seq.identity)
        self.assertEqual(seq.identity, seq2.identity)

    def test_write(self):
        doc = sbol3.Document()
        doc.add(sbol3.Component('c1', sbol3.SBO_DNA))
        doc.write('test_output.ntriples', sbol3.NTRIPLES)
        doc.write('test_output.xml', sbol3.RDF_XML)


if __name__ == '__main__':
    unittest.main()
