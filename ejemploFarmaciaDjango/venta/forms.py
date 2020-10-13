from django import forms

class VentaForm():
    nombre = forms.CharField(
        label='Nombre',
        max_length=25,
    )

    droga = forms.CharField(
        label='Droga',
        max_length=25,
    )

    obraSocial = forms.CharField(
        label='Obra Social',
        max_length=25,
    )

    plan = forms.CharField(
        label='Plan',
        max_length=25,
    )

    importe = forms.FloatField(
        label='Importe',
    )

    fechaHora = forms.DateTimeField(
        label = 'Fecha y Hora'
    )