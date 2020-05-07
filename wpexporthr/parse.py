"""Parse WordPress eXtended RSS export file"""
import xml.etree.ElementTree as ET


class WpExport:
    """Parse WordPress export file
    """
    def __init__(self, xml_data):
        self.tree = ET.parse(xml_data)
        self.root = self.tree.getroot()
