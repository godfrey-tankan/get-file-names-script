import os

folder_path = "/home/tnqn/Documents/New folder/" 

file_list = []  

for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):  
        file_list.append(file_name)


def read_titles(file_list):
    for file_name in file_list:
        title = file_name[:-4]  # Remove the file extension (.pdf)
        print(title)
    return "titles"

read_titles(['MSU AUGUST 2023 INTAKE.pdf', 'Peter Thiel - Zero to One.pdf', 'WP-From Hadoop to Data Lakehouse (1).pdf', 'Resume Lee Tabulo (5).pdf', 'Vacancy Notices.pdf', '_OceanofPDF.com_Black_Sunlight_-_Dambudzo_Marechera.pdf', 'The-One-Thing-EBook.pdf', 'ATTACHMENT CV_G MAZAMANA.pdf', 'tankan.pdf', 'Why Women Have Sex.pdf', 'The Art Of Seduction ( PDFDrive ).pdf', 'Broke-Millennial-Stop-Scrap-_Z-Library.pdf', 'Research Assistant Person Specification  Debt for Nature Swaps D4N in Africa.pdf', 'RISSC201_Exam_July_2022_Answers.pdf', 'Sexual-Intelligence-What-We-_Z-Library.pdf', 'Zimbabwe Latest Job Vacancies (2).pdf', 'Animal Farm by George Orwell.pdf', 'LEYTANS MEDICAL SUPPLIES.pdf', 'BuseFebIntake2024 (1).pdf', 'Poland .pdf', 'Summary of Programs & Fees 2024.pdf', 'Data Analyst Advert.pdf', 'Reflective_Losses_and_Derivative_Claims-DO.pdf', 'MECHANICAL ENGINEERING ASSIGNMENTS.pdf', '100496997.pdf', 'undergrad(1).pdf', 'Yolanda.pdf', 'A_Brief_History_of_Time_-_Stephen_Hawking.pdf', '_OceanofPDF.com_Dominion_-_Tom_Holland.pdf', 'So Long a Letter - Mariama Ba.pdf', 'leeroy tahanira IT cv.pdf', 'Makaza Prince Resume (1).pdf', 'Ecologist-PGT-Advert parks.pdf', 'Palazzo (Danielle Steel) (Z-Library).pdf', 'Spitzkop Lot 7 revised-1.pdf', 'COURSE OUTLINE.pdf', 'The+48+Laws+Of+Power.pdf', '15cs73_dec18-jan19.pdf', 'statistics_for_datascience.pdf', 'Routine Tracker.pdf', 'Anthills of the Savannah - Chinua Achebe.pdf', 'Advances in Intelligent Signal Processing and Data Mining.pdf', 'Telone Vacancy Notice No 2 of 2023 (003).pdf', 'Arrupe flyer 3.pdf', 'Summary of Fees JAN 2023.pdf', 'The Hard Thing About Hard Things_ Building a Business When There Are No Easy Answers ( PDFDrive ).pdf', 'Workshop Technician.pdf', 'Chimamanda_Ngozi_Adichie_-_Purple_Hibiscus.pdf', 'Act_Like_a_Lady_Think_Like_a_Man_-_Steve_Harvey.pdf', 'The 48 Laws of Power - Robert Greene.pdf', 'Job vacancy (Stores Controller) April 2024.pdf', 'ASSIGNMENT ONE.pdf', 'Job vacancy Contact Centre & Customer Experience Manager April 2024.pdf', 'Work Related Learning Vacancies.pdf', 'Critical Consciousness, Problem Solving and Life Skills -CCLS201-Module (3rd Edition) DR W. BANDA- 2023-fvv.pdf', 'dd-book2-flipbook-compressed.pdf', 'Gary_Chapman_-_Things_I_Wish_I_had_Known_Before_I_Got_Married (1).pdf', 'MSU FEBRUARY 2023 INTAKE ADVERT.pdf', 'Detecting-Forgery-Forensic-_Z-Library.pdf', 'MISA CYBER AND DATA PROTECTION ACT GUIDE_231016_081111.pdf', 'Summary of Fees 2024.pdf', '_OceanofPDF.com_An_Essay_On_Criticism_-_Alexander_Pope.pdf', 'Research Assistant Person Specification  Debt for Nature Swaps D4N in Africa-1.pdf', 'Jane_Austen_-_Pride_and_Prejudice.pdf', 'SUMMARY FEE STRUCTURE 2023.pdf', 'VACANCY NOTICE _ Research Data Analyst26022024.pdf', 'ASSIGNMENT FOUR.pdf', 'RATES_19_FEBRUARY_2024-INTERBANK_RATE.pdf', 'Curriculum Vita-WPS Office.pdf', 'Harry Potter  The complete Collection by J. K. Rowling (z-lib.org).pdf', 'FEES COMMUNIQUE.docx.pdf', 'Gmail - [CFP] Nordic Probabilistic AI School (ProbAI) — June 17-21, 2024 in Copenhagen (Denmark).pdf', 'Community Service Assessment Form.pdf', 'Step4Life GEN Membership Form.pdf', 'FULLTEXT01.pdf', 'The Song of Ice and Fire Series_ A Game of Thrones, A Clash of Kings, A Storm of Swords, and A Feast for Crows   ( PDFDrive ).pdf', 'Clean_Code__A_Handbook_of_Agile_Software_C_-_Robert_C_Martin.pdf', 'CV for Tanaka Rwizi.pdf', 'Ikigai.pdf', 'xTZbE2tQ1GxaU1vcGmphyIC7grkRb5DmiOt8mrLR-1.pdf', 'Arrupe flyer 1.pdf', 'Mastery ( PDFDrive ).pdf', 'Second Act (Danielle Steel) (Z-Library).pdf', 'SI 60 of 2024 Presidential Powers (Temporary Measures) (Zimbabwe Gold Notes Normal_240405_132538.pdf', 'null-1.pdf', 'Cloud Computing Architecture.pdf', 'External Advert - Various Positions (Sunday 14 April 2024).pdf', '2024 AUGUST INTAKE (2)-compressed.pdf', 'Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear) (z-lib.org).pdf', 'degree-programmes-offered-and-careers.pdf', 'ml_model_question_paper (1).pdf', 'Delphi Collected Works of Niccolò Machiavelli (Illustrated).pdf', 'PSV CIRCULAR 01 OF 2024.pdf', 'Wedding Invitation(3).pdf', 'how-to-win-friends-and-influence-people.pdf', '_OceanofPDF.com_Why_Men_Love_Bitches_-_Sherry_Argov.pdf', 'john_perkins_confessions_of_an_economic_hit_man.pdf', 'the-psychology-of-money-by-morgan-housel.pdf', 'ASSIGNMENT THREE_231112_181108.pdf', 'Act Like a Lady Think Like a Man.pdf', 'toaz.info-ndebele-lessonspdf-pr_4675e057b0151be1c08292dd6b64d8fa.pdf', "Panashe Mk's CV complete (1).pdf", 'MULTIPLE CHOICE QUESTIONS WITHOUT ANSWERS.pdf', 'Pres Chamisa Statement1..pdf', 'MSU FEB MARCH 2024 INTAKE.pdf', 'RESEARCH ASSIGNMENT.pdf', 'rachel-renee-russell-dork-diaries-11-tales-from-a-not-so-friendly-frenemy.pdf', '101_eassy_that_will_change_the_way_you_think_-_Brianna_wiest.pdf', 'Youth Integrity Research Call PDF.pdf', 'The-Art-of-Laziness-Overcom-_Z-Library.pdf', '2024 DIARY .pdf', 'T_Rwizi CV.pdf', 'VID.pdf', 'Vacancies - April 2024 Harare Region signed.pdf', 'UZ CUT OFF POINTS PDF.pdf', 'Why-Nations-Fail-Daron-Acemoglu.pdf', 'JOB ADVERT-IT HELP  DESK OFFICER.pdf', 'Mambo Zulu_CV.pdf', 'MUZENDA CHRIS THOMAS.pdf', 'Ukil_Book_Springer.pdf', 'ASSIGNMENT 1.pdf', 'Theodore Boone 07 The Accom (Z-Library).pdf', "Osline Kandeya's Attachment CV.pdf", 'The_House_of_Hunger_-_Dambudzo_Marechera.pdf', 'Letwin Mapungwana cv.pdf', 'null.pdf', 'Artificial Neural Network Assignment R216929j.pdf', 'AJU Short courses.pdf', 'Memory.A.Sithole_CV.pdf', '_will_you_forgive_me_.pdf', 'ZSE-Vacancies-February-2024_240213_183106.pdf', 'University Of Zimbabwe Cut Off Points 2023.pdf', 'ndebele.pdf', 'Intelligent Signal Processing.pdf', 'Curriculum vitae for Munyaradzi G Manjiche-1-2.pdf', 'ARRUPEPRINT.pdf', 'Tunesmith-Inside-the-Art-of_-_Z-Library.pdf', 'the subtle art of not giving a fuck.pdf', 'Short Courses 2023 (1).pdf', 'ABRAHAM_CV_R217037B_023833 (1).pdf', 'DECEMBER CCLS201 EXAM TIMETABLE -mcinserted 6-12-2023.pdf', 'Fu’adah_2020_IOP_Conf._Ser.__Mater._Sci._Eng._982_012005.pdf', 'AJU-short-course-application-form-2021.pdf', 'Application letter (2).pdf', 'he_Mayor_of_Casterbridge_-_Thomas_Hardy.pdf', 'The law of human nature Book by Robert Greene ( PDFDrive ).pdf', 'combinepdf(0).pdf', 'Chimamanda_Ngozi_Adichie_-_Half_of_a_Yellow_Sun.pdf', 'ASSIGNMENT 2.pdf', 'Storytelling with Data_ A Data Visualization Guide for Business Professionals ( PDFDrive ).pdf', 'How_To_Fuck_Women_Properly.pdf', 'How to Build a Cloud Computing Infrastructure.pdf', 'Surrounded By Idiots-1.pdf', 'Mr A.P Mucheki.pdf', '_OceanofPDF.com_Capone_-_John_Kobler.pdf', 'Artboard 1.pdf', 'The Wedding Planner (Danielle Steel) (Z-Library).pdf', 'CLEVER MWANANDIMAI finalCV cv.pdf', '144812 (1).pdf', 'Job vacancy Branch Supervisor April 2024.pdf', 'a-i0522e (1).pdf', 'How_to_Hug_a_Porcupine_-_Dr_Debbie_Joffe_Ellis.pdf', 'Why-Should-White-Guys-Have_-_Z-Library.pdf', 'FEE SCHEDULE SUMMARY 2024.pdf', 'Zimbabwe Latest Job Vacancies (3).pdf', 'Zeal-without-Burnout-Seven-_Z-Library.pdf', 'Research-Proposal-Template.pdf', '2023-2024  ICT STUDENT ATTACHEES 2023 ADVERT VACCANT POST REVISED.pdf', 'NewsHawks 29 March 2024.pdf', 'The-Masculine-in-Relationsh_-_Z-Library.pdf', 'CfBCs - Nyagadza, Chigora, Hassan & Bashar (2024).pdf', 'Job Adverts - Regional Center of Excellence for Forestry Biodiversity and Seascape Ecosystem.pdf', 'DOC-20180113-WA0038.pdf', 'Why_Africa_Is_Poor_-_Greg_Mills.pdf', '3286564400.pdf', 'The_Innovation_Secrets_of_Steve_Jobs_-_Carmine_Gallo.pdf', 'Expression of Interest FIATA YLP 2024.pdf', 'Richest_man_in_Babylon_George_Clason.pdf', 'Dork_Diaries__Holiday_Heartbreak.pdf', 'LAICAEND100 END OF BLOCK TEST 1.pdf', 'Abundance-Now.pdf', 'Innovation Dimension.pdf'])
