import streamlit as st

# Set up the main structure of the Streamlit App
def main():
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    sections = ["Introduction", "EDA", "Missingness Handling", "Encoding and Scaling", 
                "PCA and Dimensionality Reduction", "Modeling"]
    selected_section = st.sidebar.selectbox("Select a section", sections)

    # Display corresponding section based on user selection
    if selected_section == "Introduction":
        introduction()
    elif selected_section == "EDA":
        eda()
    elif selected_section == "Missingness Handling":
        missingness()
    elif selected_section == "Encoding and Scaling":
        encoding_scaling()
    elif selected_section == "PCA and Dimensionality Reduction":
        pca_section()
    elif selected_section == "Modeling":
        modeling()

# Introduction Section
def introduction():
    st.title("Child Mind Institute — Problematic Internet Use")
    st.image("DALL·E 2024-12-02 11.55.25.webp", use_column_width=True)
    st.header("Introduction")
    st.markdown("""
        The Healthy Brain Network (HBN) dataset is a clinical sample of about five-thousand 5-22 year-olds who have
        undergone both clinical and research screenings. The objective of the HBN study is to find biological markers
        that will improve the diagnosis and treatment of mental health and learning disorders from an objective
        biological perspective. Two elements of this study are being used for this project: internet usage behavior data
        physical activity data (wrist-worn accelerometer data, fitness assessments and questionnaires), the later is 
        not covered in this web app. The goal of this project is to predict from this data a participant's **Severity
        Impairment Index** (`sii`), a standard measure of problematic internet use. The majority of measures are 
        missing for most participants. In particular, the target sii is missing for a portion of the participants in 
        the training set.
        """)
    st.markdown("""
        ### Tabular Data - HBN Instruments
        The tabular data in *train.csv* and *test.csv* comprises measurements from a variety of instruments. The
        fields within each instrument are described in *data_dictionary.csv*. These instruments are:

        * `Demographics` - Information about *age* and *sex* of participants.
        * `Internet Use` - *Number of hours* of using computer/internet per day.
        * `Children's Global Assessment Scale` - Numeric scale used by mental health clinicians to rate the general 
        functioning of youths under the age of 18.
        * `Physical Measures` - Collection of *blood pressure*, *heart rate*, *height*, *weight* and *waist*, and
        *hip* measurements.
        * `FitnessGram Vitals and Treadmill` - Measurements of cardiovascular fitness assessed using the NHANES 
        treadmill protocol.
        * `FitnessGram Child` - Health related physical fitness assessment measuring five different parameters 
        including *aerobic capacity*, *muscular strength*, *muscular endurance*, *flexibility*, and *body composition*.
        * `Bio-electric Impedance Analysis` - Measure of key body composition elements, including *BMI*, *fat*, 
        *muscle*, and *water content*.
        * `Physical Activity Questionnaire` - Information about children's participation in vigorous activities over 
        the last 7 days.
        * `Sleep Disturbance Scale` - Scale to *categorize sleep disorders* in children.
        * `Actigraphy` - Objective measure of ecological physical activity through a research-grade biotracker.
        * `Parent-Child Internet Addiction Test (PCIAT)` - 20-item scale that measures characteristics and behaviors 
        associated with compulsive use of the Internet including compulsivity, escapism, and dependency.
        * **Note** in particular the field PCIAT-PCIAT_Total. The target sii for this competition is derived from 
        this field as described in the data dictionary: 0 for None, 1 for Mild, 2 for Moderate, and 3 for Severe. 
        Additionally, each participant has been assigned a unique identifier id.
        """)
    st.markdown("Each data science step towards this dataset can be reviewed and explored in the side and top bars!")
    st.markdown("")
    
# EDA Section
def eda():
    st.header("Exploratory Data Analysis (EDA)")

    # Subsections within EDA
    eda_subsections = ["Age & Gender", "SII and PCIAT", "Internet Use", "Children Global Assessment Scale", 
                       "Physical Measures", "Bioelectric Impedance Analysis", "FitnessGram", "Sleep Disturbance", 
                       "Physical Activity Questionnaire"]
    eda_selected = st.selectbox("Select EDA subsection", eda_subsections)

    if eda_selected == "Age & Gender":
        age_gender()
    elif eda_selected == "SII and PCIAT":
        sii_visualization()
    elif eda_selected == "Internet Use":
        internet_use()
    elif eda_selected == "Children Global Assessment Scale":
        cgas_analysis()
    elif eda_selected == "Physical Measures":
        physical_measure_analysis()
    elif eda_selected == "Bioelectric Impedance Analysis":
        bia_analysis()
    elif eda_selected == "FitnessGram":
        FitnessGram()
    elif eda_selected == "Sleep Disturbance":
        sleep_analysis()
    elif eda_selected == "Physical Activity Questionnaire":
        paq_analysis()

# Age and Gender Subsection
def age_gender():
    st.write("Let's first take a quick look at the basic demographics.")
    st.subheader("Age Group Distribution")
    table_age = """
    | Age Group         | Count (%)       |
    |-------------------|----------------|
    | Children (5-12)   | 2919 (73.71%)  |
    | Teenager (13-19)  | 980 (24.75%)   |
    | Young Adults (20-22) | 61 (1.54%)  |
    """
    st.markdown(table_age)
    st.subheader("Sex Category Distribution")
    table_gender = """
    | Basic_Demos-Sex-Category | Count (%)      |
    |--------------------------|----------------|
    | Male                     | 2484 (62.73%)  |
    | Female                   | 1476 (37.27%)  |
    """
    st.markdown(table_gender)
    st.image("Gender.png", use_column_width=True)
    st.markdown("""
    **Notes:**
    - The distribution of enrollment by season is relatively balanced.
    - There is a higher number of males across most age groups, with fewer females particularly visible in younger 
    age groups.
    """)

# SII Visualization Subsection
def sii_visualization():
    st.subheader("Severity Impairment Index (SII) Visualization")
    st.write("Here you will find visualizations of SII distribution and related statistics.")
    st.image("Distribution of SII.png", use_column_width=True)
    st.image("Distribution of PCIAT_Total.png", use_column_width=True)
    st.markdown("""
    **Notes:**
    - 40% of the samples are not affected by the Internet use.
    - 31% of the samples are not evaluated at all, which is quite a large missingness value!
    - Only ~10% of the samples are affected by internet use moderately or severely.
    - 446 samples scored 0 on all PCIAT questions.
    """)
    st.write("Now, let's take a closer look here!")
    st.image("SII and PCIAT_Total Box.png", use_column_width=True)
    st.image("SII by Age Pi-Chart.png", use_column_width=True)
    
    table_md = """
    | Age Group          | Missing       | 0 (None)       | 1 (Mild)       | 2 (Moderate)   | 3 (Severe)     | Total |
    |--------------------|---------------|----------------|----------------|----------------|----------------|-------|
    | Children (5-12)    | 850 (29.1%)   | 1360 (46.6%)   | 499 (17.1%)    | 204 (7.0%)     | 6 (0.2%)       | 2919  |
    | Teenager (13-19)   | 340 (34.7%)   | 217 (22.1%)    | 223 (22.8%)    | 172 (17.6%)    | 28 (2.9%)      | 980   |
    | Young Adults (20-22) | 37 (60.7%)  | 12 (19.7%)     | 8 (13.1%)      | 3 (4.9%)       | 1 (1.6%)       | 61    |
    """
    st.markdown(table_md)
    st.markdown("""
    **Notes:**
    - Higher sii scores are generally associated with older age groups.
    - There is an increasing-decreasing trend seen in the box plots of PCIAT_Total scores with age groups indicating
    that the peak of internet-related problems occur during teenage period.
    - Based on the pie-chart, 
        - sii scores are more skewed towards the None and Mild categories.
        - Young adults have a significant missingness.
        - Teenagers seem to have more balanced categories.
                """)

# Internet Use Subsection
def internet_use():
    st.subheader("Internet Use Analysis")
    st.write("Here you will find visualizations of the internet use distribution and related statistics.")
    st.image("Internet Use Box.png", use_column_width=True)
    st.image("Internet Use Pi.png", use_column_width=True)
    table_md = """
    | Gender | Missing       | < 1hr/day       | ~ 1hr/day       | ~ 2hr/day      | > 3hr/day      | Total |
    |--------|---------------|---------------- |---------------- |----------------|----------------|-------|
    | Female | 271 (18.4%)   | 569 (38.6%)     | 139 (9.4%)      | 353 (23.9%)    | 144 (9.8%)     | 1476  |
    | Male   | 388 (15.6%)   | 955 (38.4%)     | 274 (11.0%)     | 651 (26.2%)    | 216 (8.7%)     | 2484  |
    """
    st.markdown(table_md)
    st.markdown("""
    **Notes:**
    - Based on the bar plots, 16.6% of the Internet usage data is missing. 38.5% of samples used the Internet less 
    than hour a day.
    - Box plots shows that higher daily internet use is correlated with older age. However, considerable overlap 
    in age ranges within each Internet usage category is observed.
    - The pie charts for age groups are well aligned and shows the same.
    - Internet use in both genders is almost similar.
    """)
    st.image("Internet Use Box2.png", use_column_width=True)
    st.image("Internet Use Pi2.png", use_column_width=True)
    st.markdown("""
                **Notes:**
                - In the box plots, despite the considerable overlap between the different SII and internet use categories,
                we see a positive trend between PIU impairment and internet use, with people with higher SII scores spending
                more time online.
                - However, when the relationship between PCIAT_Total and hours of Internet use is further broken down
                by age group (bottom boxplot), the non-linear relationship between age, Internet use and PCIAT_Total 
                score emerges, with adolescents standing out as the most affected age group across all categories of 
                Internet use.
                - The pie charts also show that there is a significant proportion of participants (83 in total),
                of all ages, who spend very little time online (less than 1 hour per day) but have high SII scores 
                (20.7% with SII 2 - moderately impaired and 14.7% with SII = 3 - severely impaired).
                """)

# Children Global Assessment Scale Subsection
def cgas_analysis():
    st.subheader("Children Global Assessment Scale")
    st.markdown("""
    The Children's Global Assessment Scale (CGAS) is a clinician-rated tool used to assess the overall
    functioning of children and adolescents. It evaluates a child’s psychological, social, and academic
    functioning on a scale from 1 to 100, with higher scores indicating better functioning. The scale helps
    in determining the severity of a child's mental health issues, such as the degree of impairment in
    various domains of life, including relationships, school performance, and behavior. It is commonly
    used in clinical settings for monitoring progress, making treatment decisions, and conducting research
    on child mental health. The scores are divided into categories ranging from very low to high
    functioning to guide interventions.
                """)
    st.image("CGAS.png", use_column_width=True)
    st.image("CGAS2.png", use_column_width=True)
    st.image("CGAS3.png", use_column_width=True)
    st.markdown("""
    **Notes:**
    - Since the CGAS is a measure of general functioning, and the SII reflects the severity of the
    impact of Internet use on that functioning, it is to be expected that this feature, along with
    Internet use, to be the most important in predicting the SII.
    - The majority of individuals have CGAS scores between 51-80 (79.7%), i.e. sporadic difficulties to only slight impairments
    - Two participants have extreme difficulty in functioning.
    - It would be expected the higher the SII, the lower the median CGAS score, but the decrease is very small here.
    - However, there are no participants with the highest SII scores (3 or severely problematic internet use) who have
    good CGAS scores (81-100: good/superior functioning in all domains). This suggests that parental responses to the
    PCIAT questionnaire (our target variable) may reflect some effects of PIU on global health and functioning.
    """)

# Physical Measure Subsection
def physical_measure_analysis():
    st.subheader("Physical Measure")
    st.markdown("Let's analyze different aspects of the physical measures. Begin with general statistcs and distribution.")
    st.image("Physical Measure1.png", use_column_width=True)
    st.markdown("""Looking at the histograms, the range for each parameter looks okay, however, the following table show
                another story with non-physical zero values that must be replaces with nan!""")
    table_md = """
    | Physical Measurement          | Count   | Mean        | Std         | Min  | 25%        | 50%        | 75%        | Max        | Missing |
    |--------------------------------|---------|-------------|-------------|------|------------|------------|------------|------------|---------|
    | Physical-BMI                   | 3022.0  | 19.33   | 5.11    | 0.0  | 15.86   | 17.94  | 21.57  | 59.13  | 938     |
    | Physical-Height                | 3027.0  | 55.94   | 7.47    | 33.0 | 50.00   | 55.00  | 62.00  | 78.50  | 933     |
    | Physical-Weight                | 3076.0  | 89.03   | 44.56   | 0.0  | 57.20   | 77.00  | 113.80 | 315.00 | 884     |
    | Physical-Waist_Circumference   | 898.0   | 27.27   | 5.56    | 18.0 | 23.00   | 26.00  | 30.00  | 50.00  | 3062    |
    | Physical-Diastolic_BP          | 2954.0  | 69.64   | 13.61   | 0.0  | 61.00   | 68.00  | 76.00  | 179.00 | 1006    |
    | Physical-HeartRate             | 2967.0  | 81.59   | 13.66   | 27.0 | 72.00   | 81.00  | 90.50  | 138.00 | 993     |
    | Physical-Systolic_BP           | 2954.0  | 116.98  | 17.06   | 0.0  | 107.00  | 114.00 | 125.00 | 203.00 | 1006    |
    """
    st.markdown(table_md)
    st.markdown("""Let's take a quick look at statistics without missingness. Missingness issue will be addressed 
            extensively in the next section.""")
    table_md = """
    | Physical Measurement          | Count   | Mean       | Std        | Min   | 25%      | 50%      | 75%      | Max       | Missing |
    |--------------------------------|---------|------------|------------|-------|----------|----------|----------|-----------|---------|
    | Physical-BMI                   | 3015 | 19.38      | 5.03       | 8.52  | 15.89    | 17.95    | 21.59    | 59.13     | 945     |
    | Physical-Height                | 3027 | 55.95      | 7.47       | 33.00 | 50.00    | 55.00    | 62.00    | 78.50     | 933     |
    | Physical-Weight                | 3015 | 90.84      | 43.16      | 31.80 | 58.20    | 77.80    | 114.30   | 315.00    | 945     |
    | Physical-Waist_Circumference   | 898  | 27.28      | 5.57       | 18.00 | 23.00    | 26.00    | 30.00    | 50.00     | 3062    |
    | Physical-Diastolic_BP          | 2953 | 69.67      | 13.55      | 11.00 | 61.00    | 68.00    | 76.00    | 179.00    | 1007    |
    | Physical-HeartRate             | 2967 | 81.60      | 13.67      | 27.00 | 72.00    | 81.00    | 90.50    | 138.00    | 993     |
    | Physical-Systolic_BP           | 2953 | 117.02     | 16.93      | 49.00 | 107.00   | 114.00   | 125.00   | 203.00    | 1007    |
    """
    st.markdown(table_md)
    st.image("Physical Measure2.png", use_column_width=True)
    st.markdown("""
    **Notes:**
    - There are individuals who are unusually tall for their age group or who are extremely overweight.
    - There are also a few outliers in the waist circumference measurements, which are possible artifacts (e.g. 100 cm
    for a weight of 40 kg).
    - The problem with data cleaning here is that we cannot guess which of the data is correct. For example, we may see
    an unrealistic combination of a waist circumference of 100cm and a weight of 40kg for a participant, but where is
    the error in the waist circumference or the weight? Or a height of around 175cm for a child of 7 has the height or
    age been entered incorrectly? Or this is true data and the child has gigantism or another disorder related to the
    growth hormone?
                """)
    table_md = """
    | Physical-Diastolic_BP | Physical-Systolic_BP | Physical-HeartRate |
    |-----------------------|----------------------|--------------------|
    | 1140                 | 179.0                | 139.0              |
    | 1879                 | 117.0                | 114.0              |
    | 2386                 | 76.0                 | 116.0              |
    | 3344                 | 98.0                 | 96.0               |
    """
    st.markdown(table_md)
    st.markdown("""
    **Note:**
    - We also know that systolic BP cannot be lower than diastolic BP!
    """)
    st.markdown("Now, here is another small problem turns out based on our EDA!")
    table_md = """
    | Physical-Diastolic_BP | Physical-Systolic_BP | Physical-HeartRate |
    |-----------------------|----------------------|--------------------|
    | 1140                 | 179.0                | 139.0              |
    | 1879                 | 117.0                | 114.0              |
    | 2386                 | 76.0                 | 116.0              |
    | 3344                 | 98.0                 | 96.0               |
    """
    st.markdown(table_md)
    st.markdown("""
    **Note:**
    - We also know that systolic BP cannot be lower than diastolic BP! So, a few more nan samples are added!
    """)
    st.image("Physical Measure3.png", use_column_width=True)
    st.markdown("""
        **Note:**
        - The absence of a clear direct correlation between heart rate and blood pressure in the plots suggests that
        the measurements were likely taken in a resting state or under non-stressful conditions.
        """)
    st.image("Physical Measure4.png", use_column_width=True)
    st.markdown("""
        - There does not appear to be a strong, clear correlation between body mass index (BMI) and systolic blood
        pressure (BP).
        - As expected, there is a strong positive correlation between systolic and diastolic BP, but there are notable
        cases of isolated systolic or diastolic hypertension.
        """)
    st.image("Physical Measure5.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - The positive correlation with the target is for height, weight, and waist circumference, which means that
        taller and fatter people tend to have a higher SII. But as these physical parameters increase with age, and we
        already know that SII tends to be highest in adolescents, this could indicate that they acts as a proxy for age
        (likely reflect age-related trends).
        - Cardiovascular measures (systolic blood pressure, diastolic blood pressure and heart rate) also change with
        age, but do not vary as drastically between childhood and adolescence as physical measures, and may not be as
        sensitive to behaviours such as internet use. They also have a higher degree of variability, as we saw in the
        graphs above, so the weak correlation may indicate that cardiovascular health is not strongly linked to PIU, or
        that these data are just more scattered and noisy and the relationship with PIU is diluted.
        - Overall, these preliminary analysis help us addressing the missingness issues!
        """)

# Bioelectric Impedance Analysis Subsection
def bia_analysis():
    st.subheader("Bioelectric Impedance")
    st.markdown("""Bioelectric Impedance Analysis (BIA) is a technique used to measure the composition of the body by
                assessing its resistance to electrical flow. It works by passing a small, safe electrical current
                through the body and measuring the impedance (resistance) encountered. Since different tissues in
                the body (such as fat, muscle, and bone) conduct electricity differently, BIA can estimate various
                body parameters, including body fat percentage, lean mass, and total body water. BIA is commonly used
                in health assessments, fitness evaluations, and clinical settings as a non-invasive and relatively
                quick method to monitor body composition.""")
    st.image("BIA1.png", use_column_width=True)
    st.image("BIA2.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - The distribution of the various bioelectrical impedance analysis measurements in the data set indicates that
        most of them are not useful: highly skewed, with the majority of participants having marginal values and a few
        outliers (potential measurement errors).
        - Some variables, such as Fat Mass Index and Body Fat Percentage, show implausible negative values, and almost
        all - extreme high values, indicating potential data quality issues.
        """)

# FitnessGram Vitals and Treadmill Subsection
def FitnessGram():
    st.subheader("FitnessGram Vitals and Treadmill")
    st.markdown("""
                The Treadmill test, part of the FitnessGram's aerobic capacity assessment, involves running or 
                walking on a treadmill to assess endurance. It may measure the maximum stage of the treadmill test 
                that the individual can complete, which correlates with aerobic fitness. The Treadmill test is 
                typically used to evaluate how long an individual can maintain a certain pace or intensity before 
                reaching fatigue.
                """)
    st.image("VT1.png", use_column_width=True)
    st.markdown("Let's take a look into possible missingness.")
    table_md = """
    | Fitness_Endurance-Max_Stage | Fitness_Endurance-Time_Mins | Fitness_Endurance-Time_Sec |
    |----------------------------|-----------------------------|----------------------------|
    | 420                        | 4.0                         | 6.0                        |
    | 1470                       | 26.0                        | NaN                        |
    | 2907                       | 1.0                         | 26.0                       |
    | 3666                       | 2.0                         | NaN                        |
    """
    st.markdown(table_md)
    st.markdown("""
        **Notes:**
        - It's possible that during data entry minutes or seconds were left blank (entered as NaN) when they should 
        have been recorded as 0 minutes/seconds. While the missing seconds are not as important, the missing minutes
        may actually be missing and treating them as 0 would give an incorrect test result. It is better to 
        just remove these suspicious cases.
        - It should also be noted that the age range for participants with Fitness_Endurance-Max_Stage data is 6-12 years.
        - Let's also calculate the total time in seconds and see the statistics again.
        """)
    table_md = """
    | Fitness Endurance Measurement     | Count  | Mean       | Std        | Min  | 25%   | 50%   | 75%   | Max   | Missing |
    |-----------------------------------|--------|------------|------------|------|-------|-------|-------|-------|---------|
    | Fitness_Endurance-Max_Stage       | 739.0  | 4.97       | 1.86       | 0.0  | 4.0   | 5.0   | 6.0   | 28.0  | 3221    |
    | Fitness_Endurance-Total_Time_Sec  | 739.0  | 469.91     | 188.72     | 5.0  | 362.0 | 476.0 | 590.5 | 1200.0| 3221    |
    """
    st.markdown(table_md)
    st.subheader("FitnessGram Child")
    st.markdown("""
        The FitnessGram is a comprehensive fitness assessment tool used primarily in schools to evaluate the physical 
        fitness levels of children. It is designed to measure various aspects of physical fitness, including aerobic
        capacity, muscular strength, endurance, flexibility, and body composition.

        One of the key components of the FitnessGram is the Pacer Test (Progressive Aerobic Cardiovascular Endurance 
        Run), which measures aerobic capacity. Other assessments include the curl-up test (to assess abdominal strength),
        push-up test (for upper body strength), and sit-and-reach test (to evaluate flexibility). These tests are used
        to evaluate whether children are meeting the fitness standards and help identify areas where they may need 
        improvement.

        The data from the FitnessGram is used to track students' fitness over time and can be an important tool for 
        promoting health and encouraging physical activity in schools.
        """)
    st.image("VT2.png", use_column_width=True)
    table_md = """
    | FGC Measurement      | Count   | Mean      | Std       | Min  | 25%   | 50%   | 75%     | Max   | Missing |
    |----------------------|---------|-----------|-----------|------|-------|-------|---------|-------|---------|
    | FGC Curl Up           | 2322.0  | 11.26     | 11.81     | 0.0  | 3.0   | 9.00  | 15.75   | 115.0 | 1638    |
    | FGC Grip Strength (non-dominant)         | 1074.0  | 22.42     | 10.83     | 0.0  | 15.1  | 20.05 | 26.60   | 124.0 | 2886    |
    | FGC Grip Strength (dominant)          | 1074.0  | 23.52     | 11.15     | 0.0  | 16.2  | 21.20 | 28.18   | 123.8 | 2886    |
    | FGC Pull Up           | 2310.0  | 5.58      | 7.39      | 0.0  | 0.0   | 3.00  | 9.00    | 51.0  | 1650    |
    | FGC Sit & Reach (left side)          | 2305.0  | 8.69      | 3.43      | 0.0  | 7.0   | 9.00  | 11.00   | 21.7  | 1655    |
    | FGC Sit & Reach (right side)          | 2307.0  | 8.81      | 3.42      | 0.0  | 7.0   | 9.00  | 11.00   | 21.0  | 1653    |
    | FGC Trunk lift           | 2324.0  | 9.25      | 2.99      | 0.0  | 7.0   | 10.00 | 12.00   | 22.0  | 1636    |
    """
    st.markdown(table_md)
    st.markdown("""
                **Notes:**
                - Most of the distributions are skewed towards lower performance totals. Strangely, a greater 
                proportion of participants achieved a healthy fitness zone for the trunk lift. I would expect different
                ranges for each zone, but the values for different zones overlap significantly. This may be because the
                zone ranges are different for different ages.
                - In addition, it also doesn't make sense to call this a children's FitnessGram, since participants of almost
                all ages (5-21) were tested.
                """)
    st.image("VT3.png", use_column_width=True)
    st.markdown("""
        **Note:**
        - Positive correlation between multiple physical performance measures and the PCIAT_Total score simply does not 
        make senes, as it suggests that physical performance improves as PIU severity increases ...
        """)

# Sleep Disturbance Subsection
def sleep_analysis():
    st.subheader("Sleep Disturbance")
    st.markdown("""
    The Sleep Disturbance Scale (SDS) is a tool used to assess the severity and impact of sleep disturbances on an
    individual's daily functioning. It typically consists of a series of questions or items that evaluate various
    aspects of sleep, such as the quality of sleep, frequency of disturbances (e.g., waking up during the night,
    difficulty falling asleep), and the impact on daytime functioning (e.g., fatigue, mood). The scale is often used
    in clinical or research settings to help diagnose sleep disorders or to monitor changes in sleep patterns over
    time. It is particularly useful for identifying individuals who may be experiencing sleep problems related to
    conditions like insomnia, sleep apnea, or other health issues.
    """)
    st.image("Sleep Disturbance1.png", use_column_width=True)
    st.image("Sleep Disturbance2.png", use_column_width=True)
    st.markdown("""
        **Note:**
        - Both the raw and T-scores for sleep disturbance are moderately variable, with some extreme values indicating
        severe sleep disturbances in a subset of participants.
        - Both scores hava a similar distribution given each gender.
        """)
    table_md = """
    | SDS Measurement   | Count   | Mean      | Std       | Min  | 25%   | 50%   | 75%   | Max   | Missing |
    |-------------------|---------|-----------|-----------|------|-------|-------|-------|-------|---------|
    | SDS_Total_Raw     | 2609.0  | 41.09     | 10.43     | 17.0 | 33.0  | 39.0  | 46.0  | 96.0  | 1351    |
    | SDS_Total_T       | 2606.0  | 57.76     | 13.20     | 38.0 | 47.0  | 55.0  | 64.0  | 100.0 | 1354    |
    """
    st.markdown(table_md)

# Physical Activity Questionnaire Subsection
def paq_analysis():
    st.markdown("""
        The Physical Activity Questionnaire (PAQ) is a tool commonly used to assess an individual's physical
        activity levels. It typically involves a self-reported survey that asks respondents about the frequency,
        duration, and intensity of various physical activities they engage in over a specific time period, such
        as the past week or month.
        """)
    st.subheader("Physical Activity Questionnaire (Adolescents)")
    st.image("PA1.png", use_column_width=True)
    st.subheader("Physical Activity Questionnaire (Children)")
    st.image("PA2.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - Age range for Adolescents (with PAQ_A_Total data): 13 - 18 years.
        - Age range for Children (with PAQ_C_Total data): 7 - 17 years.
        - The division into adolescents and children seems to be incorrect (participants with data in the children 
        columns (PAQ_C_Total) are 7 - 17 years old - overlapping with those with non-missing data in the adolescents 
        columns - 13 - 18 years old).
        - Physical activity levels are fairly stable over the seasons, with only minor variations, although are 
        slightly lower in the fall and winter for adolescents and children, respectively.
        - There are many missing values for these features
        """)

# Missingness Section
def missingness():
    st.header("Missingness Handling")

    # Subsections within Missingness Handling
    missingness_subsections = ["Overview", "Weight, Height, & Waist", "Blood Pressures & Heart Rate", 
                               "Bio-Electric Impedence", "Fitness Gram Child", "Internet Use", "Sleep Disturbance",
                               "Children's Global Assessment Scale", "Remaining Features", "SII & PCIAT"]
    missingness_selected = st.selectbox("Select Missingness Handling Subsection", missingness_subsections)

    if missingness_selected == "Overview":
        overview_miss()
    elif missingness_selected == "Weight, Height, & Waist":
        whw_miss()
    elif missingness_selected == "Blood Pressures & Heart Rate":
        bphr_miss()
    elif missingness_selected == "Bio-Electric Impedence":
        bia_miss()
    elif missingness_selected == "Fitness Gram Child":
        fgc_miss()
    elif missingness_selected == "Internet Use":
        iu_miss()
    elif missingness_selected == "Sleep Disturbance":
        sd_miss()
    elif missingness_selected == "Children's Global Assessment Scale":
        cgas_miss()
    elif missingness_selected == "Remaining Features":
        remaining_miss()
    elif missingness_selected == "SII & PCIAT":
        sii_pciat_miss()

# Missingness Overview Subsection
def overview_miss():
    st.markdown("Let's take a look at the missingness heat map and percentage various features.")
    st.image("overview_miss1.png", use_column_width=True)
    st.image("overview_miss2.png", use_column_width=True)
    st.markdown("""Some of the features have seriouse missingness, while potentiall palying an important role for
                the prediction task. In the next subsections, this missingness will be addressed, step by step. 
                Moreover, in most of our missingness handling efforts, Iterative Imputer BayesianRidge and KNN 
                imputation methods are utilized.""")

# Missingness of Weight, Height, and Waist Subsection
def whw_miss():
    st.image("imp_weight_height.png", use_column_width=True)
    st.image("imp_bmi.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - Age, Height, and Weight are used for the imputation task.
        - Concerning the Iterative Imputer BayesianRidge method, a minimum value of 30 is specified to help the 
        imputation as the min of weigth and height is 31.8lb and 33.0 in.
        - Both methods resulted into almost the same imputation as they display the similar distribution. However,
        the Iterative Imputer BayesianRidge method is chosen due to a relatively better performance in the imputed
        distribution of weight.
        - Distribution of the imputed BMI also seems reasonable.
        """)
    st.markdown("""Since weight and height have already been imputed, let's use them along with age to impute waist 
                circumference.""")
    st.image("imp_waistcircum.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - Waist circumference had 77.32% missingness as it is evident from the above scatter plot. However, 
        it seems the Bayes method has a more reasonable performance.
        """)

# Missingness of Blood Pressures and Heart Rate Subsection
def bphr_miss():
    st.markdown("""Upon plotting various scatter plots, weight, systolic bp, diastolic bp, and heart rate are imputed
                together.""")
    st.image("imp_bphr1.png", use_column_width=True)
    st.image("imp_bphr2.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - Similar to the previous subsection, a min limit value of 10.0 is provided for the Bayes method as the min
        value of the diastolic bp is 11.
        - Again, both imputation methods more or less resulted into the same output.
        - Both distribution and heatmap of the imputed data seem to preserve the same shape and correlations.
        """)

# Missingness of the Internet Use Subsection
def iu_miss():
    st.markdown("""
        As concluded in its corresponding EDA section, this parameter can potentially play an important role in 
        predicting the SII. So, its missingness is handled carefully.
        
        Given each SII value, the missingness in the internet use is handled proportion to their original missingness.
        In other words, missing values are filled such that the relative percentage of each internet use category does
        not change drastically.
        """)
    st.markdown("This is the imputed pie-chart.")
    st.image("imp_internetuse.png", use_column_width=True)
    st.markdown("And this is the non-imputed pie-chart.")
    st.image("Internet Use Pi2.png", use_column_width=True)

# Missingness of Bio-electric Impedence Analysis Subsection
def bia_miss():
    st.markdown("""
        Owing to the following reasons, features related to bio-electric impedence analysis are dropped!
        
        **Notes:**
        - Roughly half of the data is missing.
        - std of most of the features are two or three times greater than their corresponding mean value.
        - Most of them have extreme min or max values.
        - Most of them have a very skewed distribution.
        """)
    st.image("BIA2.png", use_column_width=True)
    st.image("BIA1.png", use_column_width=True)

# Missingness of Fitness Gram Child Subsection
def fgc_miss():
    st.markdown("""
        All the fitness gram child features are imputed using age, gender, and bmi as auxiliary features. So, let's 
        first take a quick look at the correlation heatmap of these features.
        """)
    st.image("imp_fgc1.png", use_column_width=True)
    st.markdown("Now, here is the comparison non-imputed and KNN imputed features.")
    st.image("imp_fgc2.png", use_column_width=True)

# Missingness of Sleep Disturbance Subsection
def sd_miss():
    st.markdown("Let's first see which potential parameter be an auxilary parameter for imputing the scores.")
    st.image("imp_sd1.png", use_column_width=True)
    st.markdown("Both raw and T scores are imputed using BMI.")
    st.image("imp_sd2.png", use_column_width=True)

# Missingness of Children's Global Assessment Scale Subsection
def cgas_miss():
    st.markdown("""
        For this parameter, the aim is to preserve the distribution of the scores.
        
        Here, the score is imputed using age, bmi, and weight as auxillary features.
        """)
    st.image("imp_cgas.png", use_column_width=True)

# Missingness of the Remaining Features Subsection
def remaining_miss():
    st.markdown("""
        Let's take a look at the missingness percentages up to now. We have imputed many features while
        dropping some other features!
        """)
    st.image("imp_remaining1.png", use_column_width=True)
    st.markdown("""
        **Notes:**
        - Physical activity questionnaires for both childer and adolescents have a significant missingness. Moreover, 
        since these features are somehow reflected in other features, their missingness is ignored and they are dropped
        for the next analysis.
        - With a similar logic, the minute and second values for the fitness endurance are also dropped.
        - Let's take a bit closer look at the missingness of the target values in the next subsection.
        """)

# Missingness of the SII and PCIAT Score Subsection
def sii_pciat_miss():
    st.markdown("""
        In this project, roughly 31% of SII and PCIAT score is missing. However, this number is achieved after some
        effort described below.
        
        First of all, it must be noted that PCIAT and SII have a clear mapping as shown in the following table.
        """)
    table_md = """
    | SII Category | Minimum PCIAT Total Score | Maximum PCIAT Total Score |
    |--------------|---------------------------|---------------------------|
    | 0.0          | 0.0                       | 30.0                      |
    | 1.0          | 31.0                      | 49.0                      |
    | 2.0          | 50.0                      | 79.0                      |
    | 3.0          | 80.0                      | 93.0                      |
    """
    st.markdown(table_md)
    st.markdown("""
        Let's also have a brief overview of PCIAT:
        
        The Parent-Child Internet Addiction Test (PC-IAT) assesses internet addiction in children and adolescents by 
        combining self-assessment from the child and observations from the parent. It covers topics like time spent 
        online, emotional impact, and consequences on daily life, school, and social interactions. The test aims to
        provide a comprehensive view of internet use and its effects from both perspectives. In the present, scores 
        for 20 questions are provided with missing values that cuase reduction in the total score.
        """)
    st.markdown("""
        Second, let's review the mean imputation used for PCIAT question scores and total score.
        
        Out of all the samples with 'non-missing' sii value, 65 samples had at least one missing value in one of the 
        questions in the PCIAT. This missing value would result into an artificail decrease in the PCIAT total score
        as it is equal to sum of all PCIAT question scores. Therefore, it was decided to detecet samples with no more
        than 3 missing question scores and use mean-imputation (with rounding!) to fill the missing scores. At the end,
        only 3 samples remain with more than 3 missing scores.
        """)
    
    st.markdown("""
        Ultimately, let's take a look at the missing scores before and after the mean-imputation.
        """)
    st.image("imp_pciat1.png", caption='Part of the missing PCIAT score before mean imputation.')
    st.image("imp_pciat2.png", caption='Part of the missing PCIAT score after mean imputation.')
    st.markdown("Let's see the missing percentage one more time!")
    st.image("imp_remaining2.png", use_column_width=True)
    st.markdown("""
        The ultimate goal of this project is to predict SII or equivalently PCIAT toal score. But, both (not 
        surperisingly by now), have 31% missingness after the mean-imputation effort, described above.
        
        For sure there are some sophisticated ways to address this missingness in the target values. But, these 
        efforts would be literally translated prediction/classification task that is supposed to be answered in the
        modeling section. Therefore, for now, use the row-wise deletion for handling this missingness, which decreases 
        3960 samples to 2733.
        """)

# Encoding and Scaling Section
def encoding_scaling():
    st.header("Encoding and Scaling")
    st.markdown("Let's take a look at the remaining parameters and their type:")
    table_md = """
    | Instrument                         | Field                                    | Type             |
    |------------------------------------|------------------------------------------|------------------|
    | Demographics                       | Basic_Demos-Age                          | float            |
    | Demographics                       | Basic_Demos-Sex                          | categorical int  |
    | Children's Global Assessment Scale | CGAS-CGAS_Score                          | int              |
    | Physical Measures                  | Physical-BMI                             | float            |
    | Physical Measures                  | Physical-Height                          | float            |
    | Physical Measures                  | Physical-Weight                          | float            |
    | Physical Measures                  | Physical-Waist_Circumference             | int              |
    | Physical Measures                  | Physical-Diastolic_BP                    | int              |
    | Physical Measures                  | Physical-HeartRate                       | int              |
    | Physical Measures                  | Physical-Systolic_BP                     | int              |
    | FitnessGram Vitals and Treadmill   | Fitness_Endurance-Max_Stage              | int              |
    | FitnessGram Child                  | FGC-FGC_CU                               | int              |
    | FitnessGram Child                  | FGC-FGC_GSND                             | float            |
    | FitnessGram Child                  | FGC-FGC_GSD                              | float            |
    | FitnessGram Child                  | FGC-FGC_PU                               | int              |
    | FitnessGram Child                  | FGC-FGC_SRL                              | float            |
    | FitnessGram Child                  | FGC-FGC_SRR                              | float            |
    | FitnessGram Child                  | FGC-FGC_TL                               | int              |
    | Parent-Child Internet Addiction Test | PCIAT-PCIAT_Total                      | int              |
    | Sleep Disturbance Scale            | SDS-SDS_Total_Raw                        | int              |
    | Sleep Disturbance Scale            | SDS-SDS_Total_T                          | int              |
    | Internet Use                       | PreInt_EduHx-computerinternet_hoursday   | categorical int  |
    | SII                                | Severity Impairment Index                | categorical int  |
    """
    st.markdown(table_md)
    st.markdown("""
        **Notes:**
        - Binary Encoding (Demographics - Gender): Since 'Basic_Demos-Sex' is already binary (0, 1), we do not need
        additional encoding. 
        -  Ordinal Encoding (Internet Use and SII): Given the order of values (0: less than 1h, 1: around 1h, etc.) or
        (sii = 1 is more sever than sii = 0, etc.), Ordinal Encoding is appropriate since the categories have a 
        natural ordering.
        - For the next step, which is PCA, PCIAT-PCIAT_Total will be removed as it has a one-by-one mapping to SII.
        - All the continuous numerical parameters (int/float) are standard scaled.
        """)

# PCA and Dimensionality Reduction Section
def pca_section():
    st.header("PCA and Dimensionality Reduction Section")
    st.markdown("""
        In this section, each step of PCA and the ultimate dimensionality reduction aim is presented. 
        Let's get into it!
        """)
    st.markdown("""
        - **Step 0:** As reviewed in the previous section, features are now ready (cleaned, scaled, and encoded) to start 
        the PCA.
        - **Step 1:** Dropping the target variable (sii), the scree plot determines the number of required PCs. 12 PCs
        are chosen as they explained 95% of the cumulative variability. The feature numbers are now halfed!
        """)
    st.image("pc_1.png", use_column_width=True)
    st.markdown("""
        - **Step 2:** Let's visualize the data points, eventhough high differentiability is not expected!
        """)
    st.image("pc_2.png", use_column_width=True)
    st.markdown("""
        - **Step 3:** Just out of curiosity, let's see how would K-Mean clustering work!
        """)
    st.image("pc_3.png", use_column_width=True)
    st.markdown("""
        - **Step 4:** Now, let's visualize the contribution of features in PCs.
        """)
    st.image("pc_4.png", use_column_width=True)
    st.image("pc_5.png", use_column_width=True)
    st.markdown("""
        Features are as follows:
        
        Basic_Demos-Age, Basic_Demos-Sex, CGAS-CGAS_Score, Physical-BMI, Physical-Height, 
        Physical-Weight, Physical-Waist_Circumference, Physical-Diastolic_BP, Physical-HeartRate, 
        Physical-Systolic_BP, FGC-FGC_CU, FGC-FGC_GSND, FGC-FGC_GSD, FGC-FGC_PU, FGC-FGC_SRL, FGC-FGC_SRR, FGC-FGC_TL
        SDS-SDS_Total_Raw, SDS-SDS_Total_T, PreInt_EduHx-computerinternet_hoursday, sii.
        """)

# Modeling Section
def modeling():
    st.header("Modeling")
    st.write("This section will cover the different predictive models developed and their evaluation metrics.")

    # Subsections within Modeling
    modeling_subsections = ["Overview", "Imbalance Issue", "Gradient Boosting Classifier", 
                            "Random Forest", "Model Comparison"]
    modeling_selected = st.selectbox("Select Modeling Subsection", modeling_subsections)

    if modeling_selected == "Overview":
        overview_model()
    elif modeling_selected == "Imbalance Issue":
        imbalance_model()
    elif modeling_selected == "Gradient Boosting Classifier":
        gbm_model()
    elif modeling_selected == "Random Forest":
        rf_model()
    elif modeling_selected == "Model Comparison":    
        comp_model()

# Overview of Modeling Subsection
def overview_model():
    st.markdown("""
        Since our goal is to predict/classify the sii score, which is an ordinal target variable, we should consider
        models that are well-suited for classification (since sii takes discrete values like 0, 1, 2, 3) or regression
        (since it has a clear order). Owing to the imablance issue in the dataset, two models that are initially 
        suitable for such datasets are choses.
        
        1. Gradient Boosting Classifier (GBM):
            
        - Learns sequentially by focusing on the errors of the previous iterations.
        - Handles imbalanced datasets well when tuned
        - Can achieve high precision and recall by optimizing for specific metrics.
        - It is excellent for capturing patterns in datasets where class boundaries are non-linear and noisy.
        
        2. Random Forest Classifier:
            
        - It creates multiple independent decision trees, reducing overfitting.
        - Handles class imbalance better out of the box due to internal bootstrapping and options.
        - Robust to noisy and imbalanced data.
        
        Let's start with addressing the imbalance issue in the next subsection.
        """)

# Imabalance Subsection
def imbalance_model():
    st.markdown("""
        Let's, first, see how this problem affects the performance of the model in predicting the minority class.
        
        Here is the detailed classification report of GradientBoostingClassifier model with default hyper parameters.
        """)
    st.markdown("**Accuracy Score:** 0.55")
    classification_report_md = """
    | Class | Precision | Recall | F1-Score | Support |
    |-------|-----------|--------|----------|---------|
    | 0.0   | 0.66      | 0.83   | 0.73     | 315     |
    | 1.0   | 0.27      | 0.21   | 0.24     | 140     |
    | 2.0   | 0.38      | 0.14   | 0.20     | 86      |
    | 3.0   | 0.00      | 0.00   | 0.00     | 6       |

    | Metric          | Precision | Recall | F1-Score | Support |
    |-----------------|-----------|--------|----------|---------|
    | **Accuracy**    | -         | -      | 0.55     | 547     |
    | **Macro Avg**   | 0.32      | 0.30   | 0.29     | 547     |
    | **Weighted Avg**| 0.50      | 0.55   | 0.51     | 547     |
    """
    st.markdown(classification_report_md)
    st.markdown("""
        Let's also review some of the key performance parameters here as well.
        
        - **Precision**: 0.66 for class `0.0`, meaning that 66% of instances predicted as `0.0` were correct.
        - **Recall**: 0.83 for class `0.0`, indicating that 83% of the actual `0.0` instances were correctly predicted.
        - **F1-Score:** The harmonic mean of precision and recall. It balances precision and recall, especially
        when the data is imbalanced.
        - **Support:** The number of true instances for each class in the dataset.
        """)
    st.markdown("""
        **Notes:**
        - Class `0.0` dominates the dataset (315 instances), while class `3.0` is very rare (6 instances). This imbalance
        skews the model's performance.
        - The model performs well on class `0.0` (high precision, recall, and F1-Score), likely because of its prevalence
        in the dataset.
        - Performance on minority classes (`1.0`, `2.0`, `3.0`) is poor, indicating that the model struggles to generalize
        for underrepresented classes.
        - Use techniques like oversampling minority classes (SMOTE) or adjusting class weights in the loss function.
        """)
    st.markdown("Let's use SMOTE and fine tune it using grid search")
    code = """
    # Define the model and pipeline
    classifier = GradientBoostingClassifier()
    smote = SMOTE()
    pipeline = Pipeline(steps=[('smote', smote), ('classifier', classifier)])

    # Define parameter grid
    param_grid = {
        'smote__sampling_strategy': ['auto', 'minority'],
        'smote__k_neighbors': [3, 4, 5, 6, 10]
    }

    # Perform grid search
    grid_search = GridSearchCV(
        pipeline,
        param_grid,
        scoring='f1_weighted',
        cv=5,
        verbose=1,
        n_jobs=2)
    grid_search.fit(X_train, y_train)
    """
    st.code(code, language='python')
    st.markdown("""
        And here is the result: Best SMOTE parameters:
        ```python
        {'smote__k_neighbors': 5, 'smote__sampling_strategy': 'minority'}
        ```
        """)

# Gradient Boosting Classifier Subsection
def gbm_model():
    st.markdown("""
                Once we are done with tuning the SMOTE method to (at least) partially address the imbalance issue, let's
                get into tuning the Gradient Boosting Classifier.
                """)
    code = """
    param_grid_gb = {
        'classifier__n_estimators': [50, 100, 200, 300],
        'classifier__learning_rate': [0.01, 0.05, 0.1, 0.15],
        'classifier__max_depth': [3, 5, 7],
    }

    pipeline.set_params(smote__k_neighbors=5, smote__sampling_strategy='minority')

    # Perform grid search for GradientBoostingClassifier
    grid_search_gb = GridSearchCV(
        pipeline,
        param_grid_gb,
        scoring='f1_weighted',
        cv=5,
        verbose=1,
        n_jobs=-1  # Use all available processors
    )
    grid_search_gb.fit(X_train, y_train)
    """
    st.code(code, language='python')
    st.markdown("""
        And here is the result: Best Gradient Boosting Classifier parameters:
        ```python
        Best GradientBoosting parameters: 
        {'classifier__learning_rate': 0.1, 'classifier__max_depth': 7, 'classifier__n_estimators': 100}
        ```
        """)
    st.markdown("Finally, let's see the performance of the best pipeline!")
    classification_report_md = """
    | Class       | Precision | Recall | F1-Score | Support |
    |-------------|-----------|--------|----------|---------|
    | 0.0         | 0.64      | 0.81   | 0.72     | 315     |
    | 1.0         | 0.28      | 0.19   | 0.23     | 140     |
    | 2.0         | 0.38      | 0.16   | 0.23     | 86      |
    | 3.0         | 0.14      | 0.50   | 0.22     | 6       |

    | Metric      | Precision | Recall | F1-Score | Support |
    |-----------------|-------|--------|----------|---------|
    | **Accuracy**    |       |        | 0.54     | 547     |
    | **Macro Avg**   | 0.36  | 0.42   | 0.35     | 547     |
    | **Weighted Avg**| 0.51  | 0.54   | 0.51     | 547     |
    """
    st.markdown(classification_report_md)
    st.markdown("""
        **Notes:**
        - The results after fine-tuning indicate that there has been some improvement, especially considering the
        challenging class imbalance in the dataset.
        - Class `0.0` (Majority Class): Precision (0.64) and Recall (0.81) are solid, resulting in a strong F1-score
        (0.72).
        - Class `1.0` and `2.0` (Minority Classes): These classes still struggle, with Recall at 0.19 for `1.0` and 0.16
        for `2.0`. Precision for class `2.0` is higher (0.38), but the imbalance and overlap between classes make them
        harder to predict accurately. Efforts like SMOTE and GradientBoosting fine-tuning improved minority class
        performance somewhat but not substantially.
        - Class `3.0` (Rare Class): Remarkably, the Recall for `3.0` is 0.50, meaning half of the rare class samples 
        were identified. This is a significant improvement over earlier iterations. However, low Precision (0.14)
        indicates many false positives for this class.
        """)

# Random Forest Subsection
def rf_model():
    st.markdown("Since the SMOTE is already been fine tuned, let's get into the fine tuning of the Random Forest model.")
    code = """
    param_grid_rf = {
        'classifier__n_estimators': [50, 100, 200, 300],
        'classifier__max_depth': [5, 10, 20, None],
        'classifier__class_weight': ['balanced', 'balanced_subsample'],
        'classifier__max_features': ['sqrt', 'log2', None],
        'classifier__min_samples_split': [2, 5, 10, 20],
        'classifier__min_samples_leaf': [1, 2, 5, 10],
    }
    
    # Define Random Forest model and pipeline
    rf_classifier = RandomForestClassifier(random_state=42)
    smote = SMOTE(sampling_strategy='minority', k_neighbors=5)  # Use the best SMOTE params
    pipeline = Pipeline(steps=[('smote', smote), ('classifier', rf_classifier)])

    # Perform grid search
    grid_search_rf = GridSearchCV(
        pipeline,
        param_grid_rf,
        scoring='f1_weighted',
        cv=5,
        verbose=1,
        n_jobs=-1
    )
    grid_search_rf.fit(X_train, y_train)
    """
    st.code(code)
    st.markdown("""
        And here is the result: Best Random Forest parameters:
        ```python
        Best GradientBoosting parameters: 
        {'classifier__class_weight': 'balanced_subsample', 'classifier__max_depth': 10, 'classifier__max_features': 'sqrt', 'classifier__min_samples_leaf': 1, 'classifier__min_samples_split': 10, 'classifier__n_estimators': 300}
        ```
        """)
    st.markdown("Let's see the performance of the best pipeline!")
    classification_report_md = """
    | Class       | Precision | Recall | F1-Score | Support |
    |-------------|-----------|--------|----------|---------|
    | 0.0         | 0.67      | 0.80   | 0.73     | 315     |
    | 1.0         | 0.34      | 0.25   | 0.29     | 140     |
    | 2.0         | 0.35      | 0.15   | 0.21     | 86      |
    | 3.0         | 0.12      | 0.67   | 0.21     | 6       |

    | Metric          | Precision | Recall | F1-Score | Support |
    |-----------------|-----------|--------|----------|---------|
    | **Accuracy**    |           |        | 0.56     | 547     |
    | **Macro Avg**   | 0.37      | 0.47   | 0.36     | 547     |
    | **Weighted Avg**| 0.53      | 0.56   | 0.53     | 547     |
    """
    st.markdown(classification_report_md)
    st.markdown("""
        - Class `0.0` (Majority Class):
            - Precision (0.67): Indicates that 67% of predictions for this class are correct.
            - Recall (0.80): Reflects that 80% of the true 0.0 instances were identified.
            - F1-score (0.73): Highlights strong overall performance for this class, as expected for the majority class.
        - Class `1.0` and `2.0` (Minority Classes):
            - Class `1.0`:
                - Precision (0.34) and Recall (0.25) are moderate, leading to a F1-score (0.29). The model struggles to
                identify and correctly predict this class, though it slightly outperforms class `2.0`.
            - Class `2.0`:
                - Precision (0.35) is comparable to class `1.0`, but Recall (0.15) is much lower, indicating a greater
                difficulty in capturing true instances of this class. The F1-score (0.21) remains low, highlighting the
                need for more focused optimization for this class.
        - Class `3.0` (Rare Class):
            - Precision (0.12): Many false positives, reflecting difficulty in making correct predictions.
            - Recall (0.67): The model captures two-thirds of true 3.0 instances, a strong improvement.
            - F1-score (0.21): Shows significant recall improvements but struggles with precision.
        """)

# Comparison Subsection
def comp_model():
    st.markdown("Lastly, let's make a comparison!")
    comparison_table_md = """
    | Metric                        | Gradient Boosting | Random Forest |
    |-------------------------------|-------------------|---------------|
    | **Class `0.0` F1-score**      | 0.72              | 0.73          |
    | **Class `1.0` F1-score**      | 0.23              | 0.29          |
    | **Class `2.0` F1-score**      | 0.23              | 0.21          |
    | **Class `3.0` F1-score**      | 0.22              | 0.21          |
    | **Weighted Avg F1-score**     | 0.51              | 0.53          |
    | **Macro Avg Recall**          | 0.42              | 0.47          |
    """
    st.markdown(comparison_table_md)
    st.markdown("""
        - Strengths of Random Forest:
            - Marginally better for minority classes (1.0) in terms of F1-score.
            - Slightly higher weighted average F1-score and macro recall.
        - Strengths of Gradient Boosting:
            - Comparable performance on rare and minority classes with slightly better overall precision.
        """)

if __name__ == "__main__":
    main()