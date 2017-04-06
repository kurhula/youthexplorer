from django.conf import settings
from wazimap.data.tables import FieldTable, SimpleTable

# Define our tables for each profile so the data API can discover them.

# All profiles


# Census tables
if settings.WAZIMAP['default_profile'] == 'census':
    FieldTable(['age groups in 5 years'])
    FieldTable(['age in completed years'])
    FieldTable(['electricity for cooking', 'electricity for heating', 'electricity for lighting'])
    FieldTable(['energy or fuel for cooking'])
    FieldTable(['energy or fuel for heating'])
    FieldTable(['energy or fuel for lighting'])
    FieldTable(['gender'])
    FieldTable(['gender', 'marital status'])
    FieldTable(['gender', 'population group'])
    FieldTable(['gender', 'age groups in 5 years'])
    FieldTable(['highest educational level'])
    FieldTable(['highest educational level'], id="highesteducationallevel20", universe='Individuals 20 and older')
    FieldTable(['language'], description='Population by primary language spoken at home')
    FieldTable(['employed individual monthly income'], universe='Employed individuals')
    FieldTable(['official employment status'], universe='Workers 15 and over')
    FieldTable(['type of sector'], universe='Workers 15 and over')
    FieldTable(['population group'])
    FieldTable(['refuse disposal'])
    FieldTable(['source of water'])
    FieldTable(['toilet facilities'])

    FieldTable(['citizenship'])
    FieldTable(['province of birth'])
    FieldTable(['region of birth'])

    FieldTable(['access to internet'], universe="Households")
    FieldTable(['gender of household head', 'age of household head'], universe='Households')
    FieldTable(['annual household income', 'gender of household head'], universe='Households')
    FieldTable(['household goods'], universe='Households', denominator_key='total households')
    FieldTable(['tenure status'], universe='Households')
    FieldTable(['type of dwelling'], universe='Households')
    FieldTable(['age of household head', 'household size'], universe='Households')

    # child-specific tables
    FieldTable(['age in completed years'], id='ageincompletedyearssimplified')
    FieldTable(['present school attendance', 'age in completed years'], universe='Children 5 to 17')
    FieldTable(['mother alive', 'father alive'], universe='Children 14 and under')
    FieldTable(['official employment status'], id="officialemploymentstatus15to17", universe="Children 15 to 17")
    FieldTable(['highest educational level'], id="highesteducationallevel17", universe="17-year-old children")
    FieldTable(['individual monthly income'], id="individualmonthlyincome15to17", universe="Children 15 to 17 who are employed")
    FieldTable(['gender'], id='genderunder18', universe='Children under 18')

    # child-headed households
    FieldTable(['gender of head of household'], id="genderofheadofhouseholdunder18", universe='Households headed by children under 18')
    FieldTable(['annual household income'], id="annualhouseholdincomeunder18", universe='Households headed by children under 18')
    FieldTable(['type of main dwelling'], id='typeofmaindwellingunder18', universe='Households headed by children under 18')

    # Elections
    FieldTable(['party'], universe='Votes', id='party_votes_national_2014', description='2014 National Election results',
               dataset='2014 National Elections', year='2014')
    FieldTable(['party'], universe='Votes', id='party_votes_provincial_2014', description='2014 Provincial Election results',
               dataset='2014 Provincial Elections', year='2014')
    FieldTable(['party'], universe='Votes', id='party_votes_municipal_2011', description='2011 Municipal Election results',
               dataset='2011 Municipal Elections', year='2011')

    # Crime
    FieldTable(['crime'], universe='Crimes', dataset='Police Crime Statistics 2014', year='2014')

    # Simple tables
    SimpleTable(
        id='population',
        universe='Population',
        total_column=None,
        description='Total population',
        dataset='Census 2011',
        year='2011'
    )

    # Elections
    SimpleTable(
        id='voter_turnout_national_2014',
        universe='Registered voters',
        total_column='registered_voters',
        description='2014 National Election voter turnout',
        dataset='2014 National Elections',
        year='2014'
    )
    SimpleTable(
        id='voter_turnout_provincial_2014',
        universe='Registered voters',
        total_column='registered_voters',
        description='2014 Provincial Election voter turnout',
        dataset='2014 Provincial Elections',
        year='2014'
    )
    SimpleTable(
        id='votes_provincial_2014',
        universe='Valid votes',
        total_column='total_votes',
        description='2014 Provincial Election votes',
        dataset='2014 Provincial Elections',
        year='2014'
    )
    SimpleTable(
        id='votes_national_2014',
        universe='Valid votes',
        total_column='total_votes',
        description='2014 National Election votes',
        dataset='2014 National Elections',
        year='2014'
    )
    SimpleTable(
        id='voter_turnout_municipal_2011',
        universe='Registered and MEC7 voters',
        total_column='registered_voters',
        description='2011 Municipal Election voter turnout',
        dataset='2011 Municipal Elections',
        year='2011'
    )

# Youth
elif settings.WAZIMAP['default_profile'] == 'youth':
    # Demographics
    FieldTable(['age in completed years', 'gender'], id='youth_gender_age_in_completed_years', universe='Youth', year='2011')
    FieldTable(['population group', 'gender'], id='youth_gender_population_group', universe='Youth', year='2011')
    FieldTable(['age group in 10 years'], id='age_group_in_10_years', universe='Population', year='2011')

    # Education
    FieldTable(['completed grade9', 'gender'], id='youth_age_16_to_17_gender_completed_grade9', universe='Youth aged 16 to 17', year='2011')
    FieldTable(['education level', 'gender'], id='youth_age_20_to_24_gender_education_level', universe='Youth aged 20 to 24', year='2011')
    FieldTable(['attendance', 'gender', 'age in completed years'], id='youth_education_attendance_gender_age_incompleted_years', universe='Youth', year='2011')

    FieldTable(['year'], id='youth_average_mean_score_by_year', universe='Average mean score in both language and mathematics', year='2014', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year'], id='youth_average_language_score_by_year', universe='Average score in language', year='2014', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year', 'outcome'], id='youth_language_outcome_by_year', universe='Percentage passed in language', year='2014', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year'], id='youth_average_maths_score_by_year', universe='Average score in mathematics', year='2014', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year', 'outcome'], id='youth_maths_outcome_by_year', universe='Percentage passed in mathematics', year='2014', value_type='Float', stat_type='percentage', has_total=False)

    FieldTable(['year', 'outcome'], id='youth_matric_outcome_by_year', universe='Matric pass rate', year='2015', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year', 'outcome'], id='youth_matric_passes_as_percentage_of_grade8_enrolment_by_year', universe='Matric passes as a % of grade 8 enrolment', year='2015', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year', 'outcome'], id='youth_bachelor_passes_as_percentage_of_grade8_enrolment_by_year', universe='Bachelor passes as a % of grade 8 enrolment', year='2015', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year', 'outcome'], id='youth_student_dropout_rate_by_year', universe='Dropout rates between grade 10 and matric', year='2015', value_type='Float', stat_type='percentage', has_total=False)

    # Economic opportunities
    FieldTable(['employment status', 'gender'], id='youth_labour_force_official_gender', universe='Youth in the labour force - Official definition', description='Employment status of youth in the labour force', year='2011')
    FieldTable(['employment status', 'gender'], id='youth_labour_force_expanded_gender', universe='Youth in the labour force - Expanded definition', description='Employment status of youth in the labour force', year='2011')
    FieldTable(['employment status', 'gender'], id='youth_employment_status_gender', universe='Youth', year='2011')
    FieldTable(['employment education training', 'gender'], id='youth_employment_education_training_gender', universe='Youth', year='2011')
    FieldTable(['household employment'], id='youth_household_employment', universe='Youth living in households', description='Youth in households by adult employment', year='2011')
    FieldTable(['function type'], id='youth_difficulty_functioning', description='Youth experiencing difficulty in functioning', year='2011', universe='Youth with non-missing responses to the general health and functioning questions', denominator_key='youth')

    # Living environment
    FieldTable(['electricity access'], id='youth_electricity_access', universe='Youth living in households', year='2011')
    FieldTable(['toilet access'], id='youth_toilet_access', universe='Youth living in households', year='2011')
    FieldTable(['water access'], id='youth_water_access', universe='Youth living in households', year='2011')
    FieldTable(['dwelling type'], id='youth_dwelling_type', universe='Youth living in households', year='2011')
    FieldTable(['household crowded'], id='youth_household_crowded', universe='Youth living in households', year='2011')
    FieldTable(['income poverty', 'gender', 'population group'], id='youth_income_poverty_gender_population_group', universe='Youth', year='2011')
    FieldTable(['multidimensionally poor', 'gender', 'population group',], id='youth_multidimensionally_poor_gender_population_group', universe='Youth', year='2011')

    # Safety
    FieldTable(['age group'], id='crimes_victims_age_group', universe='Victims of crime per 10,000 population in age group', year='2015', has_total=False)
    FieldTable(['age group'], id='crimes_accused_age_group', universe='Accused of crime per 10,000 population in age group', year='2015', has_total=False)
    FieldTable(['type of offence'], id='youth_victims_offence_type', universe='Youth victims of crime, per 10,000 youth', year='2015', dataset='Police Crime Statistics 2006-2015')
    FieldTable(['type of offence'], id='youth_accused_offence_type', universe='Youth accused of crimes, per 10,000 youth', year='2015', dataset='Police Crime Statistics 2006-2015')
    FieldTable(['population group'], id='youth_victims_population_group', universe='Youth victims of crime, per 10,000 youth', year='2015', dataset='Police Crime Statistics 2006-2015', has_total=False)
    FieldTable(['population group'], id='youth_accused_population_group', universe='Youth accused of crimes, per 10,000 youth', year='2015', dataset='Police Crime Statistics 2006-2015', has_total=False)
    FieldTable(['gender'], id='youth_victims_gender', universe='Youth victims of crime, per 10,000 youth', year='2015', has_total=False, dataset='Police Crime Statistics 2006-2015')
    FieldTable(['gender'], id='youth_accused_gender', universe='Youth accused of crimes, per 10,000 youth', year='2015', has_total=False, dataset='Police Crime Statistics 2006-2015')
    FieldTable(['year'], id='youth_victims_year', universe='Youth victims of crime', year='2015', has_total=False, dataset='Police Crime Statistics 2006-2015')
    FieldTable(['year'], id='youth_accused_year', universe='Youth accused of crimes', year='2015', has_total=False, dataset='Police Crime Statistics 2006-2015')
    FieldTable(['type of crime', 'year'], id='crimes_type_of_crime_year', description='Contact and property crimes by year', year='2015', has_total=False, universe='Crimes', dataset='Police Crime Statistics 2006-2015')

    # Health
    FieldTable(['year'], id='youth_pregnancy_rate_year', universe='Teenage pregnancy rate by year', year='2015', value_type='Float', stat_type='percentage', has_total=False)
    FieldTable(['year'], id='youth_delivery_rate_year', universe='Teenage delivery rate by year', year='2015', value_type='Float', stat_type='percentage', has_total=False)

    FieldTable(['cause of death'], id='youth_causes_of_death_female', universe='Female youth causes of death', year='2013', value_type='Float')
    FieldTable(['cause of death'], id='youth_causes_of_death_male', universe='Male youth causes of death', year='2013', value_type='Float')

    # Simple Tables
    SimpleTable(
        id='youth',
        universe='Youth',
        total_column=None,
        description='Youth statistics',
        dataset='Census 2011',
        year='2011'
    )
    SimpleTable(
        id='youth_population',
        universe='Youth',
        total_column='total_pop',
        description='Youth population',
        dataset='Census 2011',
        year='2011'
    )
    SimpleTable(
        id='youth_mpi_score',
        universe='Youth',
        total_column=None,
        description='Youth MPI score',
        dataset='',
        year=''
    )

# ECD
elif settings.WAZIMAP['default_profile'] == 'ecd':
    FieldTable(['population group'])
    FieldTable(['age in completed years'])
    FieldTable(['age groups in 5 years'], id='womenagegroupsin5years15to44', universe='Women 15 to 44', description='Women of child bearing age', year='2011')
    FieldTable(['gender'], id='genderunder9', universe='Children under 9', year='2011')
    FieldTable(['gender of household head', 'age of household head'], universe='Households')
    FieldTable(['gender of head of household'], id="genderofheadofhouseholdunder18", universe='Households headed by children under 18')
    FieldTable(['type of dwelling'], universe='Households')
    FieldTable(['source of water'])
    FieldTable(['electricity for cooking', 'electricity for heating', 'electricity for lighting'])
    FieldTable(['toilet facilities'])

    # Simple Tables
    SimpleTable(
        id='hospitals_2012',
        universe='Number of hospitals',
        total_column='total_hospitals',
        description='2012 number of hospitals',
        dataset='2012 National Hospital Survey',
        year='2012'
    )
    SimpleTable(
        id='schools_2015',
        universe='Number of schools',
        total_column=None,
        description='2015 number of schools',
        dataset='Q1 2015 National Ordinary Schools Master List',
        year='2015'
    )
    SimpleTable(
        id='ecd_centres_by_registration',
        universe='ECD centres',
        total_column='total_ecd_centres',
        description='ECD centres, by registration status of centre',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )
    SimpleTable(
        id='ecd_centres_by_type',
        universe='ECD centres',
        total_column='total_ecd_centres',
        description='ECD centres, by type of centre',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )
    SimpleTable(
        id='ecd_children_enrolled',
        universe='Number of children enrolled in ECD Centres',
        total_column=None,
        description='Number of children enrolled in ECD Centres',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )
    SimpleTable(
        id='ecd_educators',
        universe='Number of practitioners per child in ECD Centres',
        total_column=None,
        description='Number of practitioners per child in ECD Centres',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )
    SimpleTable(
        id='ecd_grade_r',
        universe='Grade R learners',
        total_column=None,
        description='Grade R learners',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )
    SimpleTable(
        id='ecd_grants',
        universe='Learners receiving social grants',
        total_column=None,
        description='Learners receiving social grants',
        dataset='Audit of ECD Centres - National Report',
        year='2013'
    )

