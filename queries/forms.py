from django import forms
from django.forms.widgets import HiddenInput


class QueryData(forms.Form):
    modescountry = forms.CharField(label='Country:')
    registeredowners = forms.CharField(label='Owner:')
    registration = forms.CharField(label='Registration:')
    aircraft_type = forms.CharField(label='Type:')
    serialno = forms.CharField(label='Serial Number:')
    yearbuilt = forms.CharField(label='Manufacture Year:')
    starttime = forms.CharField(label='Start Time:', )
    endtime = forms.CharField(label='End Time:')
    callsign = forms.CharField(label="CallSign:")
    firstaltitude = forms.CharField(label="Start altitude:")
    lastaltitude = forms.CharField(label="Final altitude:")
    firstsquawk = forms.CharField(label='SQUAWK code at start:')
    lastsquawk = forms.CharField(label='SQUAWK code at end:')
    hadalert = forms.BooleanField(label='Had Alert:')
    hademergency = forms.BooleanField(label='Had Emergency:')

    parameters_dict = {
        'modescountry': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
        },

        'registeredowners': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
        },

        'registration': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
        },

        'aircraft_type': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
        },

        'serialno': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'int',
        },

        'yearbuilt': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'aircraft',
            'type': 'int',
        },

        'starttime': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
            'type': 'datetime',
        },

        'endtime': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
            'type': 'datetime',
        },

        'callsign': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'string',
        },

        'firstaltitude': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
        },
        'lastaltitude': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
            'type': 'int',
        },

        'firstsquawk': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'int',
        },

        'lastsquawk': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'int',
        },

        'hadalert': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'bool',
        },

        'hademergency': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'bool',
        },

    }

    def __init__(self, chosen_fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = list(self.fields)
        for item in fields:
            if item not in chosen_fields:
                del self.fields[item]
