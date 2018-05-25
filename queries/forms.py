from django import forms
from django.forms.widgets import HiddenInput


class QueryData(forms.Form):
    modescountry = forms.CharField(label='Country:')
    registeredowners = forms.CharField(label='Owner:')
    registration = forms.CharField(label='Registration:')
    atype = forms.CharField(label='Type:')
    serialno = forms.IntegerField(label='Serial Number:')
    yearbuilt = forms.IntegerField(label='Manufacture Year:')
    starttime = forms.DateTimeField(label='Start Time:', )
    endtime = forms.DateTimeField(label='End Time:')
    callsign = forms.CharField(label="CallSign:")
    firstaltitude = forms.IntegerField(label="Start altitude:")
    lastaltitude = forms.IntegerField(label="Final altitude:")
    firstsquawk = forms.IntegerField(label='SQUAWK code at start:')
    lastsquawk = forms.IntegerField(label='SQUAWK code at end:')
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

        'atype': {
            # changed name to atype not to shadow python type() function
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
            'selector': False,
            'extra_field': False,
            'table': 'flights',
            'type': 'datetime',
        },

        'endtime': {
            'selector': False,
            'extra_field': False,
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
            'type': 'int',
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
