import csv

with open('../data/Initial export/players.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row.get('position') == 'QB' or row.get('position') == 'RB' or row.get('position') == 'WR' or row.get('position') == 'TE' or row.get('position') == 'K' :
            print('Name:', row.get('firstName'), row.get('lastName'))
            print('Position:', row.get('position'))
            print('Team:', row.get('team'))
            print('Overall Rating:', row.get('playerBestOvr'))
            print('Age:', row.get('age'))
            print('Health Rating:', row.get('injuryRating'))
    
            qbOVR = ((.01 * float(row.get('accelRating'))) + (.16 * float(row.get('awareRating'))) + (.08 * float(row.get('playActionRating'))) + (.1 * float(row.get('speedRating'))) +(.15 * float(row.get('throwAccDeepRating'))) + (.15 * float(row.get('throwAccMidRating'))) + (.12 * float(row.get('throwAccShortRating'))) + (.03 * float(row.get('throwOnRunRating'))) + (.15 * float(row.get('throwPowerRating'))) + (.05 * float(row.get('throwUnderPressureRating'))))
            rbOVR = ((.1 * float(row.get('accelRating'))) + (.12 * float(row.get('awareRating'))) + (.11 * float(row.get('bCVRating'))) + (.01 * float(row.get('cITRating'))) + (.13 * float(row.get('carryRating'))) + (.06 * float(row.get('catchRating'))) + (.1 * float(row.get('changeOfDirectionRating'))) + (.08 * float(row.get('jukeMoveRating'))) + (.01 * float(row.get('releaseRating'))) + (.01 * float(row.get('routeRunMedRating'))) + (.01 * float(row.get('routeRunShortRating'))) + (.09 * float(row.get('speedRating'))) + (.08 * float(row.get('spinMoveRating'))) + (.02 * float(row.get('stiffArmRating'))) + (.02 * float(row.get('strengthRating'))) + (.05 * float(row.get('truckRating'))))
            wrOVR = ((.06 * float(row.get('accelRating'))) + (.1 * float(row.get('awareRating'))) + (.02 * float(row.get('bCVRating'))) + (.1 * float(row.get('cITRating'))) + (.03 * float(row.get('carryRating'))) + (.11 * float(row.get('catchRating'))) + (.08 * float(row.get('changeOfDirectionRating'))) + (.03 * float(row.get('jukeMoveRating'))) + (.04 * float(row.get('jumpRating'))) + (.08 * float(row.get('releaseRating'))) + (.05 * float(row.get('routeRunDeepRating'))) + (.05 * float(row.get('routeRunMedRating'))) + (.05 * float(row.get('routeRunShortRating'))) + (.03 * float(row.get('specCatchRating'))) + (.12 * float(row.get('speedRating'))) + (.03 * float(row.get('spinMoveRating'))) + (.02 * float(row.get('strengthRating'))))
            teOVR = ((.03 * float(row.get('accelRating'))) + (.12 * float(row.get('awareRating'))) + (.01 * float(row.get('bCVRating'))) + (.13 * float(row.get('cITRating'))) + (.03 * float(row.get('carryRating'))) + (.12 * float(row.get('catchRating'))) + (.03 * float(row.get('changeOfDirectionRating'))) + (.01 * float(row.get('jukeMoveRating'))) + (.04 * float(row.get('jumpRating'))) + (.08 * float(row.get('releaseRating'))) + (.05 * float(row.get('routeRunDeepRating'))) + (.06 * float(row.get('routeRunMedRating'))) + (.06 * float(row.get('routeRunShortRating'))) + (.05 * float(row.get('specCatchRating'))) + (.1 * float(row.get('speedRating'))) + (.01 * float(row.get('spinMoveRating'))) + (.02 * float(row.get('strengthRating'))) + (.04 * float(row.get('truckRating'))))
            kOVR = ((.1 * float(row.get('awareRating'))) + (.45 * float(row.get('kickAccRating'))) + (.45 * float(row.get('kickPowerRating'))))
    
            print('QB Overall Rating:', round(qbOVR, 1))
            print('RB Overall Rating:', round(rbOVR, 1))
            print('WR Overall Rating:', round(wrOVR, 1))
            print('TE Overall Rating:', round(teOVR, 1))
            print('K Overall Rating:', round(kOVR, 1), '\n')
        else :
            continue