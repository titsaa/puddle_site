from django import forms

from .models import ConversationMessage


# class ConversationMessageForm(forms.ModelForm):
#     class Meta:
#         model = ConversationMessage
#         fields = ('content',)
#         widget = {
#             'content': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border bg-gray-100','placeholder': 'Type your message'})
#         }

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border', 'placeholder': 'Type your message'})
        }
