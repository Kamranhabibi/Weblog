from django import forms
from django.core.validators import ValidationError
from weblog.models import Input

#create forms here .

#---------------------------------------------------------------------------------------------------------------------
class ContactUS(forms.Form):
    years_choices = ['1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999'
                                                                                                     '2000', '2001',
                     '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'
                                                                             '2010', '2011', '2012', '2013', '2014',
                     '2015', '2016', '2017', '2018', '2019', '2020',
                     '2021', '2022', '2023', '2024', '2025', '2026']

    color_choices_multi = [
        ('blue ', ' Blue'), ('red', 'Red'), ('green', 'Green')
    ]
    color_choices_single = [
        ('withe ', ' Withe'), ('bleak', 'Bleak'), ('yellow', 'Yellow')
    ]






    your_name = forms.CharField(max_length=15 , label='Your Name')
    your_email = forms.EmailField(label="Your Email")
    city = forms.CharField(label='Your City', max_length=16 , required=False)
    subject = forms.CharField(max_length=25,label='Subject')
    body = forms.TimeField(label='Write Your Massage')

    birthday = forms.DateField(widget=forms.SelectDateWidget(years=years_choices,attrs={'class':'form-control'}), required=False )
    multi= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'content'}), choices=color_choices_multi)
    single = forms.ChoiceField(widget=forms.RadioSelect,choices=color_choices_single)
    i = forms.CharField(widget=forms.EmailInput)
    def clean(self):
        your_name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')

        if your_name == subject:
            raise ValidationError('name & subject are same' , code='name_text')

#---------------------------------------------------------------------------------------------------------------------
#class Massage_form(forms.Form):
    #name = forms.CharField(max_length=100)
    #subject = forms.CharField()
    #body = forms.CharField(widget=Textarea)
    #email = forms.EmailField()                 [ one of the methods of making modeled forms ]

#---------------------------------------------------------------------------------------------------------------------

                                       # The Best way to create modeled forms !!!!
class Massage_form(forms.ModelForm):
    class Meta:
        model = Input
        fields = '__all__'    #-----> Select All fields
       # exclude = 'name'     -----> Except ** name ** field , if : there are 5 fields bring 4 folds except 1
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write Subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write Email'}),
        }