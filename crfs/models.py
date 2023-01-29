from django.db import models
from simple_history.models import HistoricalRecords

from crfs.choices import SEX, YES_NO, STEROID, ANTIHISTAMINE, PROPHYLAXIS, ANTIBIOTIC, \
    ANTIFUNGAL, COMPLETE_TREATMENT
from .mixin import BaseUuidModel


class AplasticAnaemiaCrf(BaseUuidModel):
    name = models.CharField(
        verbose_name="Name:",
        max_length=80
    )

    dob = models.DateField(
        verbose_name="Date of birth:",
    )

    age = models.IntegerField(
        verbose_name="Age:",
    )

    sex = models.CharField(
        verbose_name="Sex",
        max_length=4,
        choices=SEX,
    )

    weight = models.IntegerField(
        verbose_name="Weight",
        help_text="in Kg"
    )

    file_no = models.CharField(
        verbose_name="File Number:",
        max_length=80,
    )

    region = models.CharField(
        verbose_name="Region",
        max_length=24
    )
    district = models.CharField(
        verbose_name="District",
        max_length=24
    )
    date_admission = models.DateField(
        verbose_name="Date Of Admission:",
    )
    symptom_present_today = models.TextField(
        verbose_name="Symptom presented today:",
    )
    duration_symptom_start = models.CharField(
        verbose_name="Duration since this symptom started?",
        max_length=120,
    )
    sigs_present_today = models.TextField(
        verbose_name="Sigs presented today",
        max_length=120,
    )
    duration_sigs_start = models.CharField(
        verbose_name="Duration since this sign started?",
        max_length=120,
    )
    wbc = models.DecimalField(
        verbose_name="WBC (K/uL):",
        decimal_places=3,
        max_digits=6,
    )
    anc = models.DecimalField(
        verbose_name="ANC (K/uL):",
        decimal_places=3,
        max_digits=6,
    )
    lymphocytes = models.DecimalField(
        verbose_name="Lymphocytes (K/uL):",
        decimal_places=3,
        max_digits=6,
    )
    haemoglobin = models.DecimalField(
        verbose_name="Haemoglobin (g/dL):",
        decimal_places=3,
        max_digits=6,
    )
    platelets = models.DecimalField(
        verbose_name="Platelets K/uL):",
        decimal_places=3,
        max_digits=6,
    )
    date_fbp = models.DateField(
        verbose_name="Date when Full Blood Picture done?",
    )
    reticulocyte_results = models.IntegerField(
        verbose_name="Reticulocyte result:",
    )
    reticulocyte_pcntg = models.IntegerField(
        verbose_name="Reticulocyte result(% percentage):",
    )
    reticulocyte_date = models.DateField(
        verbose_name="Date when reticulocyte done?",
    )
    bone_marrow_aspiration = models.CharField(
        verbose_name="Bone Marrow Aspiration Result",
        max_length=120
    )
    bone_marrow_aspiration_date = models.DateField(
        verbose_name="Date when Bone Marrow Aspiration done?",
    )
    bone_biopsy_aspiration = models.CharField(
        verbose_name="Bone Marrow Biopsy Result:",
        max_length=120
    )
    bone_biopsy_aspiration_date = models.DateField(
        verbose_name="Date when Bone Marrow Biopsy done?",
    )
    smear = models.CharField(
        verbose_name="Peripheral Smear Result:",
        max_length=120
    )
    smear_date = models.DateField(
        verbose_name="Date when Peripheral Smears done?",
    )
    hiv_test = models.CharField(
        verbose_name="HIV test Result:",
        max_length=120
    )
    hiv_test_date = models.DateField(
        verbose_name="Date when HIV done?",
    )
    hepatitis_b = models.CharField(
        verbose_name="Hepatitis B Result:",
        max_length=120
    )
    hepatitis_b_date = models.DateField(
        verbose_name="Date when Hepatitis B done?",
    )
    hepatitis_c = models.CharField(
        verbose_name="Hepatitis C Result:",
        max_length=120
    )
    hepatitis_c_date = models.DateField(
        verbose_name="Date when Hepatitis C done?",
    )
    ebv = models.CharField(
        verbose_name="EBV Result",
        max_length=120
    )
    ebv_date = models.DateField(
        verbose_name="Date when EBV done?",
    )
    cmv = models.CharField(
        verbose_name="CMV Result:",
        max_length=120
    )
    cmv_date = models.DateField(
        verbose_name="Date when CMV done?",
    )
    atg = models.CharField(
        verbose_name="Was ATG given?",
        max_length=6,
        choices=YES_NO,
    )
    atg_no_reasons = models.CharField(
        verbose_name="If no, give a reason:",
        max_length=120,
    )
    atg_dosage = models.IntegerField(
        verbose_name="if yes, Dosage (mg/Kg)",
    )
    atg_date = models.DateField(
        verbose_name="Date ATG was given?",
    )
    cyclosporine = models.CharField(
        verbose_name="Was Cyclosporine given?",
        max_length=6,
        choices=YES_NO,
    )
    cyclosporine_no_reasons = models.CharField(
        verbose_name="If no, give a reason:",
        max_length=120,
    )
    cyclosporine_dosage = models.IntegerField(
        verbose_name="if yes, Dosage (mg/Kg)",
    )
    cyclosporine_date = models.DateField(
        verbose_name="Date Cyclosporine given?",
    )
    steroid = models.CharField(
        verbose_name="Was Steroid given?",
        max_length=6,
        choices=YES_NO,
    )
    steroid_no_reasons = models.CharField(
        verbose_name="If no, give a reason:",
        max_length=120,
    )
    steroid_drug = models.CharField(
        verbose_name="Which steroid was given?",
        max_length=60,
        choices=STEROID,
    )
    steroid_drug_other = models.CharField(
        verbose_name="If other",
        max_length=120,
    )
    steroid_dosage = models.IntegerField(
        verbose_name="if yes, Dosage (mg/Kg)",
    )
    steroid_date = models.DateField(
        verbose_name="Date Cyclosporine given?",
    )
    antihistamine = models.CharField(
        verbose_name="Was Antihistamine given?",
        max_length=6,
        choices=YES_NO,
    )
    antihistamine_no_reasons = models.CharField(
        verbose_name="If no, give a reason:",
        max_length=120,
    )
    antihistamine_drug = models.CharField(
        verbose_name="If yes, Which Antihistamine was given?",
        max_length=60,
        choices=ANTIHISTAMINE,
    )
    antihistamine_drug_other = models.CharField(
        verbose_name="If other",
        max_length=120,
    )
    antihistamine_dosage = models.IntegerField(
        verbose_name="if yes, Dosage (mg/Kg)",
    )
    antihistamine_date = models.DateField(
        verbose_name="Date Antihistamine given?",
    )
    prophylaxis = models.CharField(
        verbose_name="Was Prophylaxis given?",
        max_length=6,
        choices=YES_NO,
    )
    prophylaxis_no_reasons = models.CharField(
        verbose_name="If no, give a reason:",
        max_length=120,
    )
    prophylaxis_drug = models.CharField(
        verbose_name="If yes, Which Prophylaxis was given?",
        max_length=60,
        choices=PROPHYLAXIS,
    )
    antibiotic_drug = models.CharField(
        verbose_name="If antibiotic",
        max_length=60,
        choices=ANTIBIOTIC,
    )
    ciprofloxacin_dosage = models.IntegerField(
        verbose_name="If ciprofloxacin, Dosage (mg/Kg)",
    )
    antibiotic_drug_other = models.CharField(
        verbose_name="If other",
        max_length=120,
    )
    antiviral_drug = models.CharField(
        verbose_name="If antiviral",
        max_length=60,
    )
    antiviral_dosage = models.IntegerField(
        verbose_name="If antiviral, Dosage (mg/Kg)",
    )
    antifungal_drug = models.CharField(
        verbose_name="If antifungal",
        max_length=60,
        choices=ANTIFUNGAL,
    )
    antifungal_dosage = models.IntegerField(
        verbose_name="If (itraconazole or fluconazole) (mg/kg):",
    )
    antifungal_other = models.IntegerField(
        verbose_name="If other:",
    )
    antifungal_dosage_other = models.CharField(
        verbose_name="If other, Dosage (mg/Kg)",
        max_length=120,
    )

    bone_marrow_transplant = models.CharField(
        verbose_name="Has Bone Marrow Transplant done?",
        max_length=6,
        choices=YES_NO,
    )

    bone_marrow_transplant_date = models.DateField(
        verbose_name="If yes, date when Bone Marrow Transplant done? ",
    )

    bone_marrow_transplant_no = models.TextField(
        verbose_name="If no, give reason :",
    )

    completed_treatment = models.CharField(
        verbose_name="Has patient completed treatment?",
        max_length=6,
        choices=YES_NO,
    )
    completed_treatment_date = models.DateField(
        verbose_name="If yes, when  the treatment was completed?",
    )
    treatment_outcome = models.CharField(
        verbose_name="If yes, what is the outcome?",
        max_length=24,
        choices=COMPLETE_TREATMENT,
    )
    not_completed_treatment = models.TextField(
        verbose_name="If no, give a reason:",
    )

    follow_up = models.CharField(
        verbose_name="Is follow up done?",
        max_length=6,
        choices=YES_NO,
    )
    follow_up_date = models.DateField(
        verbose_name="If yes, date when follow up done",
    )
    follow_up_date_fbp = models.DateField(
        verbose_name="Date when Full Blood Picture done?",
    )
    medical_history = models.TextField(
        verbose_name="Medical history:",
    )
    physical_examination = models.TextField(
        verbose_name="Physical examination:",
    )
    dopler_ultrasound = models.CharField(
        verbose_name="Dopler ultrasound done?",
        max_length=6,
        choices=YES_NO,
    )
    dopler_ultrasound_no = models.TextField(
        verbose_name="if no, give a reason:",
    )
    dopler_ultrasound_result = models.TextField(
        verbose_name="If yes, result:",
        null=True,
    )
    lab_investigation = models.CharField(
        verbose_name="Any laboratory investigation done?",
        max_length=120,
    )
    lab_investigation_result = models.TextField(
        verbose_name="If done, what was the result?",
        null=True,
    )
    other_note = models.TextField(
        verbose_name="Any clinical notes:",
        null=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.file_no

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Aplastic Anaemia CRF"
        verbose_name_plural = "Aplastic Anaemia CRF"


