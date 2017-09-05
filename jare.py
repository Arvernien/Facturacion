#!/usr/bin/python

from distutils.core import setup
import py2exe

setup(windows=['gttFactura.py'], options={"py2exe": {"includes": ["profiles.*", "sip", "openpyxl", "PyQt4.QtSql", "PyQt4.QtNetwork", "PyQt4.QtXml", "PyQt4.Qsci"]}})