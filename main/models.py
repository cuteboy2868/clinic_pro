from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, ValidationError
from .validators import ImageFileValidator
import qrqode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    full_name = models.CharField(max_length=55, db_index=True, verbose_name='toliq ismi')
    address = models.CharField(max_length=75, null=True, blank=True, verbose_name='manzili')
    phone_number = models.CharField(max_length=13, unique=True, verbose_name='telefon raqami', validators=[
        RegexValidator(
            regex='^[/+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid number',
        )])

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'User'


class Employe(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name='foydalanuvchi')
    status = models.IntegerField(default=5, verbose_name='statusi',choices=(
        (1, 'doctor'),
        (2, 'manager'),
        (3, 'admin'),
        (4, 'nurse'),
        (4, 'director'),
        (4, 'cooker'),
    ))
    salary = models.PositiveIntegerField(verbose_name='ish haqi')
    work_time = models.CharField(max_length=255, verbose_name='ish vaqti')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='xona')
    exprience = models.ForeignKey(max_length=255, verbose_name='tajriba')
    bio = models.CharField(max_length=255, verbose_name='biosi')
    age = models.IntegerField(verbose_name='yosh')
    departament = models.ForeignKey(to='Departament', on_delete=models.CASCADE, verbose_name='departamenti')


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Employe'
        verbose_name_plural = 'Employes'


class Patient(models.Model):
    doctor = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='doktorlar')
    full_name = models.CharField(max_length=255, verbose_name='toliq ism')
    age = models.IntegerField(default=18, verbose_name='yosh')
    gender = models.IntegerField(default=1, verbose_name='jinsi',  choices=(
        (1, 'Male'),
        (2, 'Female'),
    ))
    address = models.CharField(max_length=255, verbose_name='joylashuv')
    photo = models.ImageField(upload_to='photos/', verbose_name='rasmi' , validators=[ImageFileValidator()])
    phone_number = models.CharField(max_length=13, verbose_name='telefon raqamia')
    extra_phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='ekstra_telefon_raqam')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='xona')
    bio = models.TextField(verbose_name="ma'lumotlari")
    stayed_day = models.DateTimeField
    payment_status = models.IntegerField(default=1, verbose_name='tolov statusi', choices=(
        (1, 'unpaid'),
        (2, 'part_paid'),
        (3, 'paid'),
    ))

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='ism')
    capacity = models.IntegerField(null=True, blank=True, verbose_name='kengligi')
    status = models.CharField(max_length=255, verbose_name='statusi', default=2, choices=(
        (1, 'Lux'),
        (2, 'Standart'),
        (3, 'other')
    ))
    is_booked = models.BooleanField(default=False, verbose_name='jadvalga kiritilgani')
    departament = models.ForeignKey(to='Departament', on_delete=models.CASCADE, verbose_name='departament')
    equipment = models.ForeignKey(to='Equipment', on_delete=models.CASCADE, verbose_name='aslaxa')
    other_info = models.TextField(null=True, blank=True, verbose_name='boshqa infolar')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


    def __str__(self):
        return self.name


class Comment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='bemor')
    status = models.IntegerField(default=1, verbose_name='statusi',choices=(
        (1, 'comment'),
        (1, 'complain'),
        (1, 'suggestion'),
    ))
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    qr_qode = models.ImageField(upload_to='qr_qodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qr_qode, QRcode(
            version=1,
            error_correction=qrcode.constans.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.user.full_name}")
        qr.make(fit=True)
        img = qr_make_image(fill_colors="black", back_color="white")


        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

        class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'


class Income(models.Model):
    amount = models.IntegerField(verbose_name='soni')
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True, verbose_name='yaratilgan vaqti')

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'


class Revenu(models.Model):
    amount = models.IntegerField(verbose_name='soni')
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True, verbose_name='yaratilgan vaqti')

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = 'Revenues'

class Cassa(models.Model):
    total_summa = models.PositiveIntegerField(verbose_name='aniq summa miqdori')

    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Cassas'

class Operator(models.Model):
    employee = models.ManyToManyField(to='Employee', verbose_name='employi')
    date_time = models.DateTimeField(default=True, verbose_name='sana vaqti')
    start_time = models.CharField(max_length=255, verbose_name='boshlanish vaqti')
    end_time = models.CharField(max_length=255, verbose_name='yakunlanish vaqti')
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='bemor')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='xona')
    created_at = models.DateTimeField(auto_now=True, verbose_name='yaratilgan vaqti')

    class Meta:
        verbose_name = 'Operator'
        verbose_name_plural = 'Operators'


class Departament(models.Model):
    name = models.CharField(max_length=255, verbose_name='nomi')

    class Meta:
        verbose_name = 'Departament'
        verbose_name_plural = 'Departaments'

class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name='ismi')
    number = models.CharField(max_length=200, verbose_name='soni')
    extra_info = models.CharField(max_length=255, verbose_name='extra infosi')

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return self.name

class Info_about_clinic(models.Model):
    total_patients_number = models.CharField(max_length=255, verbose_name='aniq bemorlar soni')
    total_employee_number = models.CharField(max_length=255, verbose_name='aniq employlar soni')
    bio = models.TextField(verbose_name='biosi')
    address = models.CharField(max_length=255, verbose_name='joylashuvi')
    phone_number = models.CharField(max_length=13, verbose_name='telefon raqami')

    class Meta:
        verbose_name = 'Info_about_clinic'
        verbose_name_plural = 'Info_about_clinics'


class Attendence(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    data = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)


    class Meta:
        unique_together = ['employee', 'data']


    def clean(self):
        if self.check_out and self.check_out < self.check_in:
            raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.full_name} = {self.data}"

# Create your models here.