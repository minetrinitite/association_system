import db_ehd as ehd

SERVER = '192.168.99.100' #ip address of mongo instance
PORT = 32768
DB_NAME = 'ehb_base'
DB_COLLECTION = 'ehb_collection'

diagnoses = [{
    "id": 3,
    "name": "meningomyelitis",
    "status": 1,
    "criterion": ["severe headache", "sudden fever"],
    "date_of_issue": "24-01-2014",
    "name_of_doctor": "Alexander Belimov",
    "comment": "treatment with steroids in the case of autoimmune or inflammatory reaction usually produces a quick improvement of symptoms",
    "treatment": "course of anti-inflammatory steroid",
},
    {
    "id": 4,
    "name": "diabetes",
    "status": "0",
    "criterion": ["being very thirsty", "having dry, itchy skin", "urinating often"],
    "date_of_issue": "08-11-2012",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "dietary changes and exercise",
    "treatment": "insulin",
},
    {
    "id": 5,
    "name": "fibrinolytic purpura",
    "status": "2",
    "criterion": "bleeding under the skin",
    "date_of_issue": "17-05-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "protection of the patient from trauma",
    "treatment": "elective surgery",
}]

ehd.db_ehb_insert("Anastasiya Fedorova", "04-09-2010", "27-03-1983", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 6,
    "name": "disorder of 5th cranial nerve",
    "status": 0,
    "criterion": "weakness of jaw closure",
    "date_of_issue": "02-10-2013",
    "name_of_doctor": "Alexander Belimov",
    "comment": "prescribe carbamazepine",
    "treatment": "botox injections",
},
{
    "id": 7,
    "name": "cardiac infarction",
    "status": "2",
    "criterion": ["chest discomfort", "shortness of breath"],
    "date_of_issue": "18-12-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "healthy lifestyle changes",
    "treatment": "ACE inhibitors",
}]
ehd.db_ehb_insert("Pavel Senchikov", "18-12-2010", "27-03-1965", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 8,
    "name": "conjunctivitis",
    "status": 1,
    "criterion": "membranes lining the eyelids and covering the white part of the eye",
    "date_of_issue": "24-06-2014",
    "name_of_doctor": "Alexander Belimov",
    "comment": "eye drops to treat red eyes",
    "treatment": "oral antibiotics",
},
    {
    "id": 9,
    "name": "pyelonephritis",
    "status": "2",
    "criterion": ["anxiety", "vomiting", "fast heart rate"],
    "date_of_issue": "11-04-2013",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "avoid being around secondhand smoke",
    "treatment": "beta-blockers",
},
    {
    "id": 10,
    "name": "migraine",
    "status": "0",
    "criterion": ["watering of the eye on the side of the headache", "nasal congestion on the side of the headache"],
    "date_of_issue": "16-10-2011",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "lean protein",
    "treatment": "aspirin",
}]
ehd.db_ehb_insert("Aleksey Shilnikov", "29-09-2011", "15-09-1957", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 11,
    "name": "neck pain",
    "status": 2,
    "criterion": ["headache", "shoulder pain"],
    "date_of_issue": "21-03-2014",
    "name_of_doctor": "Alexander Belimov",
    "comment": "neck pillows for sleep",
    "treatment": "physical therapy",
},
    {
    "id": 12,
    "name": "dehydration",
    "status": "0",
    "criterion": ["sweating", "muscle cramps"],
    "date_of_issue": "09-11-2012",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "more water",
    "treatment": "replacing fluid by mouth",
},
    {
    "id": 13,
    "name": "osteodystrophy",
    "status": "1",
    "criterion": "bone and joint pain",
    "date_of_issue": "06-03-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "eat food that contain phosphorous",
    "treatment": "calcium carbonate",
}]
ehd.db_ehb_insert("Olga Tilova", "03-03-2011", "19-01-1993", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 14,
    "name": "latex allergy",
    "status": 0,
    "criterion": "red patches on the skin",
    "date_of_issue": "01-07-2015",
    "name_of_doctor": "Alexander Belimov",
    "comment": "avoidance of latex",
    "treatment": "epinephrine autoinjector",
},
    {
    "id": 15,
    "name": "flu",
    "status": "2",
    "criterion": ["fever", "cough", "fatigue"],
    "date_of_issue": "09-01-2014",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "warm showers, and warm compresses",
    "treatment": "antiviral drugs",
    }]
ehd.db_ehb_insert("Polina Serova", "23-03-2013", "24-04-2005", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 16,
    "name": "rheumatioid arthritis",
    "status": 1,
    "criterion": ["joint paint", "loss of joiny function" ,"joint deformity"],
    "date_of_issue": "21-07-2011",
    "name_of_doctor": "Alexander Belimov",
    "comment": "exercises that are less traumatic for the joints",
    "treatment": "hydroxychloroquine",
},
    {
    "id": 17,
    "name": "anemia",
    "status": "0",
    "criterion": ["tired", "appear pale"],
    "date_of_issue": "09-03-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "stimulate bone marrow red blood cell production",
    "treatment": "vitamin B12 injections",
},
    {
    "id": 18,
    "name": "rash",
    "status": "2",
    "criterion": "red cluster of acne on the neck",
    "date_of_issue": "06-11-2009",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "moisturizing lotions",
    "treatment": "topical antifungal medications that contain clotrimazole",
}]
ehd.db_ehb_insert("Oleg Reznik", "20-10-2009", "19-10-1973", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 22,
    "name": "narcolepsy",
    "status": 1,
    "criterion": ["cataplexy", "sleep paralysis", "hypnagogic hallucinations"],
    "date_of_issue": "07-11-2013",
    "name_of_doctor": "Alexander Belimov",
    "comment": "exercise and exposure to bright light can improve alertness",
    "treatment": "tricyclic antidepressants (TCAs)",
},
    {
    "id": 23,
    "name": "neuroblastoma",
    "status": "0",
    "criterion": "lump in the abdomen, neck",
    "date_of_issue": "13-08-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "X-rays of the chest, bones, and abdomen",
    "treatment": "magnetic resonance imaging",
}]
ehd.db_ehb_insert("Natalya Smolina", "23-04-2010", "18-04-1986", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 24,
    "name": "binge eating disoder",
    "status": 1,
    "criterion": ["eating faster than normal", " feeling disgusted with oneself, sad, or guilty after overeating"],
    "date_of_issue": "07-11-2013",
    "name_of_doctor": "Alexander Belimov",
    "comment": "behavior therapy",
    "treatment": "include lisdexamfetamine",
},
{
    "id": 25,
    "name": "broken foot",
    "status": "2",
    "criterion": "pain",
    "date_of_issue": "21-03-2010",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "inspection of the foot for swelling, bruising, deformities and open wounds",
    "treatment": "metatarsal fractures ",
},
{
    "id": 26,
    "name": "xerostomia",
    "status": "2",
    "criterion": "dry feeling in throat ",
    "date_of_issue": "20-03-2009",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "avoid caffeine, alcohol and tobacco",
    "treatment": "artificial OTC saliva",
}]
ehd.db_ehb_insert("Aleksander Kozin", "12-02-2009", "09-04-1993", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 27,
    "name": "norovirus infection",
    "status": 1,
    "criterion": ["watery diarrhea", "fever"],
    "date_of_issue": "10-07-2014",
    "name_of_doctor": "Alexander Belimov",
    "comment": "fluids containing electrolytes and sugars should be encouraged",
    "treatment": "drinking plenty of fluids",
},
    {
    "id": 28,
    "name": "dislocated shoulder",
    "status": "0",
    "criterion": "pain",
    "date_of_issue": "15-10-2013",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "rotate the shoulder blade, dislodging the humeral head",
    "treatment": "scapular manupulation",
},
    {
    "id": 29,
    "name": "deviated septum",
    "status": "2",
    "criterion": "difficulty breathing through the nose",
    "date_of_issue": "06-03-2013",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "including decongestants, antihistamines, or nasal sprays",
    "treatment": "septoplasty",
    }]
ehd.db_ehb_insert("Vladimiz Chernozv", "03-02-2010", "18-08-1977", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 30,
    "name": "panic attack",
    "status": 0,
    "criterion": ["racing or pounding heartbeat", "difficulty breathing"],
    "date_of_issue": "23-10-2015",
    "name_of_doctor": "Alexander Belimov",
    "comment": "avoid drinking alcohol and caffeinated beverages",
    "treatment": "herbal supplements",
},
    {
    "id": 31,
    "name": "pancreatitis",
    "status": "1",
    "criterion": "pain",
    "date_of_issue": "15-03-2014",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "abdominal pain that may radiate to the back",
    "treatment": "IV fluids to prevent dehydration while fasting",
},
    {
    "id": 32,
    "name": "parvovirus",
    "status": "2",
    "criterion": "weakness and lethargy",
    "date_of_issue": "06-09-2013",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "rarely, fifth disease can become complicated",
    "treatment": "parvovirus B19",
}]
ehd.db_ehb_insert("Maria Vasilieva", "03-11-2012", "02-06-1990", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 33,
    "name": "febrile seizures",
    "status": 0,
    "criterion": "moving limbs on both sides of the body",
    "date_of_issue": "03-12-2015",
    "name_of_doctor": "Alexander Belimov",
    "comment": "may be needed to check for signs of the infection",
    "treatment": "examining the blood",
},
    {
    "id": 34,
    "name": "pseudogout",
    "status": "2",
    "criterion": ["pain", "stiffness"],
    "date_of_issue": "28-03-2014",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "local ice applications and resting can help",
    "treatment": "anti-inflammatory drugs",
}]
ehd.db_ehb_insert("Anna Selchina", "03-06-2012", "12-11-1998", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )

diagnoses = [{
    "id": 35,
    "name": "keratitis",
    "status": 1,
    "criterion": ["pain", "tearing", "blurring of vision"],
    "date_of_issue": "23-10-2015",
    "name_of_doctor": "Alexander Belimov",
    "comment": "antiviral therapy to treat the infection",
    "treatment": "eyedrops, pills",
},
    {
    "id": 36,
    "name": "cavitis",
    "status": "1",
    "criterion": "increased sensitivity to foods that are cold, hot, or sweet",
    "date_of_issue": "10-09-2014",
    "name_of_doctor": "Elizaveta Vilkova",
    "comment": "sugary soft drinks and juices are especially harmful to the teeth",
    "treatment": "dental implants",
}]
ehd.db_ehb_insert("Michail Minin", "23-03-2009", "17-06-1900", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )


diagnoses = [{
    "name": "Skin cancer",
    "status": 0,
    "criterion": ["subcutaneous tumour", "skin darkening"],
    "date_of_issue": "12-04-2013",
    "name_of_doctor": "Alexander Belimov",
    "comment": "Healthy diet and daily activities recommended",
    "treatment": "tumour removal",
    },
    {
    "name": "headache",
        "status": "2",
        "criterion": "headache always without any reason",
        "date_of_issue": "13-04-2013",
        "name_of_doctor": "Elizaveta Vilkova",
        "comment": "it will be better in time",
        "treatment": "more sleep",
        }
]
ehd.db_ehb_insert("Alexey Matrosov", "13-11-2000", "13-11-1997", "Ekaterinburg, Uralskaya 1, 108", diagnoses, SERVER, PORT, DB_NAME, DB_COLLECTION )
