from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class QueryData(forms.Form):
    modescountry = CountryField().formfield(widget=CountrySelectWidget())
    registeredowners = forms.CharField(label='Owner:')
    registration = forms.CharField(label='Registration:')
    atype = forms.CharField(label='Type:')
    serialno = forms.IntegerField(label='Serial Number:')
    yearbuilt = forms.IntegerField(label='Manufacture Year:', initial=2011)
    starttime = forms.DateTimeField(label='Start Time:')
    endtime = forms.DateTimeField(label='End Time:')
    callsign = forms.CharField(label="CallSign:")
    firstaltitude = forms.IntegerField(label="First altitude:", initial=5_000)
    lastaltitude = forms.IntegerField(label="Last altitude:", initial=10_000)
    firstsquawk = forms.IntegerField(label='SQUAWK code at start:')
    lastsquawk = forms.IntegerField(label='SQUAWK code at end:')
    hadalert = forms.BooleanField(label='Had Alert:')
    hademergency = forms.BooleanField(label='Had Emergency:')

    # parameters_dict is a setup dictionary containing parameters for setting up query fields.
    # parameters are:
    #     selector : if there should be a selector drop dawn menu
    #     selector_values: if there is a selector field - values on the drop-dawn menu
    #     extra_field: if there should be an extra field(ex for between field)
    #     type: # a proper data type
    #     human_text: A human readable text for the field.
    # if new queries added - add fields accordingly.
    # if new functionality added - add Key/Value pairs.
    # NB: If selector is true - there must be selector values list!


    parameters_dict = {
        'modescountry': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
            'human_text': 'A1:Country',
        },

        'registeredowners': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
            'human_text': 'A2:Owner',
        },

        'registration': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
            'human_text': 'A3:Registration',
        },

        'atype': {
            # changed name to atype not to shadow python type() function
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'string',
            'human_text': 'A4:Aircraft Type',
        },

        'serialno': {
            'selector': False,
            'extra_field': False,
            'table': 'aircraft',
            'type': 'int',
            'human_text': 'A5:Serial Number',
        },

        'yearbuilt': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'aircraft',
            'type': 'int',
            'human_text': 'A6: Year of Manufacture',
        },

        'starttime': {
            'selector': False,
            'extra_field': False,
            'table': 'flights',
            'type': 'datetime',
            'human_text': 'F1:Start Time',
        },

        'endtime': {
            'selector': False,
            'extra_field': False,
            'table': 'flights',
            'type': 'datetime',
            'human_text': 'F2:End Time',
        },

        'callsign': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'string',
            'human_text': 'F3:Callsign',
        },

        'firstaltitude': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
            'type': 'int',
            'human_text': 'F4:First Altitude',
        },
        'lastaltitude': {
            'selector': True,
            'selector_values': ['less', 'less or equal', 'equal', 'greater or equal', 'greater', 'between'],
            'extra_field': True,
            'table': 'flights',
            'type': 'int',
            'human_text': 'F5:Last Altitude',
        },

        'firstsquawk': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'int',
            'human_text': 'F6:First SQUAWK',
        },

        'lastsquawk': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'int',
            'human_text': 'F7:Last SQUAWK',
        },

        'hadalert': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'bool',
            'human_text': 'F8:Had Alert',
        },

        'hademergency': {
            'selector': False,
            'selector_values': [],
            'extra_field': False,
            'table': 'flights',
            'type': 'bool',
            'human_text': 'F9:Had Emergency',
        },

    }

    def __init__(self, chosen_fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = list(self.fields)
        for item in fields:
            if item not in chosen_fields:
                del self.fields[item]
