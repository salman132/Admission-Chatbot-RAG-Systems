

import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_text_splitters import RecursiveCharacterTextSplitter
import csv
import json

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Parse JSON data
json_data = json.loads(open("New document 2.json").read())
universities = json_data["data"]

# Define CSV file path
csv_file = "universities.csv"

# Define CSV headers
headers = ["University Name", "Username", "Ranking", "Description", "State", "Country", "Acceptance Rate", "Average Net Price",
           "Student Loans Description", "Student Loans Per Year Amount", "Student Loans Per Year Percentage",
           "Average Debt At Graduation Amount", "Average Debt At Graduation Description",
           "Median Monthly Loan Payment Amount", "Median Monthly Loan Payment Description", "Aid and Grants Need Met",
           "Average Federal Grant Aid Per Year", "Student Receiving Grants Percentage",
           "Student Receiving Grants Description", "Average Institution Grant Aid Per Year",
           "Student Receiving Gift Aid Description", "Student Receiving Gift Aid Average Aid Per Year",
           "Student Receiving Gift Aid Average Aid Per Year Description", "Acceptance Rate", "Institution Type",
           "Male Student", "Size Of Town", "Female Student", "Student Organization", "Male Student From Usa",
           "On Campus Women's Center", "Female Student From Usa", "Lgbt Student Resource Group",
           "Level Of Institution", "In State Tuition Fee", "In State Tuition Fee Description", "Out State Tuition Fee",
           "Out State Tuition Fee Description", "Additional Cost Description", "Roam And Board", "Book And Suppliers",
           "ACT Needed", "SAT Needed", "Transcript Needed", "Phone Number", "Country", "City", "State", "Offered Programs"]
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=300,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)
# Open CSV file in write mode
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    # Create CSV writer
    writer = csv.writer(file)

    # Write headers to CSV
    writer.writerow(headers)
    # Write data rows to CSV
    for university in universities:
        row = [
            university["name"],
            university["user_name"],
            university["ranking"],
            university["description"],
            university["capex_data"]["value"]["address"]["state"],
            university["capex_data"]["value"]["address"]["country"],
            university["capex_data"]["value"]["acceptanceRate"],
            university["capex_data"]["value"]["averageNetPrice"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["loan_description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["loan_per_year_amount"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["loan_per_year_percentage"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["avg_debt_at_graduation_amount"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["avg_debt_at_graduation_description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["median_monthly_loan_payment_amount"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["student_loans"]
            ["median_monthly_loan_payment_description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["need_met"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["average_federal_grant_aid_per_year"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["student_receiving_grants_percentage"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["student_receiving_grants_description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["average_institution_grant_aid_per_year"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["student_receiving_gift_aid_description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["student_receiving_gift_avg_aid_per_year"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["aid_and_grants"]["student_receiving_gift_avg_aid_per_year_percentage"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["acceptance_rate"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["institution_type"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["male_student"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["size_of_town"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["female_student"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["student_organization"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["male_student_from_usa"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["on_campus_women_center"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["female_student_from_usa"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["key_campus_stats"]["lgbt_student_resource_group"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["level_of_institution"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["in_state"]["fee"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["in_state"]["description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["out_state"]["fee"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["out_state"]["description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["additional_cost"]["description"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["additional_cost"]["roam_and_board"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["tuition_cost_and_aid"]["additional_cost"]["book_and_suupliers"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["admission_requirements"]["act"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["admission_requirements"]["sat"],
            university["capex_data"]["value"]["profile_details"]["key_admission_stats"]["admission_requirements"]["transcript"],
            university["address"][0]["phone_number"],
            university["address"][0]["country"]["title"],
            university["address"][0]["city"]["title"],
            university["address"][0]["state"]["title"],
            university["programs"]
        ]
        writer.writerow(row)
with open('universities.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row
    for row in reader:
        # Construct a paragraph from the row
        paragraph = f"{row['University Name']} ({row['Username']}) is located in {row['City']}, {row['State']}, {row['Country']}. It is a {row['Institution Type']} institution with a ranking of {row['Ranking']}."
        paragraph += f" The acceptance rate is {row['Acceptance Rate']} and the average net price is {row['Average Net Price']} per year."

        # Student Loans Information
        paragraph += f"\n\nStudent Loans Information:"
        paragraph += f"\n- {row['Student Loans Description']}: {row['Student Loans Per Year Amount']} ({row['Student Loans Per Year Percentage']}%)"
        paragraph += f"\n- Average Debt At Graduation: {row['Average Debt At Graduation Amount']} ({row['Average Debt At Graduation Description']})"
        paragraph += f"\n- Median Monthly Loan Payment: {row['Median Monthly Loan Payment Amount']} ({row['Median Monthly Loan Payment Description']})"

        # Aid and Grants Information
        paragraph += f"\n\nAid and Grants Information:"
        paragraph += f"\n- Aid and Grants Need Met: {row['Aid and Grants Need Met']}"
        paragraph += f"\n- Average Federal Grant Aid Per Year: {row['Average Federal Grant Aid Per Year']}"
        paragraph += f"\n- Student Receiving Grants: {row['Student Receiving Grants Percentage']}% ({row['Student Receiving Grants Description']})"
        paragraph += f"\n- Average Institution Grant Aid Per Year: {row['Average Institution Grant Aid Per Year']}"
        paragraph += f"\n- Student Receiving Gift Aid: {row['Student Receiving Gift Aid Average Aid Per Year']} ({row['Student Receiving Gift Aid Average Aid Per Year Description']})"

        # Tuition and Fees
        paragraph += f"\n\nTuition and Fees:"
        paragraph += f"\n- In-State Tuition Fee: {row['In State Tuition Fee']} ({row['In State Tuition Fee Description']})"
        paragraph += f"\n- Out-State Tuition Fee: {row['Out State Tuition Fee']} ({row['Out State Tuition Fee Description']})"
        paragraph += f"\n- Additional Cost: {row['Additional Cost Description']}"
        paragraph += f"\n- Room and Board: {row['Roam And Board']}"
        paragraph += f"\n- Books and Supplies: {row['Book And Suppliers']}"

        # Admission Requirements
        paragraph += f"\n\nAdmission Requirements:"
        paragraph += f"\n- ACT Needed: {'Yes' if row['ACT Needed'] == 'True' else 'No'}"
        paragraph += f"\n- SAT Needed: {'Yes' if row['SAT Needed'] == 'True' else 'No'}"
        paragraph += f"\n- Transcript Needed: {'Yes' if row['Transcript Needed'] == 'True' else 'No'}"

        # Contact Information
        paragraph += f"\n\nContact Information:"
        paragraph += f"\n- Phone Number: {row['Phone Number']}"

        # Programs Offered
        programs = [program['title'] for program in eval(row['Offered Programs'])]
        program_list = ", ".join(programs)
        paragraph += f"\n\nPrograms Offered:\n{program_list}"

        texts = text_splitter.create_documents([paragraph])
        docsearchpdf = PineconeVectorStore.from_documents(texts, embeddings_model, index_name="collegeinfo")
