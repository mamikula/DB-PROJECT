from django import forms

types =(
    ("balastowy","balastowy"),
    ("mieczowy","mieczowy")
)
class CityForm(forms.Form):
    city = forms.CharField(label="Znajdź miasto",max_length=100,required=False)

class DimensionsForm(forms.Form):
    length = forms.FloatField(label="Podaj długość:")
    depth = forms.FloatField(label="Podaj zanurzenie:")
    width = forms.FloatField(label="Podaj szerokość:")
    type= forms.ChoiceField(label="Podaj typ:",choices=types)

class DataForm(forms.Form):
    yachtID=forms.CharField(label="Podaj numer rejestracyjny jachtu:",max_length=6,min_length=6)
    name=forms.CharField(label="Imię:")
    surname=forms.CharField(label="Nazwisko:")
    dateFrom=forms.DateField(label="Początek rezerwacji(rrrr-mm-dd):")
    dateTo=forms.DateField(label="Koniec rezerwacji(rrrr-mm-dd):")


class ReservationForm(forms.Form):
    IN = forms.CharField(label="Numer rejestracyjny jachtu:",min_length=6,max_length=6,required=False)
    name=forms.CharField(label="Imię*:")
    surname=forms.CharField(label="Nazwisko*:")

class EditReservationForm(forms.Form):
    dateFrom = forms.DateField(label="Początek rezerwacji(rrrr-mm-dd):")
    dateTo = forms.DateField(label="Koniec rezerwacji(rrrr-mm-dd):")