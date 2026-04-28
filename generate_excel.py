import pandas as pd

columns = [
    "Organization Name", "Advertisement Number", "Post Name", "Number of Vacancies", 
    "Age Limit", "Qualification", "Experience Required", "Salary / Fellowship", 
    "Job Location", "Selection Process", "Application Mode", "Important Dates", "Application Fee", "Job Type", "Key Skills"
]

data_aau = [{
    "Organization Name": "Assam Agricultural University",
    "Advertisement Number": "PHET/01/2023",
    "Post Name": "Technical Assistant (A)",
    "Number of Vacancies": "2",
    "Age Limit": "18-40 years",
    "Qualification": "B.V.Sc",
    "Experience Required": "Meat/Product Processing",
    "Salary / Fellowship": "₹14,000 - ₹60,000",
    "Job Location": "Assam",
    "Selection Process": "Written + Skill",
    "Application Mode": "Offline",
    "Important Dates": "21 Dec 2023",
    "Application Fee": "₹300",
    "Job Type": "Contract",
    "Key Skills": "Lab, Processing"
},
{
    "Organization Name": "Assam Agricultural University",
    "Advertisement Number": "PHET/01/2023",
    "Post Name": "Technical Assistant (B)",
    "Number of Vacancies": "1",
    "Age Limit": "18-40 years",
    "Qualification": "B.Tech (Agri/Mech)",
    "Experience Required": "Equipment Fabrication",
    "Salary / Fellowship": "₹14,000 - ₹60,000",
    "Job Location": "Assam",
    "Selection Process": "Written + Skill",
    "Application Mode": "Offline",
    "Important Dates": "21 Dec 2023",
    "Application Fee": "₹300",
    "Job Type": "Contract",
    "Key Skills": "Engineering"
}]

data_csir = [{
    "Organization Name": "CSIR-CBRI",
    "Advertisement Number": "CSIR-CBRI-05/2024",
    "Post Name": "Project Assistant (PAT-I)",
    "Number of Vacancies": "Not Specified",
    "Age Limit": "Up to 35 years",
    "Qualification": "B.Sc / B.Tech",
    "Experience Required": "Project-based",
    "Salary / Fellowship": "₹25,000 + HRA",
    "Job Location": "Roorkee",
    "Selection Process": "Walk-in",
    "Application Mode": "Walk-in",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Contract",
    "Key Skills": "Civil, Chemistry"
},
{
    "Organization Name": "CSIR-CBRI",
    "Advertisement Number": "CSIR-CBRI-05/2024",
    "Post Name": "Project Associate (PAT-II)",
    "Number of Vacancies": "Not Specified",
    "Age Limit": "Up to 40 years",
    "Qualification": "M.Tech / MSc",
    "Experience Required": "Project-based",
    "Salary / Fellowship": "₹28,000 - ₹42,000",
    "Job Location": "Roorkee",
    "Selection Process": "Walk-in",
    "Application Mode": "Walk-in",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Contract",
    "Key Skills": "Structural"
}]

data_nhm = [{
    "Organization Name": "NHM Maharashtra (AYUSH Mission)",
    "Advertisement Number": "Not Specified",
    "Post Name": "Program Manager",
    "Number of Vacancies": "1",
    "Age Limit": "18-38 years",
    "Qualification": "MBA Health",
    "Experience Required": "3+ years",
    "Salary / Fellowship": "₹45,000",
    "Job Location": "Maharashtra",
    "Selection Process": "Interview",
    "Application Mode": "Offline",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Not Specified",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NHM Maharashtra (PM-ABHIM)",
    "Advertisement Number": "Not Specified",
    "Post Name": "Finance Manager",
    "Number of Vacancies": "1",
    "Age Limit": "18-38 years",
    "Qualification": "CA / MBA Finance",
    "Experience Required": "3+ years",
    "Salary / Fellowship": "₹45,000",
    "Job Location": "Maharashtra",
    "Selection Process": "Interview",
    "Application Mode": "Offline",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Not Specified",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NHM Maharashtra (PM-ABHIM)",
    "Advertisement Number": "Not Specified",
    "Post Name": "Hospital Consultant",
    "Number of Vacancies": "1",
    "Age Limit": "18-38 years",
    "Qualification": "Medical Graduate",
    "Experience Required": "3 years",
    "Salary / Fellowship": "₹40,000",
    "Job Location": "Maharashtra",
    "Selection Process": "Interview",
    "Application Mode": "Offline",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Not Specified",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NHM Maharashtra (AYUSH Mission)",
    "Advertisement Number": "Not Specified",
    "Post Name": "Data Entry Operator",
    "Number of Vacancies": "1",
    "Age Limit": "18-38 years",
    "Qualification": "Graduate + Computer",
    "Experience Required": "1 year",
    "Salary / Fellowship": "₹18,000",
    "Job Location": "Maharashtra",
    "Selection Process": "Interview",
    "Application Mode": "Offline",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Not Specified",
    "Key Skills": "Not Specified"
}]

data_ntpc = [{
    "Organization Name": "NTPC Green Energy Ltd",
    "Advertisement Number": "01/25",
    "Post Name": "Engineer (Civil)",
    "Number of Vacancies": "40",
    "Age Limit": "Up to 30 years",
    "Qualification": "B.Tech Civil",
    "Experience Required": "3 years",
    "Salary / Fellowship": "₹11 LPA",
    "Job Location": "Pan India",
    "Selection Process": "CBT + Interview",
    "Application Mode": "Online",
    "Important Dates": "Not Specified",
    "Application Fee": "₹500",
    "Job Type": "Contract",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NTPC Green Energy Ltd",
    "Advertisement Number": "01/25",
    "Post Name": "Engineer (Electrical)",
    "Number of Vacancies": "80",
    "Age Limit": "Up to 30 years",
    "Qualification": "B.Tech Electrical",
    "Experience Required": "3 years",
    "Salary / Fellowship": "₹11 LPA",
    "Job Location": "Pan India",
    "Selection Process": "CBT + Interview",
    "Application Mode": "Online",
    "Important Dates": "Not Specified",
    "Application Fee": "₹500",
    "Job Type": "Contract",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NTPC Green Energy Ltd",
    "Advertisement Number": "01/25",
    "Post Name": "Engineer (Mechanical)",
    "Number of Vacancies": "15",
    "Age Limit": "Up to 30 years",
    "Qualification": "B.Tech Mechanical",
    "Experience Required": "3 years",
    "Salary / Fellowship": "₹11 LPA",
    "Job Location": "Pan India",
    "Selection Process": "CBT + Interview",
    "Application Mode": "Online",
    "Important Dates": "Not Specified",
    "Application Fee": "₹500",
    "Job Type": "Contract",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NTPC Green Energy Ltd",
    "Advertisement Number": "01/25",
    "Post Name": "Executive (HR)",
    "Number of Vacancies": "7",
    "Age Limit": "Up to 30 years",
    "Qualification": "MBA HR",
    "Experience Required": "3 years",
    "Salary / Fellowship": "₹11 LPA",
    "Job Location": "Pan India",
    "Selection Process": "CBT + Interview",
    "Application Mode": "Online",
    "Important Dates": "Not Specified",
    "Application Fee": "₹500",
    "Job Type": "Contract",
    "Key Skills": "Not Specified"
},
{
    "Organization Name": "NTPC Green Energy Ltd",
    "Advertisement Number": "01/25",
    "Post Name": "Executive (Finance)",
    "Number of Vacancies": "26",
    "Age Limit": "Up to 30 years",
    "Qualification": "CA/CMA",
    "Experience Required": "1 year",
    "Salary / Fellowship": "₹11 LPA",
    "Job Location": "Pan India",
    "Selection Process": "CBT + Interview",
    "Application Mode": "Online",
    "Important Dates": "Not Specified",
    "Application Fee": "₹500",
    "Job Type": "Contract",
    "Key Skills": "Not Specified"
}]

data_tanuvas = [{
    "Organization Name": "TANUVAS",
    "Advertisement Number": "18/Clinics/CSIR/2025",
    "Post Name": "Junior Research Fellow (JRF)",
    "Number of Vacancies": "1",
    "Age Limit": "Up to 28 years",
    "Qualification": "MSc / BVSc / BTech + NET/GATE",
    "Experience Required": "Molecular techniques",
    "Salary / Fellowship": "₹37,000",
    "Job Location": "Chennai",
    "Selection Process": "Written + Interview",
    "Application Mode": "Email + Walk-in",
    "Important Dates": "Not Specified",
    "Application Fee": "Not Specified",
    "Job Type": "Project",
    "Key Skills": "Not Specified"
}]

# --- PART B: AI Agent Idea ---
data_part_b = [{
    "AI Feature Concept": "Job Matcher AI (Resume Parser)",
    "Problem Solved": "Candidates don't know which government jobs they qualify for out of hundreds.",
    "How It Works": "Candidate uploads Resume (PDF). AI parses skills/degrees & maps them perfectly against the required qualifications of open government jobs.",
    "Impact for Jobyaari": "Massive boost in relevant applications. Users get an 'Eligibility Score' (e.g., 95% Match) instead of reading long PDFs."
}, {
    "AI Feature Concept": "Smart Notification Agent",
    "Problem Solved": "Candidates miss out on Walk-in interviews and document deadlines.",
    "How It Works": "An automated AI bot that texts/WhatsApp candidates 48 hours before an exam or interview date explicitly based on their applied location and role.",
    "Impact for Jobyaari": "Increases job seeker retention and makes the platform sticky/daily-use."
}, {
    "AI Feature Concept": "Document Authenticity & Formatting Checker",
    "Problem Solved": "Offline applications (like AAU/NHM) get rejected due to poor formatting or missing documents.",
    "How It Works": "Before mailing offline forms, users upload a picture. AI verifies if all required fields, signatures, and DD (Demand Drafts) are attached.",
    "Impact for Jobyaari": "Positions Jobyaari as a premium assistant, reducing rejection rates by 40%."
}]

with pd.ExcelWriter("c:/Users/prabu/Downloads/hur/Task1_Completed.xlsx", engine="openpyxl") as writer:
    pd.DataFrame(data_aau, columns=columns).to_excel(writer, sheet_name="AAU", index=False)
    pd.DataFrame(data_csir, columns=columns).to_excel(writer, sheet_name="CSIR", index=False)
    pd.DataFrame(data_nhm, columns=columns).to_excel(writer, sheet_name="NHM", index=False)
    pd.DataFrame(data_ntpc, columns=columns).to_excel(writer, sheet_name="NTPC", index=False)
    pd.DataFrame(data_tanuvas, columns=columns).to_excel(writer, sheet_name="TANUVAS", index=False)
    
    # Adding Part B for Brownie Points
    pd.DataFrame(data_part_b).to_excel(writer, sheet_name="Bonus - AI Agent Vision", index=False)

print("Perfect Excel file created with Bonus AI Tab!")