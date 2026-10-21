# Algorithm and Pseudocode — Hospital Billing and Patient Classification

## Algorithm

1. Start and define the senior age, concession percentage, and bill-category limits.
2. Input the number of patients. Keep asking until it is greater than zero.
3. Create an empty list for patient records and set the summary totals to zero.
4. Repeat for each patient:
   - Input the name and ask again if it is blank.
   - Input age and ask again if it is negative.
   - Input consultation, diagnostic, and treatment fees; ask again for any negative fee.
   - Add the three fees to calculate the gross bill.
   - If age is at least 60, calculate a 10% concession; otherwise use zero.
   - Subtract the concession from the gross bill.
   - Classify the final bill as LOW, MODERATE, or HIGH according to the assumed limits.
   - Store the patient's details and update the totals.
   - Display the itemised bill and category.
5. Display the number of patients, gross total, concession total, final payable total, and count for each bill category.
6. Stop.

## Pseudocode

~~~text
BEGIN
    SENIOR_AGE <- 60
    CONCESSION_PERCENT <- 10
    LOW_LIMIT <- 1000
    MODERATE_LIMIT <- 5000

    INPUT number_of_patients
    WHILE number_of_patients <= 0
        DISPLAY "Enter a number greater than zero"
        INPUT number_of_patients
    END WHILE

    patient_records <- empty list
    gross_total <- 0
    concession_total <- 0
    payable_total <- 0

    FOR each patient from 1 to number_of_patients
        INPUT patient_name
        WHILE patient_name is blank
            DISPLAY "Name cannot be blank"
            INPUT patient_name
        END WHILE

        INPUT age
        WHILE age < 0
            DISPLAY "Age cannot be negative"
            INPUT age
        END WHILE

        INPUT consultation_fee, diagnostic_fee, treatment_fee
        WHILE any fee < 0
            DISPLAY "Fee cannot be negative"
            INPUT the invalid fee again
        END WHILE

        gross <- consultation_fee + diagnostic_fee + treatment_fee
        IF age >= SENIOR_AGE
            concession <- gross * CONCESSION_PERCENT / 100
        ELSE
            concession <- 0
        END IF

        final_bill <- gross - concession
        IF final_bill <= LOW_LIMIT
            category <- "LOW"
        ELSE IF final_bill <= MODERATE_LIMIT
            category <- "MODERATE"
        ELSE
            category <- "HIGH"
        END IF

        APPEND patient details, gross, concession, final_bill, and category
        UPDATE gross_total, concession_total, payable_total
        DISPLAY itemised bill
    END FOR

    DISPLAY totals and count records in LOW, MODERATE, and HIGH categories
END
~~~

## Policy assumptions

The case study does not specify exact thresholds. This solution assumes a 10% concession for patients aged 60 or older, LOW up to Rs. 1,000, MODERATE above Rs. 1,000 through Rs. 5,000, and HIGH above Rs. 5,000. These are for an academic demonstration only.
