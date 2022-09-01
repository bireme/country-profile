from django.db import models
from django.utils.translation import gettext_lazy as _, get_language
from django.core.validators import MinValueValidator, MaxValueValidator
from tinymce.models import HTMLField

from main import choices


INDICATOR_TYPE_CHOICES = (
    (1, _('Core')),
    (2, _('Suplementary')),
)

DATA_TYPE_CHOICES = (
    (1, _('PAHO')),
    (2, _('Public')),
)


BOOLEAN_CHOICES = (
    (True, _('Yes')),
    (False, _('No'))
)

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Country(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    code = models.CharField(_('Code'), max_length=55)
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        lang_code = get_language()
        country_name_local = self.name

        if lang_code != 'en':
            translation = CountryLocal.objects.filter(country=self.id, language=lang_code)
            if translation:
                country_name_local = translation[0].name

        return country_name_local

class CountryLocal(models.Model):
    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    country = models.ForeignKey(Country, verbose_name=_('Country'), on_delete=models.CASCADE)
    language = models.CharField(_('Language'), max_length=10, choices=choices.LANGUAGES_CHOICES[1:])
    name = models.CharField(_('Name'), max_length=255)


class Domain(models.Model):
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    number = models.SmallIntegerField(_('Domain number'))
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        lang_code = get_language()
        domain_name_local = self.name

        if lang_code != 'en':
            translation = DomainLocal.objects.filter(domain=self.id, language=lang_code)
            if translation:
                domain_name_local = translation[0].name

        return "Domain {}: {}".format(self.number, domain_name_local)

class DomainLocal(models.Model):
    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    domain = models.ForeignKey(Domain, verbose_name=_('Domain'), on_delete=models.CASCADE)
    language = models.CharField(_('Language'), max_length=10, choices=choices.LANGUAGES_CHOICES[1:])
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True)


class Indicator(models.Model):
    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"

    domain = models.ForeignKey(Domain, verbose_name=_('Domain'), on_delete=models.PROTECT)
    code = models.CharField(_('Code'), max_length=25, unique=True)
    name = models.CharField(_('Name'), max_length=255)
    type = models.SmallIntegerField(_('Core/Suplementary?'), choices=INDICATOR_TYPE_CHOICES, null=True, default=1)
    internal_notes = models.TextField(_('Internal notes'), blank=True)

    def __str__(self):
        lang_code = get_language()
        indicator_name_local = self.name

        if lang_code != 'en':
            translation = IndicatorLocal.objects.filter(indicator=self.id, language=lang_code)
            if translation:
                indicator_name_local = translation[0].name

        return "{} - {}".format(self.code, indicator_name_local)

class IndicatorLocal(models.Model):
    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    indicator = models.ForeignKey(Indicator, verbose_name=_("indicator"), on_delete=models.CASCADE)
    language = models.CharField(_('Language'), max_length=10, choices=choices.LANGUAGES_CHOICES[1:])
    name = models.CharField(_('Name'), max_length=255)


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    country = models.ForeignKey(Country, verbose_name=_('Country'), on_delete=models.PROTECT)
    description = HTMLField()

    def __str__(self):
        return "{}".format(self.country)


class ProfileLocal(models.Model):
    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    profile = models.ForeignKey(Profile, verbose_name=_("profile"), on_delete=models.CASCADE)
    language = models.CharField(_('Language'), max_length=10, choices=choices.LANGUAGES_CHOICES[1:])
    description = HTMLField()


class CountryIndicator(models.Model):
    class Meta:
        verbose_name = "Country indicator"
        verbose_name_plural = "Country indicators"

    profile = models.ForeignKey(Profile, verbose_name=_('Profile'), on_delete=models.PROTECT)
    indicator = models.ForeignKey(Indicator, verbose_name=_('Indicator'), on_delete=models.PROTECT)

    def __str__(self):
        return "{} | {}".format(self.profile, self.indicator)



class CountryIndicatorData(models.Model):
    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data"

    country_indicator = models.ForeignKey(CountryIndicator, verbose_name=_('Indicator'), on_delete=models.PROTECT)
    type = models.SmallIntegerField(_('Type'), choices=DATA_TYPE_CHOICES, null=True, blank=False, default=1)
    year = models.SmallIntegerField(_('Year'))
    info_text = models.CharField(_('Info (text)'), max_length=155, blank=True)

    info_numeric = models.DecimalField(_('Info (numeric)'), max_digits=19, decimal_places=2, default=0, blank=True, null=True)
    info_percent = models.DecimalField(_('Info (percentage)'), max_digits=5, decimal_places=2, default=0, validators=PERCENTAGE_VALIDATOR, blank=True, null=True)
    info_yesno = models.BooleanField(_('Info (Yes/No)'), choices=BOOLEAN_CHOICES, null=True, blank=True)

    reference_number = models.SmallIntegerField(_('Reference #'), null=True, blank=True)
    reference = models.TextField(_('Reference'), blank=True)

    def __str__(self):
        data = ''
        if self.info_text:
            data = self.info_text
        elif self.info_numeric:
            data = '{:,}'.format(self.info_numeric).rstrip('0').rstrip('.')
        elif self.info_percent:
            data = "{}%".format(self.info_percent)
        elif self.info_yesno != None:
            data = _('Yes') if self.info_yesno else _('No')

        data_year = "{} ({})".format(data, self.year)

        return data_year