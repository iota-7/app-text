import numpy as np

path_models = r'models'

columns =  ['Size of Lesion (<5mm/>5mm)', 'Flat/Raised', 'Pain', 'Color (Light/Dark)', 'Shape (Round/Irregular)', 'Fever', 'Location', 'Number (Sigular/Multiple)', 'Itching (Yes/No)', 'Scaly (Yes/No)']

diseases = ['Acne', 'Alopecia', 'Contact Dermatitis', 'Corns and Calluses', 'Drug Eruption', 'Folliculitis', 'Herpes Simplex', 'Genital Warts', 'Guttate Psoriasis', 'Halo Nevus', 'Hemangioma', 'Ichthyosis', 'Impetigo', 'Keloid Scar', 'Litchen Planus', 'Litchen Simplex Chronicus', 'Melasma', 'Molluscum Contagiosum', 'Nummular Dermatitis', 'Onychomycosis', 'Photocontact Dermatitis', 'Pityriasis Rosea', 'Pityriasis Versicolor', 'Plaque Psoriasis', 'Polymorphic Light Eruption', 'Ringworm of Body', 'Ringworm of Face', 'Ringworm of Hands', 'Ringworm of Scalp', 'Scabies', 'Seborrheic Dermatitis', 'Tinea Cruris', 'Urticaria', 'Vitiligo', 'Warts', 'Pityriasis Alba', 'Leprosy', 'Syphilis', 'Chancroid']

dic = {'Size of Lesion (<5mm/>5mm)': ['<5mm (Less than)', '>5mm (Gr than)'], 'Flat/Raised': ['Raised', 'Flat'], 'Pain': ['Maybe', 'No', 'Yes'], 'Color (Light/Dark)': ['Dark', 'Light', 'Red', 'Silvery', 'Dark Surronded by Light', 'Black', 'White', 'Pale'], 'Shape (Round/Irregular)': ['Round', 'Irregular', 'Coin Shaped', 'Regular'], 'Fever': ['No'], 'Location': ['Face', 'Back', 'Scalp', 'Hands & Feet', 'Feet', 'Genital Area', 'Hands', 'Trunk', 'Arms', 'Legs', 'Hairy Area', 'Lips', 'Nails', 'Sun Exposed Part', 'Elbows', 'Knees', 'Axilla(Under arms)', 'Covered Areas', 'Scalp and Face'], 'Number (Sigular/Multiple)': ['Multiple', 'Singular'], 'Itching (Yes/No)': ['No', 'Yes'], 'Scaly (Yes/No)': ['No', 'Yes']}

columns = np.array(columns)
diseases = np.array(diseases)


