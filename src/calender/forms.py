from django import forms

from calender.models import Register


class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["user", "event", "is_present"]
        widgets = {"user": forms.HiddenInput}
        labels = {"is_present": "I will be there"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].widget.attrs["readonly"] = True
