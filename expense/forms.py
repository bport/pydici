# coding:utf-8
"""
Expense form setup
@author: Sébastien Renard <Sebastien.Renard@digitalfox.org>
@license: GPL v3 or newer
"""

from datetime import datetime

from django import forms
from django.forms.models import BaseInlineFormSet
from django.forms.widgets import TextInput
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from ajax_select.fields import AutoCompleteSelectField

from pydici.expense.models import Expense


class ExpenseForm(forms.ModelForm):
    """Expense form based on Expense model"""
    class Meta:
        model = Expense
        fields = ("description", "lead", "chargeable", "amount", "category")
        widgets = { "description": TextInput(attrs={"size": 40}), } # Increase default size

    lead = AutoCompleteSelectField('lead', required=False, label=_("Lead")) # Ajax it
