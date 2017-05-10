# Motivation for the project

# Background

# Implementation and reference data set

## Reference data sets

## Synthetic data generators
### Synthetic data requirements:
<ul>
<li> PatientID </li>
<li> Gender </li>
<li> Marital status </li>
<li> Language </li>
<li> Ethnicity </li>
<li> Date of Birth </li>
    <ul>
    <li> Timestamp Format? </li>
    </ul>
<li> Age </li>
    <ul>
    <li> Range? </li>
    </ul>
<li> Diagnoses </li>
    <ul>
    <li>Which variables will this be correlated with?</li>
    </ul>
<li> Lab Results </li>
    <ul>
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

