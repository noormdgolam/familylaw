const attorneys = [
    {
        "name": "James Alason",
        "firm": "Law Offices of Smith & Alab",
        "location": "Capital City, Alabama",
        "state": "Alabama",
        "rating": "4.9",
        "reviews": 150,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithalab.com",
        "phone": "(555) 100-0101",
        "bio": "Dedicated family law practice in Alabama with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Amaman",
        "firm": "Alabama Family Legal Group",
        "location": "Major City, Alabama",
        "state": "Alabama",
        "rating": "4.7",
        "reviews": 85,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@alabamafamilylegalgroup.com",
        "phone": "(555) 200-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Alabama."
    },
    {
        "name": "James Alason",
        "firm": "Law Offices of Smith & Alas",
        "location": "Capital City, Alaska",
        "state": "Alaska",
        "rating": "4.9",
        "reviews": 157,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithalas.com",
        "phone": "(555) 101-0101",
        "bio": "Dedicated family law practice in Alaska with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Skaman",
        "firm": "Alaska Family Legal Group",
        "location": "Major City, Alaska",
        "state": "Alaska",
        "rating": "4.7",
        "reviews": 98,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@alaskafamilylegalgroup.com",
        "phone": "(555) 201-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Alaska."
    },
    {
        "name": "James Arison",
        "firm": "Law Offices of Smith & Ariz",
        "location": "Capital City, Arizona",
        "state": "Arizona",
        "rating": "4.9",
        "reviews": 164,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithariz.com",
        "phone": "(555) 102-0101",
        "bio": "Dedicated family law practice in Arizona with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Onaman",
        "firm": "Arizona Family Legal Group",
        "location": "Major City, Arizona",
        "state": "Arizona",
        "rating": "4.7",
        "reviews": 111,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@arizonafamilylegalgroup.com",
        "phone": "(555) 202-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Arizona."
    },
    {
        "name": "James Arkson",
        "firm": "Law Offices of Smith & Arka",
        "location": "Capital City, Arkansas",
        "state": "Arkansas",
        "rating": "4.9",
        "reviews": 171,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmitharka.com",
        "phone": "(555) 103-0101",
        "bio": "Dedicated family law practice in Arkansas with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Sasman",
        "firm": "Arkansas Family Legal Group",
        "location": "Major City, Arkansas",
        "state": "Arkansas",
        "rating": "4.7",
        "reviews": 124,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@arkansasfamilylegalgroup.com",
        "phone": "(555) 203-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Arkansas."
    },
    {
        "name": "James Calson",
        "firm": "Law Offices of Smith & Cali",
        "location": "Capital City, California",
        "state": "California",
        "rating": "4.9",
        "reviews": 178,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithcali.com",
        "phone": "(555) 104-0101",
        "bio": "Dedicated family law practice in California with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Niaman",
        "firm": "California Family Legal Group",
        "location": "Major City, California",
        "state": "California",
        "rating": "4.7",
        "reviews": 137,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@californiafamilylegalgroup.com",
        "phone": "(555) 204-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in California."
    },
    {
        "name": "James Colson",
        "firm": "Law Offices of Smith & Colo",
        "location": "Capital City, Colorado",
        "state": "Colorado",
        "rating": "4.9",
        "reviews": 185,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithcolo.com",
        "phone": "(555) 105-0101",
        "bio": "Dedicated family law practice in Colorado with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Adoman",
        "firm": "Colorado Family Legal Group",
        "location": "Major City, Colorado",
        "state": "Colorado",
        "rating": "4.7",
        "reviews": 150,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@coloradofamilylegalgroup.com",
        "phone": "(555) 205-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Colorado."
    },
    {
        "name": "James Conson",
        "firm": "Law Offices of Smith & Conn",
        "location": "Capital City, Connecticut",
        "state": "Connecticut",
        "rating": "4.9",
        "reviews": 192,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithconn.com",
        "phone": "(555) 106-0101",
        "bio": "Dedicated family law practice in Connecticut with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Cutman",
        "firm": "Connecticut Family Legal Group",
        "location": "Major City, Connecticut",
        "state": "Connecticut",
        "rating": "4.7",
        "reviews": 163,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@connecticutfamilylegalgroup.com",
        "phone": "(555) 206-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Connecticut."
    },
    {
        "name": "James Delson",
        "firm": "Law Offices of Smith & Dela",
        "location": "Capital City, Delaware",
        "state": "Delaware",
        "rating": "4.9",
        "reviews": 199,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithdela.com",
        "phone": "(555) 107-0101",
        "bio": "Dedicated family law practice in Delaware with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Areman",
        "firm": "Delaware Family Legal Group",
        "location": "Major City, Delaware",
        "state": "Delaware",
        "rating": "4.7",
        "reviews": 176,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@delawarefamilylegalgroup.com",
        "phone": "(555) 207-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Delaware."
    },
    {
        "name": "James Floson",
        "firm": "Law Offices of Smith & Flor",
        "location": "Capital City, Florida",
        "state": "Florida",
        "rating": "4.9",
        "reviews": 206,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithflor.com",
        "phone": "(555) 108-0101",
        "bio": "Dedicated family law practice in Florida with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Idaman",
        "firm": "Florida Family Legal Group",
        "location": "Major City, Florida",
        "state": "Florida",
        "rating": "4.7",
        "reviews": 189,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@floridafamilylegalgroup.com",
        "phone": "(555) 208-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Florida."
    },
    {
        "name": "James Geoson",
        "firm": "Law Offices of Smith & Geor",
        "location": "Capital City, Georgia",
        "state": "Georgia",
        "rating": "4.9",
        "reviews": 213,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithgeor.com",
        "phone": "(555) 109-0101",
        "bio": "Dedicated family law practice in Georgia with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Giaman",
        "firm": "Georgia Family Legal Group",
        "location": "Major City, Georgia",
        "state": "Georgia",
        "rating": "4.7",
        "reviews": 202,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@georgiafamilylegalgroup.com",
        "phone": "(555) 209-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Georgia."
    },
    {
        "name": "James Hawson",
        "firm": "Law Offices of Smith & Hawa",
        "location": "Capital City, Hawaii",
        "state": "Hawaii",
        "rating": "4.9",
        "reviews": 220,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithhawa.com",
        "phone": "(555) 110-0101",
        "bio": "Dedicated family law practice in Hawaii with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Aiiman",
        "firm": "Hawaii Family Legal Group",
        "location": "Major City, Hawaii",
        "state": "Hawaii",
        "rating": "4.7",
        "reviews": 215,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@hawaiifamilylegalgroup.com",
        "phone": "(555) 210-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Hawaii."
    },
    {
        "name": "James Idason",
        "firm": "Law Offices of Smith & Idah",
        "location": "Capital City, Idaho",
        "state": "Idaho",
        "rating": "4.9",
        "reviews": 227,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithidah.com",
        "phone": "(555) 111-0101",
        "bio": "Dedicated family law practice in Idaho with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ahoman",
        "firm": "Idaho Family Legal Group",
        "location": "Major City, Idaho",
        "state": "Idaho",
        "rating": "4.7",
        "reviews": 228,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@idahofamilylegalgroup.com",
        "phone": "(555) 211-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Idaho."
    },
    {
        "name": "James Illson",
        "firm": "Law Offices of Smith & Illi",
        "location": "Capital City, Illinois",
        "state": "Illinois",
        "rating": "4.9",
        "reviews": 234,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithilli.com",
        "phone": "(555) 112-0101",
        "bio": "Dedicated family law practice in Illinois with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Oisman",
        "firm": "Illinois Family Legal Group",
        "location": "Major City, Illinois",
        "state": "Illinois",
        "rating": "4.7",
        "reviews": 241,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@illinoisfamilylegalgroup.com",
        "phone": "(555) 212-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Illinois."
    },
    {
        "name": "James Indson",
        "firm": "Law Offices of Smith & Indi",
        "location": "Capital City, Indiana",
        "state": "Indiana",
        "rating": "4.9",
        "reviews": 241,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithindi.com",
        "phone": "(555) 113-0101",
        "bio": "Dedicated family law practice in Indiana with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Anaman",
        "firm": "Indiana Family Legal Group",
        "location": "Major City, Indiana",
        "state": "Indiana",
        "rating": "4.7",
        "reviews": 254,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@indianafamilylegalgroup.com",
        "phone": "(555) 213-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Indiana."
    },
    {
        "name": "James Iowson",
        "firm": "Law Offices of Smith & Iowa",
        "location": "Capital City, Iowa",
        "state": "Iowa",
        "rating": "4.9",
        "reviews": 248,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithiowa.com",
        "phone": "(555) 114-0101",
        "bio": "Dedicated family law practice in Iowa with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Owaman",
        "firm": "Iowa Family Legal Group",
        "location": "Major City, Iowa",
        "state": "Iowa",
        "rating": "4.7",
        "reviews": 267,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@iowafamilylegalgroup.com",
        "phone": "(555) 214-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Iowa."
    },
    {
        "name": "James Kanson",
        "firm": "Law Offices of Smith & Kans",
        "location": "Capital City, Kansas",
        "state": "Kansas",
        "rating": "4.9",
        "reviews": 255,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithkans.com",
        "phone": "(555) 115-0101",
        "bio": "Dedicated family law practice in Kansas with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Sasman",
        "firm": "Kansas Family Legal Group",
        "location": "Major City, Kansas",
        "state": "Kansas",
        "rating": "4.7",
        "reviews": 280,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@kansasfamilylegalgroup.com",
        "phone": "(555) 215-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Kansas."
    },
    {
        "name": "James Kenson",
        "firm": "Law Offices of Smith & Kent",
        "location": "Capital City, Kentucky",
        "state": "Kentucky",
        "rating": "4.9",
        "reviews": 262,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithkent.com",
        "phone": "(555) 116-0101",
        "bio": "Dedicated family law practice in Kentucky with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ckyman",
        "firm": "Kentucky Family Legal Group",
        "location": "Major City, Kentucky",
        "state": "Kentucky",
        "rating": "4.7",
        "reviews": 293,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@kentuckyfamilylegalgroup.com",
        "phone": "(555) 216-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Kentucky."
    },
    {
        "name": "James Louson",
        "firm": "Law Offices of Smith & Loui",
        "location": "Capital City, Louisiana",
        "state": "Louisiana",
        "rating": "4.9",
        "reviews": 269,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithloui.com",
        "phone": "(555) 117-0101",
        "bio": "Dedicated family law practice in Louisiana with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Anaman",
        "firm": "Louisiana Family Legal Group",
        "location": "Major City, Louisiana",
        "state": "Louisiana",
        "rating": "4.7",
        "reviews": 306,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@louisianafamilylegalgroup.com",
        "phone": "(555) 217-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Louisiana."
    },
    {
        "name": "James Maison",
        "firm": "Law Offices of Smith & Main",
        "location": "Capital City, Maine",
        "state": "Maine",
        "rating": "4.9",
        "reviews": 276,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmain.com",
        "phone": "(555) 118-0101",
        "bio": "Dedicated family law practice in Maine with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ineman",
        "firm": "Maine Family Legal Group",
        "location": "Major City, Maine",
        "state": "Maine",
        "rating": "4.7",
        "reviews": 319,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@mainefamilylegalgroup.com",
        "phone": "(555) 218-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Maine."
    },
    {
        "name": "James Marson",
        "firm": "Law Offices of Smith & Mary",
        "location": "Capital City, Maryland",
        "state": "Maryland",
        "rating": "4.9",
        "reviews": 283,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmary.com",
        "phone": "(555) 119-0101",
        "bio": "Dedicated family law practice in Maryland with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Andman",
        "firm": "Maryland Family Legal Group",
        "location": "Major City, Maryland",
        "state": "Maryland",
        "rating": "4.7",
        "reviews": 332,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@marylandfamilylegalgroup.com",
        "phone": "(555) 219-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Maryland."
    },
    {
        "name": "James Masson",
        "firm": "Law Offices of Smith & Mass",
        "location": "Capital City, Massachusetts",
        "state": "Massachusetts",
        "rating": "4.9",
        "reviews": 290,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmass.com",
        "phone": "(555) 120-0101",
        "bio": "Dedicated family law practice in Massachusetts with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ttsman",
        "firm": "Massachusetts Family Legal Group",
        "location": "Major City, Massachusetts",
        "state": "Massachusetts",
        "rating": "4.7",
        "reviews": 95,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@massachusettsfamilylegalgroup.com",
        "phone": "(555) 220-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Massachusetts."
    },
    {
        "name": "James Micson",
        "firm": "Law Offices of Smith & Mich",
        "location": "Capital City, Michigan",
        "state": "Michigan",
        "rating": "4.9",
        "reviews": 297,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmich.com",
        "phone": "(555) 121-0101",
        "bio": "Dedicated family law practice in Michigan with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ganman",
        "firm": "Michigan Family Legal Group",
        "location": "Major City, Michigan",
        "state": "Michigan",
        "rating": "4.7",
        "reviews": 108,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@michiganfamilylegalgroup.com",
        "phone": "(555) 221-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Michigan."
    },
    {
        "name": "James Minson",
        "firm": "Law Offices of Smith & Minn",
        "location": "Capital City, Minnesota",
        "state": "Minnesota",
        "rating": "4.9",
        "reviews": 304,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithminn.com",
        "phone": "(555) 122-0101",
        "bio": "Dedicated family law practice in Minnesota with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Otaman",
        "firm": "Minnesota Family Legal Group",
        "location": "Major City, Minnesota",
        "state": "Minnesota",
        "rating": "4.7",
        "reviews": 121,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@minnesotafamilylegalgroup.com",
        "phone": "(555) 222-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Minnesota."
    },
    {
        "name": "James Misson",
        "firm": "Law Offices of Smith & Miss",
        "location": "Capital City, Mississippi",
        "state": "Mississippi",
        "rating": "4.9",
        "reviews": 311,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmiss.com",
        "phone": "(555) 123-0101",
        "bio": "Dedicated family law practice in Mississippi with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ppiman",
        "firm": "Mississippi Family Legal Group",
        "location": "Major City, Mississippi",
        "state": "Mississippi",
        "rating": "4.7",
        "reviews": 134,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@mississippifamilylegalgroup.com",
        "phone": "(555) 223-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Mississippi."
    },
    {
        "name": "James Misson",
        "firm": "Law Offices of Smith & Miss",
        "location": "Capital City, Missouri",
        "state": "Missouri",
        "rating": "4.9",
        "reviews": 318,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmiss.com",
        "phone": "(555) 124-0101",
        "bio": "Dedicated family law practice in Missouri with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Uriman",
        "firm": "Missouri Family Legal Group",
        "location": "Major City, Missouri",
        "state": "Missouri",
        "rating": "4.7",
        "reviews": 147,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@missourifamilylegalgroup.com",
        "phone": "(555) 224-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Missouri."
    },
    {
        "name": "James Monson",
        "firm": "Law Offices of Smith & Mont",
        "location": "Capital City, Montana",
        "state": "Montana",
        "rating": "4.9",
        "reviews": 325,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithmont.com",
        "phone": "(555) 125-0101",
        "bio": "Dedicated family law practice in Montana with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Anaman",
        "firm": "Montana Family Legal Group",
        "location": "Major City, Montana",
        "state": "Montana",
        "rating": "4.7",
        "reviews": 160,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@montanafamilylegalgroup.com",
        "phone": "(555) 225-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Montana."
    },
    {
        "name": "James Nebson",
        "firm": "Law Offices of Smith & Nebr",
        "location": "Capital City, Nebraska",
        "state": "Nebraska",
        "rating": "4.9",
        "reviews": 332,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnebr.com",
        "phone": "(555) 126-0101",
        "bio": "Dedicated family law practice in Nebraska with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Skaman",
        "firm": "Nebraska Family Legal Group",
        "location": "Major City, Nebraska",
        "state": "Nebraska",
        "rating": "4.7",
        "reviews": 173,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@nebraskafamilylegalgroup.com",
        "phone": "(555) 226-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Nebraska."
    },
    {
        "name": "James Nevson",
        "firm": "Law Offices of Smith & Neva",
        "location": "Capital City, Nevada",
        "state": "Nevada",
        "rating": "4.9",
        "reviews": 339,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithneva.com",
        "phone": "(555) 127-0101",
        "bio": "Dedicated family law practice in Nevada with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Adaman",
        "firm": "Nevada Family Legal Group",
        "location": "Major City, Nevada",
        "state": "Nevada",
        "rating": "4.7",
        "reviews": 186,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@nevadafamilylegalgroup.com",
        "phone": "(555) 227-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Nevada."
    },
    {
        "name": "James Newson",
        "firm": "Law Offices of Smith & New ",
        "location": "Capital City, New Hampshire",
        "state": "New Hampshire",
        "rating": "4.9",
        "reviews": 346,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnew.com",
        "phone": "(555) 128-0101",
        "bio": "Dedicated family law practice in New Hampshire with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ireman",
        "firm": "New Hampshire Family Legal Group",
        "location": "Major City, New Hampshire",
        "state": "New Hampshire",
        "rating": "4.7",
        "reviews": 199,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@newhampshirefamilylegalgroup.com",
        "phone": "(555) 228-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in New Hampshire."
    },
    {
        "name": "James Newson",
        "firm": "Law Offices of Smith & New ",
        "location": "Capital City, New Jersey",
        "state": "New Jersey",
        "rating": "4.9",
        "reviews": 353,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnew.com",
        "phone": "(555) 129-0101",
        "bio": "Dedicated family law practice in New Jersey with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Seyman",
        "firm": "New Jersey Family Legal Group",
        "location": "Major City, New Jersey",
        "state": "New Jersey",
        "rating": "4.7",
        "reviews": 212,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@newjerseyfamilylegalgroup.com",
        "phone": "(555) 229-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in New Jersey."
    },
    {
        "name": "James Newson",
        "firm": "Law Offices of Smith & New ",
        "location": "Capital City, New Mexico",
        "state": "New Mexico",
        "rating": "4.9",
        "reviews": 360,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnew.com",
        "phone": "(555) 130-0101",
        "bio": "Dedicated family law practice in New Mexico with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Icoman",
        "firm": "New Mexico Family Legal Group",
        "location": "Major City, New Mexico",
        "state": "New Mexico",
        "rating": "4.7",
        "reviews": 225,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@newmexicofamilylegalgroup.com",
        "phone": "(555) 230-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in New Mexico."
    },
    {
        "name": "James Newson",
        "firm": "Law Offices of Smith & New ",
        "location": "Capital City, New York",
        "state": "New York",
        "rating": "4.9",
        "reviews": 367,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnew.com",
        "phone": "(555) 131-0101",
        "bio": "Dedicated family law practice in New York with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Orkman",
        "firm": "New York Family Legal Group",
        "location": "Major City, New York",
        "state": "New York",
        "rating": "4.7",
        "reviews": 238,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@newyorkfamilylegalgroup.com",
        "phone": "(555) 231-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in New York."
    },
    {
        "name": "James Norson",
        "firm": "Law Offices of Smith & Nort",
        "location": "Capital City, North Carolina",
        "state": "North Carolina",
        "rating": "4.9",
        "reviews": 374,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnort.com",
        "phone": "(555) 132-0101",
        "bio": "Dedicated family law practice in North Carolina with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Inaman",
        "firm": "North Carolina Family Legal Group",
        "location": "Major City, North Carolina",
        "state": "North Carolina",
        "rating": "4.7",
        "reviews": 251,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@northcarolinafamilylegalgroup.com",
        "phone": "(555) 232-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in North Carolina."
    },
    {
        "name": "James Norson",
        "firm": "Law Offices of Smith & Nort",
        "location": "Capital City, North Dakota",
        "state": "North Dakota",
        "rating": "4.9",
        "reviews": 381,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithnort.com",
        "phone": "(555) 133-0101",
        "bio": "Dedicated family law practice in North Dakota with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Otaman",
        "firm": "North Dakota Family Legal Group",
        "location": "Major City, North Dakota",
        "state": "North Dakota",
        "rating": "4.7",
        "reviews": 264,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@northdakotafamilylegalgroup.com",
        "phone": "(555) 233-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in North Dakota."
    },
    {
        "name": "James Ohison",
        "firm": "Law Offices of Smith & Ohio",
        "location": "Capital City, Ohio",
        "state": "Ohio",
        "rating": "4.9",
        "reviews": 388,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithohio.com",
        "phone": "(555) 134-0101",
        "bio": "Dedicated family law practice in Ohio with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Hioman",
        "firm": "Ohio Family Legal Group",
        "location": "Major City, Ohio",
        "state": "Ohio",
        "rating": "4.7",
        "reviews": 277,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@ohiofamilylegalgroup.com",
        "phone": "(555) 234-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Ohio."
    },
    {
        "name": "James Oklson",
        "firm": "Law Offices of Smith & Okla",
        "location": "Capital City, Oklahoma",
        "state": "Oklahoma",
        "rating": "4.9",
        "reviews": 395,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithokla.com",
        "phone": "(555) 135-0101",
        "bio": "Dedicated family law practice in Oklahoma with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Omaman",
        "firm": "Oklahoma Family Legal Group",
        "location": "Major City, Oklahoma",
        "state": "Oklahoma",
        "rating": "4.7",
        "reviews": 290,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@oklahomafamilylegalgroup.com",
        "phone": "(555) 235-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Oklahoma."
    },
    {
        "name": "James Oreson",
        "firm": "Law Offices of Smith & Oreg",
        "location": "Capital City, Oregon",
        "state": "Oregon",
        "rating": "4.9",
        "reviews": 402,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithoreg.com",
        "phone": "(555) 136-0101",
        "bio": "Dedicated family law practice in Oregon with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Gonman",
        "firm": "Oregon Family Legal Group",
        "location": "Major City, Oregon",
        "state": "Oregon",
        "rating": "4.7",
        "reviews": 303,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@oregonfamilylegalgroup.com",
        "phone": "(555) 236-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Oregon."
    },
    {
        "name": "James Penson",
        "firm": "Law Offices of Smith & Penn",
        "location": "Capital City, Pennsylvania",
        "state": "Pennsylvania",
        "rating": "4.9",
        "reviews": 409,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithpenn.com",
        "phone": "(555) 137-0101",
        "bio": "Dedicated family law practice in Pennsylvania with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Niaman",
        "firm": "Pennsylvania Family Legal Group",
        "location": "Major City, Pennsylvania",
        "state": "Pennsylvania",
        "rating": "4.7",
        "reviews": 316,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@pennsylvaniafamilylegalgroup.com",
        "phone": "(555) 237-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Pennsylvania."
    },
    {
        "name": "James Rhoson",
        "firm": "Law Offices of Smith & Rhod",
        "location": "Capital City, Rhode Island",
        "state": "Rhode Island",
        "rating": "4.9",
        "reviews": 416,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithrhod.com",
        "phone": "(555) 138-0101",
        "bio": "Dedicated family law practice in Rhode Island with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Andman",
        "firm": "Rhode Island Family Legal Group",
        "location": "Major City, Rhode Island",
        "state": "Rhode Island",
        "rating": "4.7",
        "reviews": 329,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@rhodeislandfamilylegalgroup.com",
        "phone": "(555) 238-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Rhode Island."
    },
    {
        "name": "James Souson",
        "firm": "Law Offices of Smith & Sout",
        "location": "Capital City, South Carolina",
        "state": "South Carolina",
        "rating": "4.9",
        "reviews": 423,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithsout.com",
        "phone": "(555) 139-0101",
        "bio": "Dedicated family law practice in South Carolina with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Inaman",
        "firm": "South Carolina Family Legal Group",
        "location": "Major City, South Carolina",
        "state": "South Carolina",
        "rating": "4.7",
        "reviews": 92,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@southcarolinafamilylegalgroup.com",
        "phone": "(555) 239-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in South Carolina."
    },
    {
        "name": "James Souson",
        "firm": "Law Offices of Smith & Sout",
        "location": "Capital City, South Dakota",
        "state": "South Dakota",
        "rating": "4.9",
        "reviews": 430,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithsout.com",
        "phone": "(555) 140-0101",
        "bio": "Dedicated family law practice in South Dakota with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Otaman",
        "firm": "South Dakota Family Legal Group",
        "location": "Major City, South Dakota",
        "state": "South Dakota",
        "rating": "4.7",
        "reviews": 105,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@southdakotafamilylegalgroup.com",
        "phone": "(555) 240-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in South Dakota."
    },
    {
        "name": "James Tenson",
        "firm": "Law Offices of Smith & Tenn",
        "location": "Capital City, Tennessee",
        "state": "Tennessee",
        "rating": "4.9",
        "reviews": 437,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithtenn.com",
        "phone": "(555) 141-0101",
        "bio": "Dedicated family law practice in Tennessee with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Seeman",
        "firm": "Tennessee Family Legal Group",
        "location": "Major City, Tennessee",
        "state": "Tennessee",
        "rating": "4.7",
        "reviews": 118,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@tennesseefamilylegalgroup.com",
        "phone": "(555) 241-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Tennessee."
    },
    {
        "name": "James Texson",
        "firm": "Law Offices of Smith & Texa",
        "location": "Capital City, Texas",
        "state": "Texas",
        "rating": "4.9",
        "reviews": 444,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithtexa.com",
        "phone": "(555) 142-0101",
        "bio": "Dedicated family law practice in Texas with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Xasman",
        "firm": "Texas Family Legal Group",
        "location": "Major City, Texas",
        "state": "Texas",
        "rating": "4.7",
        "reviews": 131,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@texasfamilylegalgroup.com",
        "phone": "(555) 242-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Texas."
    },
    {
        "name": "James Utason",
        "firm": "Law Offices of Smith & Utah",
        "location": "Capital City, Utah",
        "state": "Utah",
        "rating": "4.9",
        "reviews": 151,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithutah.com",
        "phone": "(555) 143-0101",
        "bio": "Dedicated family law practice in Utah with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Tahman",
        "firm": "Utah Family Legal Group",
        "location": "Major City, Utah",
        "state": "Utah",
        "rating": "4.7",
        "reviews": 144,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@utahfamilylegalgroup.com",
        "phone": "(555) 243-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Utah."
    },
    {
        "name": "James Verson",
        "firm": "Law Offices of Smith & Verm",
        "location": "Capital City, Vermont",
        "state": "Vermont",
        "rating": "4.9",
        "reviews": 158,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithverm.com",
        "phone": "(555) 144-0101",
        "bio": "Dedicated family law practice in Vermont with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ontman",
        "firm": "Vermont Family Legal Group",
        "location": "Major City, Vermont",
        "state": "Vermont",
        "rating": "4.7",
        "reviews": 157,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@vermontfamilylegalgroup.com",
        "phone": "(555) 244-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Vermont."
    },
    {
        "name": "James Virson",
        "firm": "Law Offices of Smith & Virg",
        "location": "Capital City, Virginia",
        "state": "Virginia",
        "rating": "4.9",
        "reviews": 165,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithvirg.com",
        "phone": "(555) 145-0101",
        "bio": "Dedicated family law practice in Virginia with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Niaman",
        "firm": "Virginia Family Legal Group",
        "location": "Major City, Virginia",
        "state": "Virginia",
        "rating": "4.7",
        "reviews": 170,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@virginiafamilylegalgroup.com",
        "phone": "(555) 245-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Virginia."
    },
    {
        "name": "James Wasson",
        "firm": "Law Offices of Smith & Wash",
        "location": "Capital City, Washington",
        "state": "Washington",
        "rating": "4.9",
        "reviews": 172,
        "image": "https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithwash.com",
        "phone": "(555) 146-0101",
        "bio": "Dedicated family law practice in Washington with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Tonman",
        "firm": "Washington Family Legal Group",
        "location": "Major City, Washington",
        "state": "Washington",
        "rating": "4.7",
        "reviews": 183,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@washingtonfamilylegalgroup.com",
        "phone": "(555) 246-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Washington."
    },
    {
        "name": "James Wesson",
        "firm": "Law Offices of Smith & West",
        "location": "Capital City, West Virginia",
        "state": "West Virginia",
        "rating": "4.9",
        "reviews": 179,
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithwest.com",
        "phone": "(555) 147-0101",
        "bio": "Dedicated family law practice in West Virginia with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Niaman",
        "firm": "West Virginia Family Legal Group",
        "location": "Major City, West Virginia",
        "state": "West Virginia",
        "rating": "4.7",
        "reviews": 196,
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@westvirginiafamilylegalgroup.com",
        "phone": "(555) 247-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in West Virginia."
    },
    {
        "name": "James Wisson",
        "firm": "Law Offices of Smith & Wisc",
        "location": "Capital City, Wisconsin",
        "state": "Wisconsin",
        "rating": "4.9",
        "reviews": 186,
        "image": "https://images.unsplash.com/photo-1577415124269-b9140d420bf3?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithwisc.com",
        "phone": "(555) 148-0101",
        "bio": "Dedicated family law practice in Wisconsin with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Sinman",
        "firm": "Wisconsin Family Legal Group",
        "location": "Major City, Wisconsin",
        "state": "Wisconsin",
        "rating": "4.7",
        "reviews": 209,
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@wisconsinfamilylegalgroup.com",
        "phone": "(555) 248-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Wisconsin."
    },
    {
        "name": "James Wyoson",
        "firm": "Law Offices of Smith & Wyom",
        "location": "Capital City, Wyoming",
        "state": "Wyoming",
        "rating": "4.9",
        "reviews": 193,
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Divorce",
            "Child Custody",
            "Alimony"
        ],
        "verified": true,
        "email": "consult@lawofficesofsmithwyom.com",
        "phone": "(555) 149-0101",
        "bio": "Dedicated family law practice in Wyoming with over 20 years of experience handling complex divorce and custody cases."
    },
    {
        "name": "Sarah Ingman",
        "firm": "Wyoming Family Legal Group",
        "location": "Major City, Wyoming",
        "state": "Wyoming",
        "rating": "4.7",
        "reviews": 222,
        "image": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?q=80&w=200&auto=format&fit=crop",
        "specialties": [
            "Mediation",
            "Property Division",
            "Paternity"
        ],
        "verified": false,
        "email": "info@wyomingfamilylegalgroup.com",
        "phone": "(555) 249-0202",
        "bio": "Focusing on amicable dispute resolution and aggressive litigation when necessary for families in Wyoming."
    }
];