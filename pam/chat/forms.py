from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from .hooks import hookset
from .models import Message


class UserModelChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return hookset.display_name(obj)


class UserModelMultipleChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return hookset.display_name(obj)

class NewMsgForm(forms.ModelForm):
    subject = forms.CharField(label='Thema')
    content = forms.CharField(label='Nachricht eingeben', widget=forms.Textarea)

    class Meta:
        model = Message
        fields =["subject", "content"]

class NewMessageForm(forms.ModelForm):

    subject = forms.CharField(label='Thema:')
    to_user = UserModelChoiceField(queryset=get_user_model().objects.none(), disabled = False, empty_label=None)
    content = forms.CharField(label='Nachricht eingeben:', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["to_user"].queryset = hookset.get_user_choices(self.user)
        if self.initial.get("to_user") is not None:
            qs = self.fields["to_user"].queryset.filter(pk=self.initial["to_user"])
            self.fields["to_user"].queryset = qs

    def save(self, commit=True):
        data = self.cleaned_data
        return Message.new_message(
            self.user, [data["to_user"]], data["subject"], data["content"]
        )

    class Meta:
        model = Message
        fields = ["to_user", "subject", "content"]


class NewMessageFormMultiple(forms.ModelForm):
    subject = forms.CharField()
    to_user = UserModelMultipleChoiceField(get_user_model().objects.none())
    content = forms.CharField(label='Nachricht eingeben:',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["to_user"].queryset = hookset.get_user_choices(self.user)
        if self.initial.get("to_user") is not None:
            qs = self.fields["to_user"].queryset.filter(pk__in=self.initial["to_user"])
            self.fields["to_user"].queryset = qs

    def save(self, commit=True):
        data = self.cleaned_data
        return Message.new_message(
            self.user, data["to_user"], data["subject"], data["content"]
        )

    class Meta:
        model = Message
        fields = ["to_user", "subject", "content"]


class MessageReplyForm(forms.ModelForm):

    content = forms.CharField(label='Nachricht eingeben:',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.thread = kwargs.pop("thread")
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        return Message.new_reply(
            self.thread, self.user, self.cleaned_data["content"]
        )

    class Meta:
        model = Message
        fields = ["content"]
