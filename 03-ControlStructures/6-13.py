good_influencer = 0

q1 = input('Do you have facebook: (Y/N)')
if q1 == 'Y':
    good_influencer += 1
q2 = input('Do you have twitter: (Y/N)')
if q2 == 'Y':
    good_influencer += 1
q3 = input('Do you have instagram: (Y/N)')
if q2 == 'Y':
    good_influencer += 1
if good_influencer >= 2:
    print('You are a good influencer')