### IMPORTS                     ###
    ## Dependencies                 ##
import filemodes as _filemodes
    ## Dependencies                 ##
import os as _os
from tkinter import *
import xml.etree.ElementTree as _ET
import typing as _typing
import collections as _collections
### IMPORTS                     ###
### DO_NOT_DISTURB              ###
class _(object):
    """ Do Not Disturb """
    def __init__(self):
        self.disturbtions = [
            'tk',       # default
            'ttk',      # recommended
            'beginner'
        ]

        self.standard_library = [
            'templates'
        ]
        self.approved_tags = [
            # General
            'Dist',

            # Tk Widgets
            'Button',
            'Checkbutton',
            'Radiobutton',
            'Spinbox',
            'Listbox',
            'Entry',
            'Text',
            'Menu',
            'Label',
            'Frame',
            'Labelframe'
            # TTK Widgets
        ]
        self.approved_attrs = {
            'standard': [
                'activebackground',
                'activeforeground',
                'anchor',
                'background',
                'bitmap',
                'borderwidth',
                'cursor',
                'disabledforeground',
                'font',
                'foreground',
                'highlightbackground',
                'highlightcolor',
                'highlightthickness',
                'image',
                'justify',
                'padding',
                'relief',
                'repeatdelay',
                'repeatinterval',
                'takefocus',
                'text',
                'textvariable',
                'underline',
                'wraplength'
            ],
            'general': [
                'import',
                'dist'
            ],
            'Button': [
                'command',
                'compound',
                'default',
                'height',
                'overrelief',
                'state',
                'width'
            ]
        }
### DO_NOT_DISTURB              ###
### SETTINGS CLASS              ###
class Settings(object):
    def __init__(self): self.settings = {
        'dist': 'tk'
    }
### SETTINGS CLASS              ###
### LAMBDAS                     ###
_miss_attr_err = lambda attr, required=True: (
    "Missing" + ("required" if required else "") + f"attribute: {attr}"
)
### LAMBDAS                     ###
### LOAD                        ###
def load(src: _typing.TextIO) -> dict:
    parser = _ET.XMLParser(encoding="utf-8")
    _root = _ET.parse(src, parser).getroot()
    CNF = _()
    settings = Settings()
    parsed_content = {'master': Tk()}
    ## Closures                 ##
    def make_widget(widget_class, master, **opts):
        widget_class = eval(
            widget_class.capitalize(),
            globals(),
            locals()
        )
        exec(
            f'global w_\nw_ = {widget_class.__name__}(master, **opts)',
            globals(), locals()
        )
        return w_
    ## Closures                 ##
    _root = next(_root.iter())    # skip past src tag
    for elem in _root:
        ## Data                     ##
        tag = elem.tag.capitalize()
        attr = elem.attrib
        master = parsed_content['master']
        attr['text'] = elem.text
        ## Data                     ##
        ## Checks                   ##
        assert tag in CNF.approved_tags, f"'{tag}' tag is not recognized"
        assert all([a in (
            CNF.approved_attrs['standard']
            + CNF.approved_attrs['general']
            + CNF.approved_attrs[tag]
        ) for a in attr if a not in (
            'text',
            'id',
            'version'
        )]), f"An attribute in '{attr}' is not recognized"
        ## Checks                   ##
        ## Filter Attrs             ##
        f_attr = {}
        for k, v in attr.items():
            if k not in ('id',): f_attr[k] = v
        ## Filter Attrs             ##
        ## Handle Tags              ##
        if tag in ('Dist',):
            if tag == 'Dist':
                version = attr.get('version')
                # checks                    #
                assert version, _miss_attr_err('version')
                assert version in CNF.disturbtions, f"Unrecognized distrubtion: {version}"
                # checks                    #
                settings.settings['dist'] = version

        elif tag in ('Frame',):     # acts like a div
            frame_master = Frame(master)
            for frame_elem in elem:
                fm_tag = frame_elem.tag
                fm_attr = frame_elem.attrib

                w = make_widget(
                    tag,    # capitalized string in CamalCase
                    frame_master,   # the master of the widget
                    **{k:v for (k, v) in f_attr.items() if k != 'text'}
                )
                parsed_content[fm_attr['id']] = w
            parsed_content[attr['id']] = frame_master
        else:
            w = make_widget(
                tag,    # capitalized string in CamalCase
                master, # the master of the widget
                **{k:v for (k, v) in f_attr.items()}  # dict comp for opts
            )
            parsed_content[attr['id']] = w
        ## Handle Tags              ##
    return parsed_content
### LOAD                        ###
### DOCUMENTATION               ###
"""

"""
### DOCUMENTATION               ###