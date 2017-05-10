# Motivation for the project

# Background

# Implementation and reference data set

## Reference data sets

## Synthetic data generators
### Synthetic data requirements:
<ul>
<li> PatientID </li>
    <ul>
    <li> AlphaNumeric </li>
    </ul>
<li> First Name </li>
    <ul>
    <li> Alpha characters </li>
    </ul>
<li> Last Name </li>
    <ul>
    <li> Alpha characters </li>
    </ul>
<li> SSN </li>
    <ul>
    <li> Format: 123456789 </li>
    </ul>
<li> Phone Number </li>
    <ul>
    <li> Format: 1234567890 </li>
    </ul>
<li> Street address of residence </li>
<li> City of residence </li>
<li> State of residence </li>
<li> Zip code of residence </li>
<li> City of birth</li>
<li> State of birth </li>
<li> Zip code of birth </li>
<li> Gender </li>
    <ul>
    <li> Male/Female OR 1/0?
    </ul>
<li> Marital status </li>
    <ul>
    <li> Single </li>
    <li> Married </li>
    <li> Divorced </li>
    <li> Separated </li>
    <li> Widowed </li>
    <li> Unknown </li>
    </ul>
<li> Language </li>
    <ul>
    <li> English </li>
    </ul>
<li> Ethnicity </li>
    <ul>
    <li> African American </li>
    <li> Asian </li>
    <li> White </li>
    <li> Unknown </li>
    </ul>
<li> Date of Birth </li>
    <ul>
    <li> Timestamp Format? </li>
    <li> Min/Max? </li>
    </ul>
<li> Age </li>
    <ul>
    <li> Range? </li>
    <li> Dynamic or static from a predefined date? </li>
    </ul>
<li> Provider </li>
<li> Physician </li>
<li> Chief Complaint </li>
    <ul>
    <li> ICD10 Codes </li>
    </ul>
<li> Primary Diagnoses </li>
    <ul>
    <li> ICD10 Codes </li>
    <li>Which variables will this be correlated with?</li>
    </ul>
<li> Diagnoses Explanation </li>
    <ul>
    <li> Text </li>
    </ul>
<li> Lab Results </li>
    <ul>
    <li> Date </li>
        <ul>
        <li> Associated with a specific admission? </li>
        </ul>
    <li> Units </li>
    <li> Value </li> 
    <li> Are these going to be correlated with each other? If one lab value is low, does another lab value need to be high? "For example in nonalcoholic fatty liver disease patients, assumptions would be needed about the inverse correlations of albumin levels and sodium levels with cardiovasular disease" as a comorbidity. Another example would be patients with "congestive heart failure would need to be associated with a high prevalence o diuretic use, advanced age, and a high prevalence of associated comorbidities, such as renal failure." - Uri Kartoun, "A Methodology to Generate Virtual Patient Repositories" </li>
    <li> If so, where do we find these correlations? </li>
    <li> What lab values will be included? </li>
    <li> Will lab value results be tied other demographic information, e.g gender, age, ethnicity, etc? </li>
    <li> Min/max values for each lab results? </li>
    <li> What other variables will lab results be tied to? e.g encounters, medications, images, etc, etc.. </li>
    </ul>
<li> Encounters </li>
    <ul>
    <li> What will be included here? </li>
    </ul>
<li> Images </li>
    <ul>
    <li> Will these be generated images or from a dataset? </li>
    <li> Will we be running analysis on the images or will there simply be a interpretation field? </li>
    </ul>
<li> Questions? </li>
    <ul>
    <li> Ideas for accounting for the complex time-dependent interactions between these factors? </li>
    </ul>
</ul>


## Error generating algorithms

