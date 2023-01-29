from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from .models import AplasticAnaemiaCrf

admin.site.enable_nav_sidebar = False


@admin.register(AplasticAnaemiaCrf)
class AplasticAnaemiaCrfAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            "DEMOGRAPHIC",
            {
                "fields": (
                    "name",
                    "dob",
                    "age",
                    "sex",
                    "weight",
                    "file_no",
                    "region",
                    "district",
                    "date_admission",
                ),
            },
        ),
        (
            "SYMPTOMS",
            {
                "fields": (
                    "symptom_present_today",
                    "duration_symptom_start",
                ),
            },
        ),
        (
            "SIGNS",
            {
                "fields": (
                    "sigs_present_today",
                    "duration_sigs_start",
                ),
            },
        ),
        (
            "LABORATORY INVESTIGATION",
            {
                "fields": (
                    "wbc",
                    "anc",
                    "lymphocytes",
                    "haemoglobin",
                    "platelets",
                    "date_fbp",
                    "reticulocyte_results",
                    "reticulocyte_pcntg",
                    "reticulocyte_date",
                    "bone_marrow_aspiration",
                    "bone_marrow_aspiration_date",
                    "bone_biopsy_aspiration",
                    "bone_biopsy_aspiration_date",
                    "smear",
                    "smear_date",
                    "hiv_test",
                    "hiv_test_date",
                    "hepatitis_b",
                    "hepatitis_b_date",
                    "hepatitis_c",
                    "hepatitis_c_date",
                    "ebv",
                    "ebv_date",
                    "cmv",
                    "cmv_date",
                ),
            },
        ),
        (
            "TREATMENT",
            {
                "fields": (
                    "atg",
                    "atg_no_reasons",
                    "atg_dosage",
                    "atg_date",
                    "cyclosporine",
                    "cyclosporine_no_reasons",
                    "cyclosporine_dosage",
                    "cyclosporine_date",
                    "steroid",
                    "steroid_no_reasons",
                    "steroid_drug",
                    "steroid_drug_other",
                    "steroid_dosage",
                    "steroid_date",
                    "antihistamine",
                    "antihistamine_no_reasons",
                    "antihistamine_drug",
                    "antihistamine_drug_other",
                    "antihistamine_dosage",
                    "antihistamine_date",
                    "prophylaxis",
                    "prophylaxis_no_reasons",
                    "prophylaxis_drug",
                    "antibiotic_drug",
                    "ciprofloxacin_dosage",
                    "antibiotic_drug_other",
                    "antiviral_drug",
                    "antiviral_dosage",
                    "antifungal_drug",
                    "antifungal_dosage",
                    "antifungal_other",
                    "antifungal_dosage_other",
                    "bone_marrow_transplant",
                    "bone_marrow_transplant_date",
                    "bone_marrow_transplant_no",
                ),
            },
        ),
        (
            "OUTCOME",
            {
                "fields": (
                    "completed_treatment",
                    "completed_treatment_date",
                    "treatment_outcome",
                    "not_completed_treatment",
                ),
            },
        ),
        (
            "FOLLOW UP",
            {
                "fields": (
                    "follow_up",
                    "follow_up_date",
                    "follow_up_date_fbp",
                    "medical_history",
                    "physical_examination",
                    "dopler_ultrasound",
                    "dopler_ultrasound_no",
                    "dopler_ultrasound_result",
                    "lab_investigation",
                    "lab_investigation_result",
                    "other_note",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "name",
        "file_no",
        "dob",
        "age",
        "sex",
        "weight",
        "region",
        "district",
    )

    search_fields = (
        "file_no",
        "name",
    )

    list_filter = (
        "age",
        "sex",
        "dob",
        "weight",
        "region",
        "district",
    )

    radio_fields = {
        "atg": admin.VERTICAL,
        "cyclosporine": admin.VERTICAL,
        "steroid": admin.VERTICAL,
        "steroid_drug": admin.VERTICAL,
        "antihistamine": admin.VERTICAL,
        "antihistamine_drug": admin.VERTICAL,
        "prophylaxis": admin.VERTICAL,
        "prophylaxis_drug": admin.VERTICAL,
        "antibiotic_drug": admin.VERTICAL,
        "antifungal_drug": admin.VERTICAL,
        "bone_marrow_transplant": admin.VERTICAL,
        "treatment_outcome": admin.VERTICAL,
        "follow_up": admin.VERTICAL,
        "dopler_ultrasound": admin.VERTICAL,
    }
