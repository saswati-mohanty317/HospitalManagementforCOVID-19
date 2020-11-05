from app import db, Doctor,Patient

db.create_all()

 ajay=Covid(

    user='Ajay Patel',
    statuss='Positive'
)
Ankita=Covid(
    user='Ankita',
    statuss='Negative'
)
ram=Covid(
    user='Ram',
    statuss='Positve'
)
aryan=Covid(
    user='Oberoi',
    statuss='Recovered'
)
kartik=Covid(
    user='Kartik',
   statuss='Recovered'
)
James=Covid(
    user='James',
    statuss='Recovered'
)
guddu=Covid(
    user='Guddu',
    statuss='Positive'
)

sam1=Doctor(
            username='Dr.Ajay Patel',
            department='Dermatology',
            timing="10 am - 4 pm",
            available='Yes')
fran=Doctor(username='Dr.Raj Sharma',
            department='ENT',
            timing="10 am - 6 pm",
            available='Yes')

fran2=Doctor(username='Dr.Ankita',
            department='Cardiologist',
            timing="10 am - 3 pm",
            available='No')

fran4=Doctor(username='Dr.Naman',
            department='Dermatologist',
            timing="11 am - 5 pm",
            available='Yes')
fran5=Doctor(username='Dr.Aryan',
            department='Pediatrician',
            timing="10 am - 6 pm",
            available='Yes')

pat1=Patient(name = 'Ajith Sharma',
    age = '22',
    location_room = '102a',
    location_bed = '4',
    status='Out of Operation',
    visting_time='10 am - 11 am',
    Num_vistors=2 )

pat2=Patient(name = 'Ranjan Patel',
    age = '44',
    location_room = '202a',
    location_bed = '1',
    status='In Operation',
    visting_time='4 pm - 5pm',
    Num_vistors=1 )

pat3=Patient(name = 'Ram Patel',
    age = '49',
    location_room = '222a',
    location_bed = '1',
    status='In Operation',
    visting_time='4 pm - 5pm',
    Num_vistors=2 )
pat4=Patient(name = 'Shankar',
    age = '19',
    location_room = '122a',
    location_bed = '8',
    status='Out of Operation',
    visting_time='1pm - 5pm',
    Num_vistors=3 )
pat5=Patient(name = 'Kapil',
    age = '72',
    location_room = '23e',
    location_bed = '1',
    status='Discharged',
    visting_time='NA',
    Num_vistors=2)
pat6=Patient(name = 'Rajiv',
    age = '18',
    location_room = '23e',
    location_bed = '2',
    status='Discharged',
    visting_time='NA',
    Num_vistors=2)
pat7=Patient(name = 'Ashish',
    age = '39',
    location_room = '23f',
    location_bed = '12',
    status='In ICU',
    visting_time='3pm - 4pm',
    Num_vistors=1)

print(sam1.id)
print(fran.id)

db.session.add_all([sam1,fran,fran2,fran4,fran5,pat1,pat2,pat3,pat4,pat5,pat6,pat7,ankita,kartik,ajay,ram,guddu,James,aryan])
db.session.commit()

